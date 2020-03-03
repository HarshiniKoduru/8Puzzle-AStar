# -*- coding: utf-8 -*-

#Definitions for operations on the Priority Queue Class
from operator import itemgetter
class Priority_Queue():
    def __init__(self):
            self.elements = []
            self.max_elements = 0
    def insert_element(self, item, h=0, g=0, priority=0,move='initial'):
            self.elements.append((priority, h, g, item, move))
            self.elements.sort(key=itemgetter(0))
    def get_child(self):
            return self.elements.pop(0)
    def get_rem_elements(self):
            return len(self.elements)
    def empty(self):
            return len(self.elements) == 0