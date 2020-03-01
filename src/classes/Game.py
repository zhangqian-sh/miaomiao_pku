from random import random

import pandas as pd


class Game():
    def __init__(self, campus, cats, daily_consumption=50):
        self.m_time = 0
        self.m_daily_consumption_expect = daily_consumption
        self.m_daily_consumption = daily_consumption
        self.m_campus = campus
        self.m_cats = cats

        # Saving Information
        self.m_save_path = "savings/"
        self.m_game_saving = pd.read_csv(self.m_save_path + "game_saving.csv", sep=",", engine="python",
                                         encoding="utf-8")
        self.m_cats_saving = pd.read_csv(self.m_save_path + "cat_data.csv", sep=",", engine="python", encoding="utf-8")

    def load_Saving(self, campus, cats):
        self.m_game_saving = pd.read_csv(self.m_save_path + "game_saving.csv", sep=",", engine="python",
                                         encoding="utf-8")
        self.m_time = self.m_game_saving[u"time"][0]
        self.m_daily_consumption_expect = self.m_game_saving[u"daily_consumption_expect"][0]
        self.m_daily_consumption = self.m_game_saving[u"daily_consumption"][0]
        self.m_campus = campus
        self.m_cats = cats

    def save_Saving(self):
        # Save game info
        self.m_game_saving.at[0, u"time"] = self.m_time
        self.m_game_saving.at[0, u"daily_consumption_expect"] = self.m_daily_consumption_expect
        self.m_game_saving.at[0, u"daily_consumption"] = self.m_daily_consumption
        self.m_game_saving.to_csv(self.m_save_path + "game_saving.csv", index=False)
        # Save campus info
        self.m_campus.save_Saving()
        # Save cats info
        for i in range(len(self.m_cats)):
            self.m_cats_saving.at[i, u"Friendly_const"] = self.m_cats[i].m_friendly_const
            self.m_cats_saving.at[i, u"Consumption"] = self.m_cats[i].m_consumption
            self.m_cats_saving.at[i, u"Is_alive"] = self.m_cats[i].m_is_alive
        self.m_cats_saving.to_csv(self.m_save_path + "cat_data.csv", index=False)

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

    def get_Appeared_Cats(self):
        cats = self.m_cats
        appear_list = []
        L = len(cats)
        for i in range(L):
            if cats[i].m_is_alive == True and random() * 10 < cats[i].m_friendly_const * self.m_daily_consumption / 50:
                appear_list.append(cats[i].m_name)
        return appear_list

    def next_Round(self):
        self.food_Decrease()
        self.m_time += 1

