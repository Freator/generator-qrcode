class diaoyong:
    name=' '
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.weight=w
    def speak(self):
        print("%s说我今年%d岁体重为%d斤"%(self.name,self.age,self.weight))
x=diaoyong('dave',45,150)
x.speak()





