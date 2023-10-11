from tkinter import*
from tkinter import ttk
from modulos.generalabels_2 import ventana
import datetime



def programa_root():
    global root

    root = Tk()
    """   root title   """
    root_title = "MANEJO DE ZONAS CAFETERAS" 
    root.title(root_title)

    """   root icon   """
    #root.iconbitmap("logo.ico")
    #root.geometry("300x200+500+225")
    root.config(padx=10,pady=10)

    """  frame  """
    principal_box = Frame(root)
    principal_box.pack() 

    """frame de ingresada de datos"""

    box_1 = LabelFrame(principal_box,text="MENU DE SELECCION")
    box_1.pack(padx=10,pady=10)

    tituloGeneral = Label(box_1,text="SELECCIONA UNA DE LAS SIGIENTES OBCIONES") 
    tituloGeneral.grid(row=0,column=0,columnspan=2, padx=10,pady=10)

    """   border   """

    framex = Frame(box_1)
    framex.grid(padx = 15,pady = 15)


    """   seccion 1   """

    a = ventana.botones(root,2,3,0,0,1,"CONTEO PERSONAL","CPONTEO DE LA FINCA","CONTEO DE NEGOCIOS",FRAMEF = framex)

    a[0].config(command = conteo_personal)
    a[1].config(command = conteo_finca)
    a[2].config(command = conteo_negocios)


    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------

def conteo_personal():



    root.destroy()

    rootx = Tk()

    # configuracion basica 

    rootx.title("conteo personal")
    #rootx.iconbitmap("C:\\Users\\lenovo\\Documents\\inicio\\administrador de tierras\\archivos del programa\\logo.ico")
    rootx.config(padx=10,pady=10)

    """  frame  """
    principal_box = Frame(rootx)
    principal_box.pack() 

    """frame de ingresada de datos"""

   #BORDER


    box_1 = LabelFrame(principal_box,text="")
    box_1.pack(padx=10,pady=10)



    frameup = Frame(box_1)
    frameup.grid(row = 1,column = 0, padx = 15,pady = 15)

    framedown = Frame(box_1)
    framedown.grid(row = 2, column=0 ,padx = 15,pady = 15)   


    # continuar con lo que se tiene que meter



    fecha_actual = datetime.date.today ()

    border = LabelFrame(frameup,text="")
    border.grid(row = 0,column=0 ,padx=10,pady=10)


    tituloGeneral = Label(framedown,text="SELECCONA UNA DE LAS SIGUIENTES OBCIONES") 
    tituloGeneral.grid(row=0,column=0,columnspan=2, padx=10,pady=10)

    

    label_datos1 = Label(border, text = "FECHA =")
    label_datos1.grid(row = 0, column = 0)

    label_datos2 = Label(border, text = fecha_actual)
    label_datos2.grid(row = 0, column = 1)

    label_balance = Label(border,text=" -- BALANCE ACTUAL =")
    label_balance.grid(row = 0, column = 2, columnspan=2)

    label_balance2 = Label(border,text="XXX")
    label_balance2.grid(row = 0, column = 4)

    label_conciliacion = Label(border,text=" -- ULTIMA CONCILIACION =")
    label_conciliacion.grid(row = 0, column = 5, columnspan=2)

    label_conciliacion = Label(border,text="XXX")
    label_conciliacion.grid(row = 0, column = 7)

    label_fechaConciliacion = Label(border,text=" -- FECHA DE ULTIMA CONCILIACION =")
    label_fechaConciliacion.grid(row = 0, column = 8, columnspan=2)

    label_fechaConciliacion = Label(border,text="XXX")
    label_fechaConciliacion.grid(row = 0, column = 10)








    a = ventana.botones(framedown,2,7,0,1,1,"INGRESOS","DEUDORES","AHORROS","EGRESOS","DEUDAS","GASTOS","PENDIENTE DE PAGO",FRAMEF = framedown)

    #botones (root, direccion,cuantos,dependiente,independiente, border,*args,**kwargs)


    rootx.mainloop

#------------------------------------------------------------------------------------------------------------------------------------------------------------

def conteo_finca():
    root.destroy()

    rootx = Tk()

    # configuracion basica 

    rootx.title("conteo personal")
    #rootx.iconbitmap("C:\\Users\\lenovo\\Documents\\inicio\\administrador de tierras\\archivos del programa\\logo.ico")
    rootx.config(padx=10,pady=10)

    """  frame  """
    principal_box = Frame(rootx)
    principal_box.pack() 

    """frame de ingresada de datos"""

    box_1 = LabelFrame(principal_box,text="")
    box_1.pack(padx=10,pady=10)

    tituloGeneral = Label(box_1,text="selecciona una de las siguientes obciones") 
    tituloGeneral.grid(row=0,column=0,columnspan=2, padx=10,pady=10)

    """   border   """

    framex = Frame(box_1)
    framex.grid(padx = 15,pady = 15)   
    """   border   """
    framex = Frame(box_1)
    framex.grid(padx = 15,pady = 15) 

    # continuar con lo que se tiene que meter

    
    rootx.mainloop

#--------------------------------------------------------------------------------------------------------------------------------

def conteo_negocios():

    root.destroy()

    rootx = Tk()

    # configuracion basica 

    rootx.title("conteo personal")
    #rootx.iconbitmap("C:\\Users\\lenovo\\Documents\\inicio\\administrador de tierras\\archivos del programa\\logo.ico")
    rootx.config(padx=10,pady=10)

    """  frame  """
    principal_box = Frame(rootx)
    principal_box.pack() 

    """frame de ingresada de datos"""

    box_1 = LabelFrame(principal_box,text="")
    box_1.pack(padx=10,pady=10)

    tituloGeneral = Label(box_1,text="selecciona una de las siguientes obciones") 
    tituloGeneral.grid(row=0,column=0,columnspan=2, padx=10,pady=10)

    """   border   """

    framex = Frame(box_1)
    framex.grid(padx = 15,pady = 15)   
    """   border   """
    framex = Frame(box_1)
    framex.grid(padx = 15,pady = 15) 

    # continuar con lo que se tiene que meter

    


    root.mainloop
    

#------------------------------------------------------------------------------------------------------------------------------------

