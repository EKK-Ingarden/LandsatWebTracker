import sys

from sqlalchemy.orm import Session

from backend.models.report import Report
from backend.schemas.landsat.landsat_api_by_id_advanced import LandsatAdvancedAPIById


def write_report_to_db(scene_id: str, db: Session):
    print("working")
    landsat_item = LandsatAdvancedAPIById(scene_id=scene_id).first_result
    print("afterwaited")
    print(sys.getsizeof(landsat_item.model_dump_json()))
    db.query(Report).filter(Report.scene_id == scene_id).update(
        {
            "is_processed": True,
            "raw_data": landsat_item.model_dump_json(),
        }
    )
    print("dumped")
    db.commit()
