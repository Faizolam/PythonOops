class Ccy:
    currencies =  {'CHF': 1.0821202355817312, 
                       'CAD': 1.488609845538393, 
                       'GBP': 0.8916546282920325, 
                       'JPY': 114.38826536281809, 
                       'FAZA':2,
                       'EUR': 1.0, 
                       'USD': 1.11123458162018}
    def __init__(self, value, unit="EUR"):
        self.value = value
        self.unit = unit
    def __str__(self):
        return "{0:5.2f}".format(self.value) + " " + self.unit
    
    def changeTo(self, new_unit):
        """
            An Ccy object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Ccy.currencies[self.unit] * Ccy.currencies[new_unit])
        self.unit = new_unit
        return f'Changde {self.unit},{self.value}'
    
    def __add__(self, other):
        """
            Defines the '+' operator.
            If other is a CCy object the currency values 
            are added and the result will be the unit of 
            self. If other is an int or a float, other will
            be treated as a Euro value. 
        """
        if type(other) == int or type(other) == float:
                x = (other * Ccy.currencies[self.unit])
                print('O={other}, x={x}')
        else:
                x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit]) 
                print('O={other}, x={x}')
        return Ccy(x + self.value, self.unit)