import tkinter as tk
import random


def  init_gui():
    root = tk.Tk()
    root.title("Взлом игр от Xatab")
    return root

def close(root):
    root.destroy()

# def init_lbls(root):
#     lbl_start = tk.Label(root, text="Подбор ключа активации Photoshop",
#                             font = ('',50))
#     lbl_start.pack(anchor='center', expand=True)
#     lbl_key_out = tk.Label(root)
#     lbl_key_out.pack(anchor='center', expand= True)
#     return lbl_start ,lbl_key_out


def init_button(root,label):
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
        for i in range(7):
            key_fragment = 0
            key_fragment = random.randint(int(ord('A'))+(code_num1-1)
                                            ,int(ord('A'))+(code_num2-1))
            print(key_fragment)
            key_final = key_final + chr(key_fragment)
        if code_num2 < 10: 
            key_final = key_final + ' ' + '0' + str(code_num2)
        else:
            key_final = key_final + ' ' + str(code_num2)
        print()

        label.configure(text="Ключ активации " +
                        "Red Dead Redemption 2 - "
                          + key_final, font = ('',20) ) 
    
    btn_hack = tk.Button(root, text ='Подобрать ключ', 
                         command=lambda: clicked())
    btn_hack.pack(anchor='center', expand= True)

    btn_exit = tk.Button(root, text ='Выход', 
                         command=lambda: close(root))
    btn_exit.pack(anchor='se', expand= True, padx=10, pady=10)

window = init_gui()
window.geometry('1280x720')


bg_img = tk.PhotoImage(file='LABA3/bg_rdr2.png')
lbl_bg = tk.Label(window, image=bg_img)


lbl_start = tk.Label(window, text="Подбор ключа активации"
                     + " Red Dead Redemption 2",font = ('',40))
lbl_start.pack(anchor='center', expand=True)

lbl_key_out = tk.Label(window)
lbl_key_out.pack(anchor='center', expand= True)

lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

init_button(window,lbl_key_out)

window.mainloop()