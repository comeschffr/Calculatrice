import tkinter as tk


class Calculatrice:
    def __init__(self, screenSize, widgNbColumn):
        
        self.screenSize = screenSize
        self.widgNbColumn = widgNbColumn
        self.widthSquare = 400 / self.widgNbColumn
        self.heightSquare = (650 - 150) / self.widgNbColumn
        self.expression = '' # str type for calculation

        self.root = tk.Tk() # Initialize window
        self.root.title('Calculatrice')
        self.root.geometry("400x650")

        self.root.bind('<Button-1>', self.clic) # Gets coords when clic
        self.root.bind('<Motion>', self.motion) # To change colors when moving mouse

        self.can = tk.Canvas(self.root, width=400, height=650, bg="white")
        self.can.pack()
                                                        # "#%02x%02x%02x", (58, 64, 69)
        self.can.create_rectangle(0, 0, 400, 150, fill='#282828') #screen
        self.pad = self.can.create_rectangle(0, 150, 400, 650, fill='#191919') #pad

        self.onScreen = self.can.create_text(370, 75, text=self.expression, anchor='e', fill='white', font='size 60') # Disp calculation on screen

        line1 = (' ' * 3) + '7' + (' ' * 7) + '8' + (' ' * 7) + '9' + (' ' * 7) + '*'
        line2 = (' ' * 3) + '4' + (' ' * 7) + '5' + (' ' * 7) + '6' + (' ' * 7) + '/'
        line3 = (' ' * 3) + '1' + (' ' * 7) + '2' + (' ' * 7) + '3' + (' ' * 7) + '+'
        line4 = (' ' * 3) + '0' + (' ' * 7) + ' . ' + (' ' * 7) + '=' + (' ' * 7) + '-'

        self.can.create_text(0, 225, text=line1, anchor='w', fill='white', font='size 50')
        self.can.create_text(0, 350, text=line2, anchor='w', fill='white', font='size 50')
        self.can.create_text(0, 475, text=line3, anchor='w', fill='white', font='size 50')
        self.can.create_text(0, 600, text=line4, anchor='w', fill='white', font='size 50')

        self.root.mainloop()


    def motion(event):
        pass


    def clic(self, event):
        clavier = [[0, '.', '=', '-'], [1, 2, 3, '+'], [4, 5, 6, '/'], [7, 8, 9, '*']]

        self.x, self.y = event.x, event.y
        ligne = self.widgNbColumn - 1 - int((self.y - self.screenSize) / self.heightSquare)
        colonne = int(self.x / self.widthSquare)
        
        element = str(clavier[ligne][colonne])
        
        if element != '=':
            self.add_to_expression(str(clavier[ligne][colonne]))
        else:
            self.result()


    def add_to_expression(self, char):
        if len(self.expression) < 10:
            self.expression += char
        self.can.itemconfig(self.onScreen, text=self.expression)


    def result(self):
        try:
            _result = eval(self.expression)
            if _result == int(_result):
                _result = int(_result)
            self.can.itemconfig(self.onScreen, text=_result)
            self.expression = str(_result)
        except SyntaxError:
            self.can.itemconfig(self.onScreen, text='Error')
            self.expression = ''


calc1 = Calculatrice(150, 4)
