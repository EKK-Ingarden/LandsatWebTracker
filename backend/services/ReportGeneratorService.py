from backend.entities import LandsatData


class ReportGeneratorService:
    def __init__(self, data: LandsatData):
        self.Data = data

    def generate_csv_report(self):
        raise NotImplementedError
