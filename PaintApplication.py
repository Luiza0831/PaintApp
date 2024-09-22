from tkinter import * # type: ignore

class Paint():

    def __init__(self,window):
        self.win=window
        self.ColorFG='Black'
        self.ColorBG='White'
        self.PenWidth=5
        self.widgets()

    def paint(self):
        pass

    def change_fg(self):
        pass

    def change_bg(self):
        pass

    def change_width(self):
        pass

    def save(self):
        pass

    def quit(self):
        pass

    def widgets(self):
        self.win.configure(background='MistyRose')
        self.win.geometry('1080x720')
        buttons=[]
        for i in range(5):
            button=Button(self.win,text='',command='',width=1,height=1,
                    activebackground='AntiqueWhite1',activeforeground='HotPink4'
                    ,bg='lightpink1',fg='IndianRed4',font='System',relief='ridge')
            buttons.append(button)
        
        buttons[0].config(text='Quit',command=self.quit,width=3,height=1)
        buttons[1].config(text='Save',command=self.save,width=4,height=1)
        buttons[2].config(text='Pen color',command=self.change_fg,width=7,height=1)
        buttons[3].config(text='Pen width',command=self.change_width,width=7,height=1)
        buttons[4].config(text='BG color',command=self.change_bg,width=7,height=1)
    
        n=0
        for button in buttons:
            button.pack()
            button.place(x=0,y=n)
            n+=30
        self.canvas=Canvas(self.win,width=700,height=700,bg=self.ColorBG,cursor='dotbox')
        self.canvas.pack()
        self.canvas.place(x=200,y=0)