from backend.entities import LandsatData


class ReportGeneratorService:
    @staticmethod
    def generate_csv_report(self, data: LandsatData):
        raise NotImplementedError
