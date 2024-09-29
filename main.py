from tkinter import *
import style 
import config

root = Tk()
root.configure(bg='black')
root.geometry(f'{style.WIDTH}x{style.HEIGHT}')

root.title("MineSweeper Game")
root.resizable(False,False)

top_frame = Frame(root, bg = 'yellow', width = style.WIDTH, height = config.height_pred(25))
top_frame.place(x = 0,y = 0)

game_title = Label(top_frame,bg='red',fg='white',text='MineSweeper Game',font=('',48))
game_title.place(x= config.width_pred(30),y=config.height_pred(7))

center_frame = Frame(root,bg='white',width=config.width_pred(42.5),height=config.height_pred(60))
center_frame.place(x=config.width_pred(30),y=config.height_pred(30))








root.mainloop()
