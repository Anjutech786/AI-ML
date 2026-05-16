from MachineLearning.Model.InsuranceModel import InsuranceData


class Data:
    @staticmethod
    def GetLinearInsuranceData():
        return [
            InsuranceData(18, 2000),
            InsuranceData(19, 500),
            InsuranceData(20, 4000),
            InsuranceData(21, 5000),
            InsuranceData(22, 300),
            InsuranceData(23, 7000),
            InsuranceData(24, 8000),
            InsuranceData(25, 9000),
            InsuranceData(26, 10000),
            InsuranceData(27, 11000)
        ]