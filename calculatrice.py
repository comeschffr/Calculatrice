import tkinter as tk


class Calculatrice:
    def __init__(self):
        # str type for calculus
        self.expression = ""

        self.root = tk.Tk() # Initialize the window
        self.root.title('Calculatrice')
        self.root.geometry("400x650")

        self.root.bind('<Button-1>', self.clic) # Get coords when clic

        self.can = tk.Canvas(self.root, width=400, height=650, bg="white")
        self.can.pack()

        self.can.create_rectangle(0, 0, 400, 150, fill='#6e668f') #screen
        self.pad = self.can.create_rectangle(0, 150, 400, 650, fill='#9fcadd') #pad

        self.onScreen = self.can.create_text(370, 75, text=self.expression, anchor='e', font='size 60')

        line1 = (' ' * 3) + '7' + (' ' * 7) + '8' + (' ' * 7) + '9' + (' ' * 7) + '*'
        line2 = (' ' * 3) + '4' + (' ' * 7) + '5' + (' ' * 7) + '6' + (' ' * 7) + '/'
        line3 = (' ' * 3) + '1' + (' ' * 7) + '2' + (' ' * 7) + '3' + (' ' * 7) + '+'
        line4 = (' ' * 3) + '=' + (' ' * 7) + '0' + (' ' * 7) + '.' + (' ' * 7) + '-'

        self.can.create_text(0, 225, text=line1, anchor='w', font='size 50')
        self.can.create_text(0, 350, text=line2, anchor='w', font='size 50')
        self.can.create_text(0, 475, text=line3, anchor='w', font='size 50')
        self.can.create_text(0, 600, text=line4, anchor='w', font='size 50')

        self.root.mainloop()

    def clic(self, event):
        self.x, self.y = event.x, event.y
        clavier = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        if 0 < self.x < 300 and 150 < self.y < 550:
            ligne = 2 - int((self.y - 150) / 133)
            colonne = int(self.x / 100)
            number = clavier[ligne][colonne]
            self.add_to_expression(str(number))
        elif 0 < self.x < 100:
            self.result()
        elif 100 < self.x < 200:
            self.add_to_expression('0')
        elif 200 < self.x < 300:
            self.add_to_expression('.')
        else:
            operations = ['*', '/', '+', '-']
            indice = int((self.y - 150) / 150)
            self.add_to_expression(operations[indice])

    def add_to_expression(self, char):
        self.expression += char
        self.can.itemconfig(self.onScreen, text=self.expression)

    def result(self):
        _result = eval(self.expression)
        if _result == int(_result):
            _result = int(_result)
        self.can.itemconfig(self.onScreen, text=_result)
        self.expression = str(_result)


calc1 = Calculatrice()
