from functions import DataBaseIO


class Campus():
    def __init__(self, cats):
        self.m_food = 10000
        self.m_alive_cats_num = len(cats)
        self.m_alive_list = []
        # Saving Information
        self.m_save_path = "savings/savings.db"

    def load_Saving(self,cats):
        self.m_food=DataBaseIO.read_Database(self.m_save_path,"CAMPUS",1,"FOOD")
        self.m_alive_cats_num = len(cats)
        self.m_alive_list = []

    def save_Saving(self):
        DataBaseIO.update_Database(self.m_save_path,"CAMPUS",1,"FOOD",self.m_food)

    def food_Decrease(self, consumption):
        self.m_food -= consumption
