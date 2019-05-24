import tkinter as tk


class Calculatrice:
    def __init__(self, winWidth, winHeight, screenSize, widgNbColumn):
        
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.screenSize = screenSize
        self.widgNbColumn = widgNbColumn
        self.widthKey = self.winWidth / self.widgNbColumn # Single key width
        self.heightKey = (self.winHeight - self.screenSize) / self.widgNbColumn # Single key height
        self.expression = '' # str type for calculation

        self.root = tk.Tk() # Initialize window
        self.root.title('Calculatrice')
        self.root.geometry("{}x{}".format(winWidth, winHeight))

        self.root.bind('<Button-1>', self.clic) # Gets coords when clic
        self.root.bind('<Motion>', self.motion) # To change colors when moving mouse
        self.root.bind('<Key>', self.key)

        self.can = tk.Canvas(self.root, width=self.winWidth, height=self.winHeight, bg="white")
        self.can.pack()

        self.can.create_rectangle(0, 0, self.winWidth, self.screenSize, fill='#282828') #screen
        self.pad = self.can.create_rectangle(0, self.screenSize, self.winWidth, self.winHeight, fill='#191919') #pad

        self.onScreen = self.can.create_text(int(0.9 * self.winWidth), self.screenSize / 2, text=self.expression, anchor='e', fill='white', font=('System', 50)) # Disp calculation on screen

        self.clavier = [[0, '.', '=', '-'], [1, 2, 3, '+'], [4, 5, 6, '/'], [7, 8, 9, '*']]
       
        lines = [(' ' * 3) + '7' + (' ' * 7) + '8' + (' ' * 7) + '9' + (' ' * 7) + '*',
            (' ' * 3) + '4' + (' ' * 7) + '5' + (' ' * 7) + '6' + (' ' * 7) + '/',
            (' ' * 3) + '1' + (' ' * 7) + '2' + (' ' * 7) + '3' + (' ' * 7) + '+',
            (' ' * 3) + '0' + (' ' * 7) + ' . ' + (' ' * 7) + '=' + (' ' * 7) + '-']

        for i in range(self.widgNbColumn):
            self.can.create_text(0, (self.screenSize + self.heightKey / 2 + i * (self.heightKey)), text=lines[i], anchor='w', fill='white', font=('System', 50))

        self.root.mainloop()


    def motion(self, event):
        pass


    def key(self, event):
        chars = ['0', '.', '-', '1', '2', '3', '+', '4', '5', '6', '/', '7', '8', '9', '*']
        if event.char in chars:
            self.add_to_expression(event.char)
        elif event.keysym == 'Return':
            self.result()
        elif event.keysym in ['Escape', 'Tab']:
            self.clear_screen()


    def clic(self, event):
        ligne = self.widgNbColumn - 1 - int((event.y - self.screenSize) / self.heightKey)
        colonne = int(event.x / self.widthKey)
        
        if event.y > self.screenSize:
            element = str(self.clavier[ligne][colonne])
        else:
            element = ''
            self.clear_screen()

        if element == '=':
            self.result()
        else:
            self.add_to_expression(element)


    def add_to_expression(self, char):
        if len(self.expression) < 10:
            self.expression += char
        self.can.itemconfig(self.onScreen, text=self.expression)


    def clear_screen(self):
        self.expression = ''
        self.can.itemconfig(self.onScreen, text='')


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


calc1 = Calculatrice(400, 650, 150, 4)
