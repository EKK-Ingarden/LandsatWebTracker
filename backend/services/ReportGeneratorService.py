from classes import LandSatData


class ReportGeneratorService:
    def __init__(self, Data: LandSatData):
        self.Data = Data

    def generate_csv_report(self):
        raise NotImplementedError
