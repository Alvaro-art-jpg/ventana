import tkinter as tk


from tkinter import messagebox

def ventana_con_boton():
    ventana=tk.Tk()
    ventana.title("Comidaaaa")
    ventana.geometry("700x300+440+200")
    tk.Label(ventana, text="¿Estas trayendo comida?").pack()
    botones=tk.Frame(ventana)
    botones.pack(pady=20)
    boton1=tk.Button(botones,text="Si nagoncito", command=lambda:messagebox.showinfo("Respuesta","Más te vale"))
    boton1.pack(side="left",padx=50)
    boton2=tk.Button(botones,text="No, soy fan de Kunno", command=lambda:messagebox.showinfo("Respuesta","ok"))
    boton2.pack(side="left",padx=60)
    ventana.mainloop()
    
ventana_con_boton()