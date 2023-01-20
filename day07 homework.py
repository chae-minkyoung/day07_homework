#10.4
import pprint
class Element():
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number

A=Element('Hydrogen','H','1')
pprint.pprint(vars(A))

