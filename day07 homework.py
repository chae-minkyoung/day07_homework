#10.5
el_dict={'name':'Hydrogen','symbol':'H','number':'1'}
el_di21ct={'symbol':'H','number':'1','name':'Hydrogen'}
class Element():
    def __init__(self,other):
        self.name=other["name"]
        self.symbol=other["symbol"]
        self.number=other["number"]
hydrogen=Element(el_dict)
print(vars(hydrogen))



