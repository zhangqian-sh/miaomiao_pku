from random import random


class Game():
    def __init__(self, campus, cats, daily_consumption=50):
        self.m_time = 1
        self.m_campus = campus
        self.m_daily_consumption = daily_consumption

    def food_Decrease(self, daily_consumption):
        self.m_daily_consumption = daily_consumption * (0.95 + 0.15 * random())
        self.m_campus.food_Decrease(self.m_daily_consumption)

    def get_Alive_Cats(self, campus, cats):
        alive_num = 0
        alive_list = []
        L = len(cats)
        for i in range(L):
            if cats[i].m_is_alive == True:
                alive_num += 1
                alive_list.append(cats[i].m_name)

        campus.m_alive_cats_num = alive_num
        campus.m_alive_list = alive_list

    def get_Appeared_Cats(self, cats):
        appear_list=[]
        L = len(cats)
        for i in range(L):
            if cats[i].m_is_alive == True and random()*10<cats[i].m_friendly_const*self.m_daily_consumption/50:
                appear_list.append(cats[i].m_name)

        return appear_list
