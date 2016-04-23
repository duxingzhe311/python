class Info:
    id = ""
    name = ""
    address = ""
    price = ""
    phone = ""
    time = ""
    
    def setId(self,n):
        self.id = n
        return self
    
    def setName(self,n):
        self.name = n;
        return self
    
    def setAddress(self,n):
        self.address = n;
        return self
    
    def setPrice(self,n):
        self.price = n
        return self
    
    def setPhone(self,n):
        self.phone = n
        return self
    
    def setTime(self,n):
        self.time = n
        return self
    
    def toString(self):
        return "id=" + self.id + ",name=" + self.name + ",address=" + self.address + ",price=" + self.price + ",phone=" + self.phone + ",time=" + self.time
