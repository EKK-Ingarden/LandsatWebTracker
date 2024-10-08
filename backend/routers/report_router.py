import json
from datetime import datetime

import structlog
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from gotrue import UserResponse
from sqlalchemy.orm import Session

from backend import models, schemas
from backend.database import get_db
from backend.schemas.landsat.landsat_item_advanced import LandsatAdvancedItem
from backend.tasks.write_report import write_report_to_db
from backend.utils.auth import get_current_user

logger = structlog.get_logger()

report_router = APIRouter()


def get_report_by_scene_id(scene_id: str, db: Session):
    query = db.query(models.Report).filter_by(scene_id=scene_id)
    return query.first()


def add_new_processing_report(scene_id: str, db: Session):
    new_report = models.Report(
        scene_id=scene_id,
        created_at=datetime.now(),
    )
    db.add(new_report)
    db.commit()


@report_router.post("/generate_report", status_code=202)
async def generate_report(scene_id: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    report = get_report_by_scene_id(scene_id, db)
    if report:
        if report.is_processed:
            raise HTTPException(status_code=409, detail="Report already processed")
        else:
            raise HTTPException(status_code=402, detail="Report is being processed")

    add_new_processing_report(scene_id, db)
    background_tasks.add_task(write_report_to_db, scene_id, db)

    return {"message": "Report added to processing queue"}


@report_router.get("/get_report")
async def get_report(scene_id: str, db: Session = Depends(get_db)) -> LandsatAdvancedItem:
    report = get_report_by_scene_id(scene_id, db)

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    if not report.is_processed:
        raise HTTPException(status_code=402, detail="Report is not processed yet")

    return LandsatAdvancedItem.model_validate(json.loads(str(report.raw_data)))


@report_router.get("/get_reports", response_model=list[schemas.Report])
async def get_reports(user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    # todo: return only user reports
    reports = db.query(models.Report).all()

    return reports
