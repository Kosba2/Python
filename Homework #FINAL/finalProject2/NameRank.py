# Homework No. FINAL  Exercise No.2
# File Name:     finalProject2.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement: Name-Rank Class which keeps the relationship between name frequency and rank


class NameRank:

    def __init__(self, rank, count):
        self.rank = rank
        self.count = count

    @property
    def Rank(self):
        return self.rank

    @property
    def Count(self):
        return self.count
