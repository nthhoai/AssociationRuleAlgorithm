
class clinical_features_patient:

    clinical_features_patient = []
    #def __init__(self,Age,Anaemia,Creatinine_phosphokinase,Diabetes,Ejection_fraction,
    #             High_blood_pressure,Platelets,Serum_creatinine,Serum_sodium,Sex,Smoking,Time):
    #    self.age = Age
    #    self.anaemia = Anaemia 
    #    self.creatinnine_phosphokinase = Creatinine_phosphokinase
    #    self.diabetes = Diabetes
    #    self.ejection_fraction = Ejection_fraction
    #    self.high_blood_pressure = High_blood_pressure
    #    self.platelets = Platelets
    #    self.serum_creatinine = Serum_creatinine
    #    self.serum_sodium = Serum_sodium
    #    self.sex = Sex
    #    self.smoking = Smoking
    #    self.time = Time

    def __init__(self):
        pass

    def insert(self,Age,Anaemia,Creatinine_phosphokinase,Diabetes,Ejection_fraction,
                 High_blood_pressure,Platelets,Serum_creatinine,Serum_sodium,Sex,Smoking,Time):
        self.age = Age
        self.anaemia = Anaemia 
        self.creatinnine_phosphokinase = Creatinine_phosphokinase
        self.diabetes = Diabetes
        self.ejection_fraction = Ejection_fraction
        self.high_blood_pressure = High_blood_pressure
        self.platelets = Platelets
        self.serum_creatinine = Serum_creatinine
        self.serum_sodium = Serum_sodium
        self.sex = Sex
        self.smoking = Smoking
        self.time = Time
    #getter
    def get_age(self):
        return self.age
    def get_anaemia(self):
        return self.anaemia
    def get_creatinnine_phosphokinase(self):
        self.creatinnine_phosphokinase
    def get_diabetes(self):
        return self.diabetes
    def get_ejection_fraction(self):
        return self.ejection_fraction
    def get_high_blood_pressure(self):
        return self.high_blood_pressure
    def get_platelets(self):
        return self.platelets
    def get_serum_creatinine(self):
        return self.serum_creatinine
    def get_serum_sodium(self):
        return self.serum_sodium
    def get_sex(self):
        return self.sex
    def get_smoking(self):
        return self.smoking
    def get_time(self):
        return self.time


    #setter
    def set_age(self, Age):
        self.age = Age
    def set_anaemia(self, Anaemia):
        self.anaemia = Anaemia
    def set_creatinnine_phosphokinase(self, Creatinnine_phosphokinase):
        self.creatinnine_phosphokinase = Creatinnine_phosphokinase
    def set_diabetes(self, Diabetes):
        self.diabetes = Diabetes
    def set_ejection_fraction(self, Ejection_fraction):
        self.ejection_fraction = Ejection_fraction
    def set_high_blood_pressure(self, High_blood_pressure):
        self.high_blood_pressure = High_blood_pressure
    def set_platelets(self, Platelets):
        self.platelets = Platelets
    def set_serum_creatinine(self, Serum_creatinine):
        self.serum_creatinine = Serum_creatinine
    def set_serum_sodium(self, Serum_sodium):
        self.serum_sodium = Serum_sodium
    def set_sex(self, Sex):
        self.sex = Sex
    def set_smoking(self, Smoking):
        elf.smoking = Smoking
    def set_time(self, Time):
        self.time = Time
