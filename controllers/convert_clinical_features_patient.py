import numpy as np 

import sys 
sys.path.append("mvc_alogrithm")
from views import clinical_features_patient as vcfp
from models import clinical_features_patient as mcfp
import os


mcfp = mcfp.clinical_features_patient()
vcfp = vcfp.view_clinical_features_patient()


class convert_clinical_feature_patient:
    convert_dataInput = vcfp.get_data()

    def __init__(self):
        pass
    def convert_age(self):
        if self.convert_dataInput[0] > 90:
            self.convert_dataInput[0] = "T5"
        elif self.convert_dataInput[0] >80:
            self.convert_dataInput[0] = "T4"
        elif self.convert_dataInput[0] > 70:
            self.convert_dataInput[0] = "T3"
        elif self.convert_dataInput[0] > 60:
            self.convert_dataInput[0] = "T2"
        else:
            self.convert_dataInput[0] = "T1"
    

    def convert_anaemia(self):
        if self.convert_dataInput[1] == "Có":
            self.convert_dataInput[1] = "M1"
        if self.convert_dataInput[1] == "Không":
            self.convert_dataInput[1] = "M0"


    def convert_creatine_phosphokinase (self):
        if self.convert_dataInput[2] > 164:
            self.convert_dataInput[2] = "CP1"
        elif self.convert_dataInput[2] > 39: 
            self.convert_dataInput[2] = "CP0"
        else: 
            self.convert_dataInput[2] = "CP1"



    def convert_diaconvert_dataInputete (self):
        if self.convert_dataInput[3] == "Có":
            self.convert_dataInput[3] = "TD1"
        else:
            self.convert_dataInput[3] = "TD0"
        #self.convert_dataInput[3] = np.where(self.convert_dataInput[3] == "Không", 0, 1)


    def convert_ejection_fraction(self):
        if self.convert_dataInput[4] > 70:
            self.convert_dataInput[4] = "EF2"
        if self.convert_dataInput[4] > 50:
            self.convert_dataInput[4] = "EF1"
        if self.convert_dataInput[4] > 0:
            self.convert_dataInput[4] = "EF0"

    def convert_ha (self):
        if self.convert_dataInput[5] == "Có":
            self.convert_dataInput[5] = "HA1"
        if self.convert_dataInput[5] == "Không":
            self.convert_dataInput[5] = "HA0"

    def convert_thc(self):
        if self.convert_dataInput[6] > 400000:
            self.convert_dataInput[6] = "THC2"
        elif self.convert_dataInput[6] > 150000:
            self.convert_dataInput[6] = "THC1"
        else:
            self.convert_dataInput[6] = "THC0"

    def convert_serum_creatinine (self):
        if self.convert_dataInput[7] > 1.15:
            self.convert_dataInput[7] = "SC2"
        elif self.convert_dataInput[7] > 0.55:
            self.convert_dataInput[7] = "SC1"
        else:
            self.convert_dataInput[7] = "SC0"

    def convert_serum_sodium (self):
        if self.convert_dataInput[8] > 147:
            self.convert_dataInput[8] = "SS2"
        if self.convert_dataInput[8] > 135:
            self.convert_dataInput[8] = "SS1"
        if self.convert_dataInput[8] > 0:
            self.convert_dataInput[8] = "SS0"

    def convert_sex(self):
        if self.convert_dataInput[9] == "Nam":
            self.convert_dataInput[9] = 'GT0'
        if self.convert_dataInput[9] == "Nữ":
            self.convert_dataInput[9] = 'GT1'


    def convert_smoking (self):
        if self.convert_dataInput[10] == "Có":
            self.convert_dataInput[10] = "SM1"
        if self.convert_dataInput[10]  == "Không":
            self.convert_dataInput[10]  = "SM0"

    def convert_sl (self):
        if self.convert_dataInput[11] < 50:
            self.convert_dataInput[11] = "SL1"
        else:
            self.convert_dataInput[11] = "SL2"

    def set_model(self):
        mcfp.insert(self.convert_dataInput[0], self.convert_dataInput[1],self.convert_dataInput[2],self.convert_dataInput[3],self.convert_dataInput[4],self.convert_dataInput[5],self.convert_dataInput[6],self.convert_dataInput[7],self.convert_dataInput[8],
                    self.convert_dataInput[9],self.convert_dataInput[10],self.convert_dataInput[11])

    def get_convert_data(self):
        return self.convert_dataInput

if __name__ == "__main__":
    c = convert_clinical_feature_patient()
    c.convert_age()
    c.convert_anaemia()
    c.convert_creatine_phosphokinase()
    c.convert_diaconvert_dataInputete()
    c.convert_ejection_fraction()
    c.convert_ha()
    c.convert_serum_creatinine()
    c.convert_serum_sodium()
    c.convert_sex()
    c.convert_smoking()
    c.convert_sl()
    print (c.convert_dataInput)
    