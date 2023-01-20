#10.8
class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    def setter(self,input_name):
        self.__name=input_name
    def getter(self):
        print(self.__name)
hydrogen=Element('Hydrogen','H','1')

hydrogen.getter()
hydrogen.setter('Argon')
hydrogen.getter()





