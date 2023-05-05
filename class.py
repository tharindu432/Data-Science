#class
class Human:
    def __init__(self,n,occ):
        self.name= n
        self.occupation=occ

    def do_work(self):
        if self.occupation=="tennis player":
         print(self.name,"plays tennis")
        elif self.occupation=="actor":
         print(self.name,"shoot a film")

tom=Human("tom cruise","actor")
tom.do_work()






