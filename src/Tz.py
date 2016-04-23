class Person():
    def __init__(self,name,gz):
        self.name = name
        self.gz = gz
    
    def print_info(self):
        print self.name , self.gz
    
    def zgz(self):
        self.gz = self.gz * 100;
    

p = Person("James",10)
p.print_info()
p.zgz()
p.print_info()





