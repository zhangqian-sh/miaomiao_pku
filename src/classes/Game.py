from random import random
from functions import DataBaseIO


class Game():
    def __init__(self, campus, cats, daily_consumption=50):
        self.m_time = 0
        self.m_daily_consumption_expect = daily_consumption
        self.m_daily_consumption = daily_consumption
        self.m_campus = campus
        self.m_cats = cats
        # Saving Information
        self.m_save_path = "savings/savings.db"

    def load_Saving(self, campus, cats):
        self.m_time = DataBaseIO.read_Database(self.m_save_path, "GAME", 1, "TIME")
        self.m_daily_consumption_expect = DataBaseIO.read_Database(self.m_save_path, "GAME", 1,
                                                                   "DAILY_CONSUMPTION_EXPECT")
        self.m_daily_consumption = DataBaseIO.read_Database(self.m_save_path, "GAME", 1, "DAILY_CONSUMPTION")
        self.m_campus = campus
        self.m_cats = cats

    def save_Saving(self):
        DataBaseIO.update_Database(self.m_save_path, "GAME", 1, "TIME", self.m_time)
        DataBaseIO.update_Database(self.m_save_path, "GAME", 1, "DAILY_CONSUMPTION_EXPECT",
                                   self.m_daily_consumption_expect)
        DataBaseIO.update_Database(self.m_save_path, "GAME", 1, "DAILY_CONSUMPTION", self.m_daily_consumption)
        self.m_campus.save_Saving()
        for i in range(len(self.m_cats)):
            DataBaseIO.update_Database(self.m_save_path, "CAT", i + 1, "IS_ALIVE", self.m_cats[i].m_is_alive)
            DataBaseIO.update_Database(self.m_save_path, "CAT", i + 1, "FRIENDLY_CONST",
                                       self.m_cats[i].m_friendly_const)
            DataBaseIO.update_Database(self.m_save_path, "CAT", i + 1, "CONSUMPTION", self.m_cats[i].m_consumption)
            DataBaseIO.update_Database(self.m_save_path, "CAT", i + 1, "APPEARED_YESTERDAY",
                                       self.m_cats[i].m_appeared_yesterday)

    def food_Decrease(self):
        self.m_daily_consumption = self.m_daily_consumption_expect * (0.95 + 0.15 * random())
        self.m_campus.food_Decrease(self.m_daily_consumption)

    def get_Alive_Cats(self):
        cats = self.m_cats
        alive_num = 0
        alive_list = []
        L = len(cats)
        for i in range(L):
            if cats[i].m_is_alive == True:
                alive_num += 1
                alive_list.append(cats[i].m_name)
        self.m_campus.m_alive_cats_num = alive_num
        self.m_campus.m_alive_list = alive_list

    def find_Appeared_Cats(self):
        cats = self.m_cats
        L = len(cats)
        for i in range(L):
            if cats[i].m_is_alive == True and random() * 10 < cats[i].m_friendly_const * self.m_daily_consumption / 50:
                cats[i].m_appeared_yesterday = True
            else:
                cats[i].m_appeared_yesterday = False

    def get_Appeared_Cats_List(self):
        cats = self.m_cats
        appear_list = []
        L = len(cats)
        for i in range(L):
            if cats[i].m_appeared_yesterday:
                appear_list.append(cats[i].m_name)
        return appear_list

    def next_Round(self):
        self.food_Decrease()
        self.find_Appeared_Cats()
        self.m_time += 1
