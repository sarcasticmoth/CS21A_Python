import tkinter

class MyFrame(tkinter.Frame):
    """
    class MyFrame is the View for a simple program that exemplifies the Model/View/Controller
    architecture. This View class is a tkinter.Frame that contains two Buttons and a Label. One Button
    notifies the Controller when it is pressed, and the other Button quits the app. The Label displays
    the current value of the counter. Notice that the View never contains a reference to the Model,
    but it does contain a reference to the Controller.
    """
    def __init__(self, controller):
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller    # saves a reference to the controller so that we can call methods
                                        # on the controller object when the user generates events

        self.divider1 = tkinter.LabelFrame(self, {"text" : "Fahrenheit To Celcius"})
        self.divider1.pack()

        self.F_txtbox = tkinter.Entry(self.divider1)
        self.F_txtbox.pack()

        self.convertToCButton = tkinter.Button(self.divider1)
        self.convertToCButton["text"] = "Convert"
        self.convertToCButton["command"] = self.controller.buttonPressed1
        self.convertToCButton.pack()

        self.C_resultLabel = tkinter.Label(self.divider1)
        self.C_resultLabel["text"] = ""
        self.C_resultLabel.pack()

        self.divider2 = tkinter.LabelFrame(self, {"text" : "Celcius to Fahrenheit"})
        self.divider2.pack()

        self.C_txtbox = tkinter.Entry(self.divider2)
        self.C_txtbox.pack()
        self.C_txtbox.pack()

        self.convertToFButton = tkinter.Button(self.divider2)
        self.convertToFButton["text"] = "Convert"
        self.convertToFButton["command"] = self.controller.buttonPressed2
        self.convertToFButton.pack()

        self.F_resultLabel = tkinter.Label(self.divider2)
        self.F_resultLabel["text"] = ""
        self.F_resultLabel.pack()

        self.divider3 = tkinter.LabelFrame(self, {"text" : ""})
        self.divider3.pack()

        self.quitButton = tkinter.Button(self.divider3)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack({"side" : "bottom"})



