import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('450x300')

# welcom image
canvas = tk.Canvas(window, height = 200, width = 500)
img = tk.PhotoImage(file = "welcome.gif")
canvas.create_image(0, 0, anchor = 'nw', image = img)
canvas.pack(side = 'top')

#user info 

tk.Label(window, text = 'User name').place(x = 50, y = 150)
tk.Label(window, text = 'Password').place(x = 50, y = 190)

var_name = tk.StringVar()
var_name.set('example@python.com')
tk.Entry(window, textvariable = var_name).place(x = 150, y = 150)

var_pwd = tk.StringVar()
tk.Entry(window, textvariable = var_pwd, show= '*').place(x = 150, y = 190)

try:
    with open('user_info.pickle', 'rb') as user_file:
        pass
except:
    user_info = {'admin': 'admin'}
    with open('user_info.pickle', 'wb') as user_file:
        pickle.dump(user_info, user_file)



def log_in():
    name = var_name.get()
    pwd = var_pwd.get()
    
    with open('user_info.pickle', 'rb') as user_file:
        user_info = pickle.load(user_file)

    if name in user_info:
        if pwd == user_info[name]:
            tk.messagebox.showinfo(message = 'welcome ' + name)
        else:
            tk.messagebox.showerror('Error', 'Wrong Password')
    else:
        is_sign_up = tk.messagebox.askyesno(message = 'The user has not sign up yet. Sign today?')
        if is_sign_up:
            sign_up()
        

def sign_up():
    
    def new_member():
        nu = var_nu.get()
        np = var_np.get()
        renp = var_renp.get()
        
        with open('user_info.pickle', 'rb') as file:
            user_info = pickle.load(file)
            
        
        if nu in user_info:
            tk.messagebox.showerror('Error', 'The user has already signed up')
            sign_up()
        elif np != renp:
            tk.messagebox.showerror('Error', 'Confirmed password is different')
            sign_up()
        else:
            user_info[nu] = np
            with open('user_info.pickle', 'wb') as file:
                pickle.dump(user_info, file)
            tk.messagebox.showinfo(message = 'Welcome')
            sub_window.destroy()
    
    sub_window = tk. Toplevel(window)
    sub_window.title('Hellow')
    sub_window.geometry('400x200')
    
    tk.Label(sub_window, text = 'User name').place(x = 10, y = 20)
    tk.Label(sub_window, text = 'Password').place(x = 10, y = 60)
    tk.Label(sub_window, text = 'Again').place(x = 10, y = 100)
    
    var_nu = tk.StringVar()
    tk.Entry(sub_window, textvariable = var_nu).place(x = 190, y = 20)
    var_np = tk.StringVar()
    tk.Entry(sub_window, textvariable = var_np, show = '*').place(x = 190, y = 60)
    var_renp = tk.StringVar()
    tk.Entry(sub_window, textvariable = var_renp, show= '*').place(x = 190, y = 100)
    
    tk.Button(sub_window, text = 'Sign up', command = new_member).place( x = 150, y = 150)
    
    
    

tk.Button(window, text = "Log In", command = log_in).place(x = 150, y = 220)
tk.Button(window, text = 'Sign Up', command = sign_up).place(x = 230, y = 220)







window.mainloop()