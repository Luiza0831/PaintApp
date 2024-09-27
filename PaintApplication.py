from tkinter import * # type: ignore
from tkinter import colorchooser,ttk,messagebox,filedialog
from PIL import ImageGrab
import os

class Paint():

    def __init__(self,window,savedir):
        self.win=window
        self.savedir=savedir
        self.ColorFG='Black'
        self.ColorBG='White'
        self.PenWidth=5
        self.fullscreen=True
        self.OldX=None
        self.OldY=None
        self.widgets()
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def paint(self,e):
        if self.OldX and self.OldY:
            self.canvas.create_line(self.OldX,self.OldY,e.x,e.y,width=self.PenWidth,fill=self.ColorFG,capstyle='round',smooth=True)
        self.OldX=e.x
        self.OldY=e.y

    def reset(self,e):
        self.OldX=None
        self.OldY=None

    def change_fg(self):
        self.ColorFG=colorchooser.askcolor(color=self.ColorFG)[1]

    def change_bg(self):
        self.ColorBG=colorchooser.askcolor(color=self.ColorBG)[1]
        self.canvas['bg']=self.ColorBG

    def changed_w(self,width):
        self.PenWidth=width

    def clicked(self):
        self.slider.destroy()
        self.newbutton=Button(self.win,text='>',command=self.change_width,width=1,height=1,
                    activebackground='pink',activeforeground='dark red'
                    ,bg='lightpink1',fg='IndianRed4',font='System',relief='ridge')
        self.newbutton.pack()
        self.newbutton.place(x=70,y=120)
        self.button.destroy()

    def change_width(self):
        self.slider=ttk.Scale(from_=5, to=100, command=self.changed_w, orient='horizontal')
        self.slider.set(self.PenWidth)
        self.slider.grid(row=0, column=1)
        self.slider.place(x=70,y=122)
        self.button=Button(self.win,text='<',command=self.clicked,width=1,height=1,
                    activebackground='pink',activeforeground='dark red'
                    ,bg='lightpink1',fg='IndianRed4',font='System',relief='ridge')
        self.button.pack()
        self.button.place(x=175,y=122)
        try:
            self.newbutton.destroy()
        except AttributeError:
            pass
    
    def screenshot(self):
        if not os.path.exists(self.savedir):
            os.makedirs(self.savedir)
        fileName=filedialog.asksaveasfilename(initialdir=self.savedir,
                                              title="Select file",
                                              filetypes=(('PNG','*.png'),
                                                         ('PNG','*.png')))
        image=ImageGrab.grab(bbox=(253,53,1752,952))
        if '.png' not in fileName:
            if '.jpg' not in fileName:
                fileName=fileName+'.png'
        image.save(fileName)

    def save(self):
        if not self.fullscreen:
            self.fullscreen_mode()
            self.screenshot()
            self.fullscreen_mode()
        else:
            self.screenshot()

    def quit(self):
        response=messagebox.askquestion('Quitting!','Are you sure you want to quit?')
        if response=='yes':
            self.win.destroy()
        else:
            pass

    def fullscreen_mode(self):
        self.fullscreen=not self.fullscreen
        self.win.attributes('-fullscreen',self.fullscreen)

    def widgets(self):
        self.win.attributes('-fullscreen',self.fullscreen)
        self.win.configure(background='MistyRose')
        self.win.geometry('1500x800')
        buttons=[]
        for i in range(6):
            button=Button(self.win,text='',command='',width=1,height=1,
                    activebackground='AntiqueWhite1',activeforeground='HotPink4'
                    ,bg='lightpink1',fg='IndianRed4',font='System',relief='ridge')
            buttons.append(button)
        
        buttons[0].config(text='Quit',command=self.quit,width=3,height=1)
        buttons[1].config(text='Save',command=self.save,width=4,height=1)
        buttons[2].config(text='Fullscreen',command=self.fullscreen_mode,width=8,height=1)
        buttons[3].config(text='Pen color',command=self.change_fg,width=7,height=1)
        buttons[4].config(text='Pen width',command=self.change_width,width=7,height=1)
        buttons[5].config(text='BG color',command=self.change_bg,width=7,height=1)
    
        n=0
        for button in buttons:
            button.pack()
            button.place(x=0,y=n)
            n+=30
        self.canvas=Canvas(self.win,width=1200,height=720,bg=self.ColorBG,cursor='dotbox')
        self.canvas.pack()
        self.canvas.place(x=200,y=40)