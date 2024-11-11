import tkinter as tk
import random


def  init_gui():
    root = tk.Tk()
    return root


def init_frames(root):
    lbl_greet = tk.Label(root, text="Подбор ключа активации Photoshop",
                          font = ('',50))
    lbl_greet.pack(anchor='center', expand=True)


    def clicked():

        code_num1 = 0
        code_num2 = 0
        key_final = ''
        checking = False
        code_num1 = random.randint(1,25)
        while not checking:
            code_num2 = random.randint(1,26)
            if code_num2 > code_num1:
                checking = True
        if code_num1 < 10: 
            key_final = key_final + '0' + str(code_num1) + ' '
        else:
            key_final = key_final + str(code_num1) + ' ' 
        for i in range(5):
            key_fragment = 0
            key_fragment = random.randint(int(ord('A'))+(code_num1-1)
                                            ,int(ord('A'))+(code_num2-1))
            key_final = key_final + chr(key_fragment)
        if code_num2 < 10: 
            key_final = key_final + ' ' + '0' + str(code_num2)
        else:
            key_final = key_final + ' ' + str(code_num2)
        lbl_key = tk.Label(root, text='Ключ активации Photoshop - '
                            + key_final,font = ('',20))
        lbl_key.pack(anchor='center', expand= True)

    
    btn_hack = tk.Button(root, text ='Подобрать ключ', 
                         command=lambda: clicked())
    btn_hack.pack(anchor='center', expand= True)

root = init_gui()
root.geometry('1280x720')
bg_img = tk.PhotoImage(file='LABA3/bg_ps.png')
lbl_bg = tk.Label(root, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
init_frames(root)
root.mainloop()