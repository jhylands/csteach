from _abcoll import ItemsView

class item:
    def __init__(self, name, description, barcode, pricePerUnit, quantity, VAT):
        self.name = name
        self.description = description
        self.barcode = barcode
        self.pricePerUnit = pricePerUnit
        self.quantity = quantity
        self.VAT = VAT
        
    def __str__(self):
        print "'Name: " + self.name
        print "Description: " + self.description
        print "Barcode" + self.barcode
        print "Price per unit" +  self.pricePerUnit
        print "Quantity" + self.quantity
        print "VAT@" + self.VAT
        
        
class Electronic(item):
    def __init__(self,Brand,YearsOfWarrenty):
        self.Brand = Brand
        self.YearsOfWarrenty = YearsOfWarrenty
        
    def __str__(self):
        print "Brand:" + self.Brand 
        print "Years of warrenty" + str(self.YearsOfWarrenty)
class Cloathing(item):
    def __init__(self, size,childCloathing):
        self.size = size
        self.childCloathing = childCloathing
        
    def __str__(self):
        if self.childCloathing:
            print "Age: " + self.size
        else:
            print "Size" + self.size
    
class basket:
    def __init__(self):
        self.items = []
        
    def additem(self,anItem):
        self.items.append(anItem)
    
    def removeItem(self,itemR):
        self.items.remove(itemR)
        
    def totalPrice(self):
        total = 0
        for item in self.items:
            total += item.pricePerUnit*item.quantity
        return total

items = [item("A","B",00,1,1,0.2),item("B","B",00,1,1,0.2),item("A","B",00,1,1,0.2)]
         
myBasket = basket()
for anItem in items:
    myBasket.additem(anItem)

myBasket.removeItem(items[0])
print len(myBasket.items)
         
