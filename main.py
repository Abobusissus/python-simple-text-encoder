from cryptography.fernet import Fernet
from time import *
from tkinter import *


# параметры графики 
window = Tk()
window.title("шифратор fernet ")
window.geometry('600x400')

# функция для кнопки назад        
def back ():
    print(1)
    for i in widgets:
        i.forget()
    f1.pack()

# функция для кнопки очистки
def clear():
    print(1)
    global result
    result.destroy()
    result = Text(window, bg = '#141414', fg = 'White')    
    
#функции для шифрования   
def encrypt ():
    b_back.pack()
    f1.forget()
    gl.pack()
    g.pack()
    costyl.pack()
def encrypt_costyl() :
    key = Fernet.generate_key()
    f = Fernet(key)
    key = str(key)
    text = g.get()
    text = text.encode( 'utf-8' )
    token = str(f.encrypt(text))
    result.insert(INSERT, f' зашифрованный текст: \n {token[2:-1]}  \n Ключ: {key[2:-1]}')
    result.pack()
    b_clear.pack()
    
    
# и дешифрования         
def decrypt():
    b_back.pack()
    f1.forget()
    gl.pack()
    g.pack()
    gl2.pack()
    g2.pack()
    costyl2.pack()
def decrypt_costyl():
    key =g2.get()
    key = key.encode( ' utf-8 ' )
    f = Fernet(key)
    token = g.get()
    token = token.encode( ' utf-8 ' )
    decrupt_t = f.decrypt(token)
    x = (str(decrupt_t)[2:-1])
    result.insert(INSERT, f'расшифрованный текст: \n {x}')
    b_back.pack()
    result.pack()
    b_clear.pack()
print(1)

#кнопочки и настройки графики 
costyl = Button(window, command= encrypt_costyl, text = 'зашифровать')
costyl2 = Button(window, command= decrypt_costyl, text = 'расшифровать')
gl = Label(window , text = 'введите текст' )    
g = Entry(window )
gl2 = Label(window , text = 'введите ключ' )    
g2 = Entry(window )   
f1 = Frame(window)
f2 = Frame(window)
result = Text(window)
b1 = Button(f1, command = encrypt , text = 'шифрация')
b2 = Button(f1, command = decrypt , text = 'дещифрация')
b_back = Button(window, command = back, text = 'Назад')
b_clear = Button(window, command = clear , text = 'очистка')
f1.pack()
b1.pack()
b2.pack()
global widgets 
widgets = [gl,g,gl2,g2,f1,f2,result,costyl,costyl2,b_back,b_clear]
widgets2  = [gl,g,gl2,g2,f1,f2,result,costyl,costyl2,b_back,b1,b2,window,b_clear]
for i in widgets2:
        i.config(bg = '#141414')
        try:
            i.config(fg = 'White')
        except :
            print(1)
window.mainloop()




      
