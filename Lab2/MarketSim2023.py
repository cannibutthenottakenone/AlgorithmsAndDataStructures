#sorry for the lack of comments :( 

import sys, os
sys.path.append(os.path.join(sys.path[0], "..", "modules"))

from typing import Any
from LinearStructures import Queue
from random import randint

MAX_NUMBER=250
CUSTOMERS_NUMBER = 50000
DESKS_NUMBER = 85

class Customer:
    def __init__(self, id: int, numItems: int):
        if numItems>MAX_NUMBER:
            raise Exception("too many items in Customer's basket")
        
        self.id=id
        self.numItems=numItems

    def __str__(self):
        return "Customer %s, itemsLeft %s" % (self.id, self.numItems)


class Desk:
    currentCust=None
    servedCusts=0

    def __init__(self, id: int, waitingCusts=Queue()):
        self.id=id
        self.waitingCusts=waitingCusts

    def iterate(self):
        if self.currentCust==None:
            if self.waitingCusts.size!=0:
                self.currentCust=self.waitingCusts.dequeue()
            else:
                return
            
        else:
            if self.currentCust.numItems>0:
                self.currentCust.numItems-=1
            else:
                print("Check desk %s, served customer %s" % (self.id, self.currentCust.id))
                self.servedCusts+=1
                self.currentCust=self.waitingCusts.dequeue()

    def addCustomer(self, cust: Customer):
        self.waitingCusts.enqueue(cust)

outsideCustomers = [ Customer(i, randint(0, MAX_NUMBER)) for i in range(CUSTOMERS_NUMBER) ]
outsideCustomers.reverse()
desks = [ Desk(i) for i in range(DESKS_NUMBER) ]

while len(outsideCustomers)!=0 or not all(d.waitingCusts.isEmpty() for d in desks) or not all(d.currentCust==None for d in desks):
    if randint(1, 10)<4 and len(outsideCustomers)>0: #30% of times
        #select desk with less people
        desk=desks[0]
        if desk.currentCust!=None:
            for i in range(1,len(desks)):
                if desks[i].currentCust==None:
                    desk=desks[i]
                    break

                if desks[i].waitingCusts.size()<desk.waitingCusts.size():
                    desk=desks[i]
        
        #add cutomer from list to selected desk
        desk.addCustomer(outsideCustomers.pop())
    
    for d in desks:
        d.iterate()

print("finished!")
for d in desks:
    print("desk %s, customers served %s" % (d.id, d.servedCusts))
