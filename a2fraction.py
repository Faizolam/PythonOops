class Fraction:
    def __init__(self, n, d) -> None:
        self.num = n
        self.den = d

    def __str__(self) -> str:
        # return "Hello"
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,other): #It is a binary operator and it's need 2 object to operate so 1st object will get x and 2nd object will get y(below is detailed explaination) 

        temp_num=self.num*other.den + other.num*self.den
        temp_den=self.den*other.den

        return "{}/{}".format(temp_num,temp_den)
    
    def __sub__(self,other):

        temp_num=self.num*other.den - other.num*self.den
        temp_den=self.den*other.den

        return "{}/{}".format(temp_num,temp_den)
    
    def __mul__(self,other):

        temp_num=self.num*other.num 
        temp_den=self.den*other.den

        return "{}/{}".format(temp_num,temp_den)
    
    def __truediv__(self,other):

        temp_num=self.num*other.num
        temp_den=self.den*other.den

        return "{}/{}".format(temp_num,temp_den)
    

#? Note:

# >>from fraction import Fraction
# >>x = Fraction(4,5)
# >>print(x)
# >>4/5

# >>y = Fraction(5,6)
# >>print(y)
# >>5/6

# >>print(x+y)
# >>TypeError:unsupported operand type(s) for +: 'Fraction' and 'Fraction'

#* Here you did not tell how will your 2 object will 

# >>S1={1,2,3}
# >>S2={4,5,6}

# >>print(S1+S2)
# >>TypeError:unsupported operand type(s) for +: 'set' and 'set'

#* matlab jisne v set ka class banaya usne ye logic nhi likha ki 2 sets ko kaise add krte hai

#* So what if i have to add my 2 Fraction object, and for this we use __add__() magic method.
# it will automatically trigger whenever we type 
# >>print(x+y)