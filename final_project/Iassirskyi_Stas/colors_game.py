import tkinter as tk
from tkinter import *
from random import choice
from tkinter import font
from my_bs_manager import BaseManager as my_manager
import os
import sys
import webbrowser


HEIGHT = 800
WIDTH = 800
base = 'score.db'


class Home_page(tk.Canvas):

    # HEIGHT = 800
    # WIDTH = 800
    #base = 'score.db'

    def __init__(self, main = None):
        super().__init__(main)
        self.main = main
        self.canvas = tk.Canvas(main, height=HEIGHT, width=WIDTH, bg='#276247', bd=5)
        self.canvas.pack()

        self.frame = tk.Frame(main, bg='white', bd=5)
        self.frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.1, anchor='n')

        self.hello_label = tk.Label(self.frame, text='Wellcome to a simple color game', fg='#283b32', font= ('Courier', 15))
        self.hello_label.pack(anchor='n')

        self.name_label = tk.Label(self.frame, text='Enter your name:', font=('Courier', 12))
        self.name_label.pack(side='left')

        self.name_enter = tk.Entry(self.frame)
        self.name_enter.pack(side='left')

        self.name_button = tk.Button(self.frame, text='Save', font=('Courier', 10), command= lambda: self.get_name(self.name_enter.get()))
        self.name_button.pack(side='left')

        self.test_button = tk.Button(self.frame, text='Start', font=('Courier', 10), command=lambda: MainGame(self.main))
        self.test_button.pack(side='left')

        self.restart_button = tk.Button(self.frame, text='Restrart', font=('Courier', 10), command=lambda: self.restart_game())
        self.restart_button.pack(side='left')

        self.score_button = tk.Button(self.frame, text='Leaderboard', font=('Courier', 10), command=lambda: webbrowser.open('http://127.0.0.1:5000/'))
        self.score_button.pack(side='left')


    def restart_game(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    
    def get_name(self, entry):
        sql = '''
            INSERT INTO leaderboard (Name)
            VALUES (?)
        '''
        with my_manager(base) as bm:
            bm.execute(sql, [entry])
            result = bm.fetchall()
        return result


class MainGame(Home_page):
    sql = '''
    UPDATE leaderboard
    SET questions = ?, correct = ?
    WHERE questions ISNULL and correct ISNULL  
    '''
    score = 0
    timeleft = 20
    atempt = 0
    colors = ['red', 'blue', 'white', 'green', 'yellow', 'orange', 'black', 'brown', 'purple', 'pink']


    def __init__(self, main):
        super().__init__(main)
        self.game_frame = tk.Frame(self.main, bg='white', bd=5)
        self.game_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.3, anchor='n')
        self.top_label = tk.Label(self.game_frame, text='Whrite a color of the word, not the word text\n Please Enter to start', font=('Courier',13))
        self.top_label.pack(side='top')
        
        self.score_label = tk.Label(self.game_frame, text='Score' + " " + str(self.score))
        self.score_label.pack(side='left', anchor='n')

        self.time_label = tk.Label(self.game_frame, text='Timeleft' + " " + str(self.timeleft))
        self.time_label.pack(side='left', anchor='n')

        self.show_colors = tk.Label(self.game_frame, font=('Courier', 25))
        self.show_colors.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.3)
        #self.show_colors.pack(side='top') 


        self.user_answer = tk.Entry(self.game_frame, font=24)
        #self.user_answer.pack(side='left', anchor='s')
        self.user_answer.place(relx=0.35, rely=0.55)
        self.user_answer.focus_set()

        self.main.bind('<Return>', self.startgame)


    def check_answer(self):

        if self.timeleft > 0:
            self.atempt += 1

            answer = self.user_answer.get()
            if answer == self.show_colors['fg']:
                self.score += 1
            self.user_answer.delete(0, END)
            self.show_colors.config(fg=str(choice(self.colors)), text=str(choice(self.colors)), font=('Arial', 45))

            self.score_label.config(text='Score:  ' + str(self.score))
        else:
            self.show_colors.config(fg='red', text='Time is left', font=('Arial', 45))
            with my_manager(base) as bm:
                bm.execute(self.sql, [self.atempt, self.score])
                bm.fetchall()



    def timer(self):

        if self.timeleft > 0:
            self.timeleft -= 1

        self.time_label.config(text='Timeleft: ' + str(self.timeleft))
        self.time_label.after(1000, self.timer)


    def startgame(self, *args):
        if self.timeleft == 20:
            self.timer()
    
        self.check_answer() 


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry(f'{HEIGHT}x{WIDTH}')
    app = Home_page(root)
    app.mainloop()