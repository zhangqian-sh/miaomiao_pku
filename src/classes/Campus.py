class Campus():
    def __init__(self, cats):
        self.m_food = 10000
        self.m_alive_cats_num = len(cats)
        self.m_alive_list = []

    def food_Decrease(self, consumption):
        self.m_food -= consumption
