class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,ob):
        return Complex(self.real+ob.real,self.imag+ob.imag)
    def __sub__(self,other):
        return Complex(self.real-other.real,self.imag-other.imag)
    def __str__(self):
        return str(self.real)+"i + "+str(self.imag)+"j"
z1=Complex(5,7)
z2=Complex(3,8)
result=z1+z2
print(result.real)
print(result.imag)
print(result)
result=z1-z2
print(result.real)
print(result.imag)
print(result)
