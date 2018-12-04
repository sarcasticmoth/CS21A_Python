
class Convert:
    """
    class Convert is the model for a simple program that converts temperature
    values from Celcius to Fahrenheit and from Fahrenheit to Celsius
    """
    def __init__(self):
        self.fahrenheit = 0
        self.celcius = 0

    def convertToCelcius(self, fahrenheit):
        self.celcius = float((fahrenheit - 32)) * (5/9)
        return self.celcius

    def convertToFahrenheit(self, celcius):
        self.fahrenheit = float((celcius * (9/5))) + 32
        return self.fahrenheit
