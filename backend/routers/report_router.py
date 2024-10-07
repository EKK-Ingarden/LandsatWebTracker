from datetime import datetime, timedelta

import structlog
from fastapi import APIRouter, BackgroundTasks, Depends
from gotrue import UserResponse
from sqlalchemy.orm import Session

from backend import models, schemas
from backend.database import get_db
from backend.schemas.landsat.landsat_item_advanced import LandsatAdvancedItem
from backend.schemas.structures.report_result import (
    ReportResultError,
    ReportResultProcess,
    ReportResultSuccess,
)
from backend.tasks.write_report import write_report_to_db
from backend.utils.auth import get_current_user

logger = structlog.get_logger()

report_router = APIRouter()


@report_router.get("/generate_report")
async def generate_report(scene_id: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    query = db.query(models.Report).filter_by(scene_id=scene_id)
    report = query.first()

    if query.scalar():
        if report.is_processed:
            return ReportResultSuccess(
                is_processed=report.is_processed,
                scene_id=report.scene_id,
                created_at=report.created_at,
                data=LandsatAdvancedItem.model_validate(report.raw_data),
            )

        if datetime.now() - report.created_at < timedelta(minutes=10):
            return ReportResultProcess(is_processed=False, scene_id=report.scene_id, created_at=report.created_at)

        if datetime.now() - report.created_at > timedelta(minutes=10):
            db.delete(report)

    db.add(
        models.Report(
            scene_id=scene_id,
            created_at=datetime.now(),
        )
    )

    db.commit()

    background_tasks.add_task(write_report_to_db, scene_id, db)

    return ReportResultProcess(is_processed=False, scene_id=scene_id, created_at=datetime.now())


@report_router.get("/get_report")
async def get_report(scene_id: str, db: Session = Depends(get_db)):
    query = db.query(models.Report).filter_by(scene_id=scene_id)
    report = query.first()

    if not query.scalar():
        return ReportResultError(scene_id=scene_id, error="Report not found")

    if not report.is_processed:
        return ReportResultProcess(
            is_processed=report.is_processed,
            scene_id=report.scene_id,
            created_at=report.created_at,
        )

    return ReportResultSuccess(
        is_processed=report.is_processed,
        scene_id=report.scene_id,
        created_at=report.created_at,
        data=LandsatAdvancedItem.model_validate_json(report.raw_data),
    )


@report_router.get("/get_reports", response_model=list[schemas.Report])
async def get_reports(user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    # todo: return only user reports
    reports = db.query(models.Report).all()

    return reports
