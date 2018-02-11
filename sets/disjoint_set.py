'''
Author: Zhenyi Qi

'''

class disjointSet(object):

    def __init__(self):
        self.sets = []


    def make_set(self, first_ele):
        self.sets.append([first_ele])


    def union(self, ele1, ele2):
        for index, set in enumerate(self.sets):
            if ele1 in set:
                set1 = set
                index1 = index
            if ele2 in set:
                set2 = set

        self.sets.remove(set2)
        self.sets[index1] = set1 + set2

    def find_set(self, ele):
        for set in self.sets:
            if ele in set:
                return set[0]

        return None

    