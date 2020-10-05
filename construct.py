#!/bin/python3

# Constructs are used as resources in CDK
class Fruits:
    def __init__(self,name,count):
        self.name=name
        self.count=count
    def showFruits(self):
        print('Fruit name is {} and count is {}'.format(self.name,self.count))

apple=Fruits("Apple",2)
orange=Fruits("Orange",3)

apple.showFruits()
orange.showFruits()
