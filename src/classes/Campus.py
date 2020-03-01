import pandas as pd


class Campus():
    def __init__(self, cats):
        self.m_food = 10000
        self.m_alive_cats_num = len(cats)
        self.m_alive_list = []

        # Saving Information
        self.m_save_path = "savings/"
        self.m_campus_saving = pd.read_csv(self.m_save_path + "campus_saving.csv", sep=",", engine="python",
                                           encoding="utf-8")

    def load_Saving(self, cats):
        self.m_campus_saving = pd.read_csv(self.m_save_path + "campus_saving.csv", sep=",", engine="python",
                                           encoding="utf-8")
        self.m_food = self.m_campus_saving[u"food"][0]
        self.m_alive_cats_num = len(cats)
        self.m_alive_list = []

    def save_Saving(self):
        self.m_campus_saving.at[0, u"food"] = self.m_food
        self.m_campus_saving.to_csv(self.m_save_path + "campus_saving.csv", index=False)

    def food_Decrease(self, consumption):
        self.m_food -= consumption
