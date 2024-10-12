import structlog
from sqlalchemy.orm import Session

from backend.models.report import Report
from backend.schemas.landsat.landsat_api_by_id_advanced import LandsatAdvancedAPIById


def write_report_to_db(scene_id: str, db: Session):
    try:
        landsat_item = LandsatAdvancedAPIById(scene_id=scene_id).first_result
        print("Processed")
        db.query(Report).filter(scene_id == Report.scene_id).update(
            {
                "is_processed": True,
                "raw_data": landsat_item.model_dump_json(),
            }
        )
        db.commit()
    except Exception as e:
        structlog.get_logger().error(f"Error while building LandsatItem from {scene_id}: {e}")
