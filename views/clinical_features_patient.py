#dataInput = ["T3", "M0", "CP0", "TD0", "EF0", "HA1", "THC1", "SC2", "SS0", "GT1", "SM0", "SL1"]


class view_clinical_features_patient:
    dataInput = []

    def __init__(self):
        pass


    def get_data(self):
        Age = int (input ("Nhập tuổi: "))
        Anaemia = input ("Bạn có bị thiếu máu không: ")
        Cp = int (input ("Nhập chỉ số creatine phosphokinase: "))
        Diabete = input ("Bạn có bị tiểu đường không ?")
        Ef = int (input ("Nhập chỉ số phân suất tống máu (ejection_fraction)"))
        Ha = input ("Bạn có bị huyết áp cao không ?")
        Thc = int (input ("Nhập chỉ số tiểu huyết cầu: "))
        Sc = float (input ("Nhập chỉ số serum creatinine: "))
        Ss = int (input ("Nhập chỉ số natri huyết thanh (serum sodium): "))
        Sex = input ("Giới tính của bạn: ")
        Sm = input ("Bạn có hút thuốc không ?")
        Sl = int (input("Số lần bạn từng khám bệnh: "))
        #return self.insert(Age,Anaemia,Cp,Diabete,Ef,Ha,Thc,Sc,Ss,Sex,Sm,Sl)
        self.dataInput = [Age,Anaemia,Cp,Diabete,Ef,Ha,Thc,Sc,Ss,Sex,Sm,Sl]
        return self.dataInput

if __name__ == "__main__":
    a = view_clinical_features_patient()
    print (a.get_data())




