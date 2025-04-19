class CurrencyConvert:
    exchange_rates = {
    'INR': 1.00,
    'USD': 0.011998,
    'EUR': 0.010936,
    'GBP': 0.009451,
    'AUD': 0.018112,
    'CAD': 0.016305,
    'SGD': 0.015984,
    'CHF': 0.010473,
    'MYR': 0.055819,
    'JPY': 1.765493,
    'CNY': 0.085270
}
    def __init__(self,value, unit='INR') -> None:
        self.value = value
        self.unit = unit
    def __str__(self) -> str:
        return f"{self.value:5.2f} {self.unit}"    

    def changeTo(self, new_unit):
        self.value = (self.value / CurrencyConvert.exchange_rates[self.unit] * CurrencyConvert.exchange_rates[new_unit])
        self.unit = new_unit
        # return f"Changed {self.value} {self.unit}"

    def __add__(self, other):
        
        if type(other) == int or type(other) == float:
            x = (other * CurrencyConvert.exchange_rates[self.unit])
            print(x)
        else:
            x = (other.value / CurrencyConvert.exchange_rates[other.unit])
            print(x)
            return CurrencyConvert(x + self.value, self.unit)
    
    def __iadd__(self, other):

        if type(other) == int or type(other) == float:
            x = (other * CurrencyConvert.exchange_rates[self.unit])
        else:
            x = (other.value / CurrencyConvert.exchange_rates[other.unit] * CurrencyConvert.exchange_rates[self.unit])
        self.value += x
        return self
        