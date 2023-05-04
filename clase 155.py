from tkinter import*
from tkinter import filedialog
from PIL import ImageTk, Image
root=Tk()
root.title("Abrir imagenes")
root.geometry("400x400")
root.config(bg="lightgreen")

label_1=Label(root,text="Abrir imagenes",bg="lightblue",highlightthickness=4,font=15)
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)
a=""

def b():
    global a
    a=filedialog.askopenfilename(title="Abrir archivo de texto", filetypes=[("Archivos de imagen","*.jpg *.gif *.jpg *.png *.jpeg")])
    c=Image.open(a)
    d=ImageTk.PhotoImage(c)
    label_2["image"]=d
    a.close()



button_1=Button(root,text="Abrir la imagen", command=b )
button_1.place(relx=0.5,rely=0.3,anchor=CENTER)

label_2=Label(root,text=".",bg="lightblue",highlightthickness=4)
label_2.place(relx=0.5,rely=0.5,anchor=CENTER)


root.mainloop()
