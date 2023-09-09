import sys
sys.path.append("mvc_alogrithm")
from controllers import data_mining_association_rules as dmar
from controllers import convert_clinical_features_patient as ccfp

dmar = dmar.data_mining_association_rule("")

c = ccfp.convert_clinical_feature_patient()
c.convert_age()
c.convert_anaemia()
c.convert_creatine_phosphokinase()
c.convert_diaconvert_dataInputete()
c.convert_ejection_fraction()
c.convert_ha()
c.convert_thc()
c.convert_serum_creatinine()
c.convert_serum_sodium()
c.convert_sex()
c.convert_smoking()
c.convert_sl()
c.set_model()


class parttern:
    #input = dmar.df_rule()
    input = dmar.frequent()
    data = c.get_convert_data()
    #data = ["T3",'M0','CP0','TD0','EF0','HA1','THC1','SC2','SS0','GT1','SM0','SL1']

    rule1 = [] #???
    rules = [] #các luật có thể áp dụng
    rules_same_confidence = [] #các luật cùng conf


    def __init__(self):
        pass


    def find_number_rule(self, a, b): ##trả về số phần tử trùng với dữ liệu nhập vào
        ''' Kiểm tra xe có nhiều luật hợp với input hay không
            + đầu vào: Danh sách luật khai phá, datainput của người dùng
            + đầu ra: Số lượng tiền tố của các luật trùng '''
        count = 0
        for i in b:
            for j in a:
                if i == j:
                    count = count + 1
        if count != len (b):
            return -1
        return count


    def check_rule(self):
        ''' Kiểm tra số lượng luật trùng với dataInput
            + Đầu vào: dataInput người dùng nhập + kết quả find_number_rule: kiểm tra luật khớp với datainput
            + Đầu ra: Trường hợp xảy ra: 0 luật nào thảo mãn/ duy nhất 1 luật/ >= 2 luật
        '''
        count_rule = 0
        #input = r.rule_DE1()
        for i in range(len(self.input)):    
            # kết quả find_number_rule:
            a = self.find_number_rule(self.data, self.input["items_base"][i])
            if a != -1:
                count_rule = count_rule + 1
                self.rules.append(self.input.loc[i])
        if count_rule == 0:
            return 0
        elif count_rule == 1:
            return 1
        elif count_rule >= 2:
            return 2 

       
    def find_rule(self ):
        ''' Tìm luật tốt nhất:
            + Đầu vào: Số lượng luật thỏa mãn với dataInput
            + Đầu ra: Luật tốt nhất trong số đó
        '''
        #input = r.rule_DE1() #đầu vào: là đầu ra của hàm trả về số lượng 
        result_rule = self.check_rule() 
        if result_rule == 0:
            print ("Không thể phán đoán !")


        if result_rule == 1:
            for i in range(len(self.input)):    
                # kết quả find_number_rule:
                a = self.find_number_rule(self.data, self.input["items_base"][i])
                if a != -1:
                     print ("1")
                     return self.input.loc[i]
             #print (self.input.loc[i])


        if result_rule == 2:
            list_confidence_rule = []
            for i in range(len(self.rules)):
                list_confidence_rule.append(self.rules[i]['confidence'])
            
            # kiểm tra độ tin cậy của các luật thỏa mãn
            max_confidence_rule = max(list_confidence_rule)
            for i in range (len(self.rules)):
                if self.rules[i]['confidence'] == max_confidence_rule:
                    self.rules_same_confidence.append(self.rules[i])


            if len(self.rules_same_confidence) == 1:
                print ("2.1")
                return self.rules_same_confidence[0:]
            else:
                element = []
                #kiểm tra sô phần tử
                for i in range (len (self.rules_same_confidence)):
                    element.append(len(self.rules_same_confidence[i]["items_base"]))   
                                   
                max_element_rule = max(element)
                for i in range(len(self.rules_same_confidence)):         
                    if len (self.rules_same_confidence[i]["items_base"]) == max_element_rule:
                        print ("2.2")
                        #print (type(self.rules))
                        #print (self.rules[0]['confidence'])
                        #print (self.rules[0]['items_base'])
                        #print (list_confidence_rule)
                        #print (max_element_rule)
                        #print (max_confidence_rule)
                        return (self.rules_same_confidence[i])
                        #print (self.input.loc[i])


if __name__ == "__main__":    
    test = parttern()
    test.check_rule()
    print (test.find_rule())
    #print (test.data)

    print (test.input)
