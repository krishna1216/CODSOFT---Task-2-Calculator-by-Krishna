import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        self.expression = ""
        self.output = tk.StringVar()

        # Entry widget to display input and output
        self.entry = tk.Entry(root, textvariable=self.output, font=('Arial', 18), bd=5, insertwidth=4, width=25, justify='right')
        self.entry.grid(row=0, column=0, columnspan=6)

        # Buttons for numbers and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('^', 4, 4),
            ('(', 1, 5), (')', 2, 5), ('sqrt', 3, 5), ('clr', 4, 5)
        ]

        for button_text, row, col in buttons:
            tk.Button(root, text=button_text, width=5, font=('Arial', 14),
                      command=lambda text=button_text: self.action(text)).grid(row=row, column=col)

    def action(self, text):
        if text == '=':
            try:
                self.expression = self.entry.get()
                result = eval(self.expression)
                self.output.set(result)
            except:
                self.output.set("Error")
        elif text == 'clr':
            self.entry.delete(0, tk.END)
        elif text == 'sqrt':
            self.expression = self.entry.get()
            try:
                result = math.sqrt(eval(self.expression))
                self.output.set(result)
            except:
                self.output.set("Error")
        elif text == '^':
            self.expression = self.entry.get()
            try:
                result = eval(self.expression) ** 2
                self.output.set(result)
            except:
                self.output.set("Error")
        elif text in ['sin', 'cos', 'tan']:
            func_map = {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan
            }
            self.expression = self.entry.get()
            try:
                # Assuming input is in degrees, convert to radians
                if text == 'sin':
                    result = func_map['sin'](math.radians(eval(self.expression)))
                elif text == 'cos':
                    result = func_map['cos'](math.radians(eval(self.expression)))
                elif text == 'tan':
                    result = func_map['tan'](math.radians(eval(self.expression)))
                self.output.set(result)
            except:
                self.output.set("Error")
        else:
            self.entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
calculator = ScientificCalculator(root)
root.mainloop()
