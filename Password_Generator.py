from tkinter import *
import customtkinter
import string
import random
from tkinter import messagebox

customtkinter.set_appearance_mode("System")

root = customtkinter.CTk()

root.geometry("500x300")
root.title("Password Generator")
root.resizable(0,0)





def genrate():
    
    try:
        length = int(entry_Name.get())
        if length==0:
            show_label.configure(text="Please Choose Length Of The Password 😑", bg_color='red', font=customtkinter.CTkFont(size=12, weight='bold',))

        elif length <=1 or length <=7:
            show_label.configure(text="Length is too short :(", bg_color='red', font=customtkinter.CTkFont(size=12, weight='bold',))

        else:
    
            blank.delete(0,END)
            all = lower + upper + num + symbols
            show_label.configure(text="Password Generated 😃", bg_color='green', font=customtkinter.CTkFont(size=12, weight='bold',))
            temp = random.sample(all,length)
            password = "".join(temp)
            blank.insert(0,password)
            

    except Exception as ep:
        show_label.configure(text="Somthing went wrong 😢", bg_color='red', font=customtkinter.CTkFont(size=12, weight='bold'))
        messagebox.showinfo(title='Error',message="Entry shouldn't be empty/Only contain Number!", icon='error',)
   

def toggle_password_visibility():
    if(v1.get()==1):
        blank.configure(show='')
    else:
        blank.configure(show='*')

def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

#string
upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
symbols = string.punctuation
v1=IntVar(value=0)
#Label
M_title = customtkinter.CTkLabel(root,text="Password Generator",
                                font=("arial",20,"bold"))
M_title.place(relx=0.3, rely=0.01,)

lbl_Name = customtkinter.CTkLabel(root,text="Choose Password Length:",
                                font=("arial",15,"bold"))
lbl_Name.place(relx=0.01, rely=0.2,)

show_label = customtkinter.CTkLabel(root,width=300,corner_radius=50,text="MADE BY RAVI:")
show_label.place(relx=0.01, rely=0.4,)

label1 = customtkinter.CTkLabel(root,text="Genrated Password:",
                                font=("arial",15,"bold"))
label1.place(relx=0.01, rely=0.5)


#Entry
entry_Name = customtkinter.CTkEntry(root,width=50,corner_radius=10)
entry_Name.place(relx=0.01,rely=0.3)

blank = customtkinter.CTkEntry(root,show='*',width=190,corner_radius=8,placeholder_text="Your Password")
blank.place(relx=0.01,rely=0.6)

#Button
button0 = customtkinter.CTkButton(root, text="Generate",hover_color='green',command=genrate,font=customtkinter.CTkFont(size=12, weight='bold',))
button0.place(relx=0.4,rely=0.6)

show_password_button = customtkinter.CTkCheckBox(root, text="Show Password",variable=v1,command=toggle_password_visibility)
show_password_button.place(relx=0.01,rely=0.7)

ex = customtkinter.CTkButton(root, text="Quit",hover_color='red',command=root.destroy,font=customtkinter.CTkFont(size=12, weight='bold',))
ex.place(relx=0.01,rely=0.8)

appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root, values=["Light", "Dark", "System"],
                                                        command=change_appearance_mode_event)

appearance_mode_optionemenu.place(relx=0.01,rely=0.9)
root.mainloop()