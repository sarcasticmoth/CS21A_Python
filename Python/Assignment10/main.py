

import tkinter
import myFrame    # the VIEW
import convert    # the MODEL

class Controller:
    """
    The Controller for an app that follows the Model/View/Controller architecture.
    When the user presses a Button on the View, this Controller calls the appropriate
    methods in the Model. The Controller handles all communication between the Model
    and the View.
    """
    def __init__(self):    
        """
        This starts the Tk framework up, instantiates the Model (a Convert object),
        instantiates the View (a MyFrame object), and starts the event loop that waits
        for the user to press a Button on the View.
        """
        root = tkinter.Tk()
        self.model = convert.Convert()
        self.view = myFrame.MyFrame(self)
        self.view.mainloop()
        root.destroy()
    
    def buttonPressed1(self):
        """
        Python calls this method when the user presses the convert in the View.
        """
        currentFahrenheit = self.view.F_txtbox.get()
        celcius = self.model.convertToCelcius(float(currentFahrenheit))
        self.view.C_resultLabel["text"] = str(celcius)


    def buttonPressed2(self):
        """
        this method is called when the user presses the convert in the View.
        """
        currentCelcius = self.view.C_txtbox.get()
        fahrenheit = self.model.convertToFahrenheit(float(currentCelcius))
        self.view.F_resultLabel["text"] = str(fahrenheit)

if __name__ == "__main__":
    c = Controller()
