from tkinter import *
from tkinter import ttk
from modulos.genera_Labels import labels_progresive
from modulos.generalabels_2 import ventana


root = Tk()
"""   root title   """
root_title = "manejo de zonas cafeteras" 
root.title(root_title)

"""   root icon   """
root.iconbitmap("C:/Users/lenovo/Desktop/administrador de tierras/archivos del programa/logo.ico")
#root.geometry("300x200+500+225")
root.config(padx=10,pady=10)

"""  frame  """
principal_box = Frame(root)
principal_box.pack() 

"""frame de ingresada de datos"""

box_1 = LabelFrame(principal_box,text="ingresada de datos")
box_1.pack(padx=10,pady=10)

tituloGeneral = Label(box_1,text="inventario general") 
tituloGeneral.grid(row=0,column=0,columnspan=2, padx=10,pady=10)

"""   border   """

framex = Frame(box_1)
framex.grid(padx= 15,pady= 15)


"""   seccion 1   """


root.mainloop()
