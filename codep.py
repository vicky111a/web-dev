class flight():
    def __init__(self,count):
        self.tseats=count
        self.passengers=[]
    def add(self,name):
        self.passengers.append(name)
    def available(self):
        if (self.tseats-len(self.passengers))>0:
            return True
        return False
a=flight(4)
n=list(input("enter passengers list").split())
c=True
for i in n:
    if a.available():
        a.add(i)
        print(f"ticket for {i} is booked")
    else:
        print(f"cant book ticket for {i}")