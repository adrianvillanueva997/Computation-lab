import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalcGridLayout(GridLayout):

    # llamada a la funcion cuando el igual es presionado
    def calculate(self, calculation):
        if calculation:
            try:
                # resuelve la formula y muestra el entry
                # el cual hace referencia al display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()