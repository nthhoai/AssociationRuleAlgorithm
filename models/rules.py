import sys
sys.path.append("mvc_alogrithm")
from controllers import data_mining_association_rules as dmar

dmar = dmar.data_mining_association_rule("")




class rules:
    rules = dmar.df_rule()

    def __init__ (self, Confidence, Items_base, Items_add = "DE1"):
        self.confidence = Confidence
        self.items_base = Items_base 
        self.items_add = Items_add


        