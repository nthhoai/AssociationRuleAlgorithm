#import thư viện xử lý
import pandas as pd
import apyori 
from apyori import apriori 

class data_mining_association_rule:
    output = [] # tất cả luật 
    column_ordered_statistics = [] # cột 3
    dic_rule = [] # luật chứa đích
    def __init__(self, Path ):
        self.path = Path

    def handle_path(self):
        ''' Dùng thuật toán apriori để khai thác luật:
        + Đầu vào: danh sách record data
        + Đầu ra: list danh sách luật '''
        df = pd.read_csv(self.path)
        # Chuyển đổi dataframe - list
        records = []
        for i in range (0,299):
            records.append([str(df.values[i, j]) for j in range (0,13)])
        # thuật toán luật kết hợp
        alogrithm_association_rules = apriori (records, min_support=0.1, min_confidence= 0.5)
        self.output = pd.DataFrame(alogrithm_association_rules)
        return self.output 

    #lấy cột  3 - ordered_statistics:
    def alogrithm_get_ordered_statistics(self):
        ''' Get column Ordered_statistics 
        + Đầu vào: Danh sách luật (items_base, items_add, ordered_statistics)
        + Đầu ra: Danh sách record Ordered_statistics
        '''        
        for i in range (len (self.output)):
            a = self.output.loc[i, "ordered_statistics"]
            self.column_ordered_statistics.append(a)
        return self.column_ordered_statistics 


    # Tìm luật chứa đích là "DE1":
    def rule_DE1(self):
        ''' Xét điều kiện tìm luật có đích = "DE1":
        + Đầu vào: Danh sách record Ordered_statistics
        + Đầu ra: Danh sách luật thỏa mãn đích = "DE1"
        '''
        for i in range (len (self.column_ordered_statistics)):
            detail_column_ordered_statistics = self.column_ordered_statistics[i]
            for j in range (len (detail_column_ordered_statistics)):
                temp  = detail_column_ordered_statistics[j]
                #items_base = temp[0]
                items_add = temp[1]
                if items_add == {"DE1", }:
                    self.dic_rule.append(temp)
        
    #def df_rule(self):
    #    df_rule = pd.DataFrame(self.dic_rule)
    #    return df_rule 

    #thực hiện tuần tự: 
    def frequent(self):
        dmar = data_mining_association_rule("items.csv")
        dmar.handle_path()
        dmar.alogrithm_get_ordered_statistics()
        dmar.rule_DE1()
        #dmar.df_rule()
        df_rule = pd.DataFrame(self.dic_rule)
        return df_rule 




#if __name__ == '__main__':

