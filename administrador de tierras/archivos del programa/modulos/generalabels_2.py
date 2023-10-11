from tkinter import *

class ventana :


    def entrys (x, **kwargs):

        """ para los entrys solo necesitas el contenedor padre y los keys y values de los row y columns"""

        a = Entry(x)
        a.grid(row= kwargs["row"],column= kwargs["column"])
        

        return a 

    def labels(IF,cont,**kwargs):

        """para los labels tengo una condicion , si los args en posicion 1 es true, me da las obciones de pad
        en la posicion 0 me da el contenedor, de resto en los kwargs, si la condicion es true me toca colocar
        pading, pero si no es simplemente row y column"""

        a = None
    
        if IF == True:
            a = Label(cont,text = kwargs["texto"])
            a.grid(row= kwargs["row"],column = kwargs["column"],padx= kwargs["padx"],pady=kwargs["pady"] )


        else:

            a = Label(cont,text = kwargs["texto"])
            a.grid(row= kwargs["row"],column = kwargs["column"])


        return a
    
    def buttons (root,texto,**kawargs):

        a = Button(root,text = texto)
        a.grid(row = kawargs["row"], column = kawargs["column"])   

        return a 


# ----------------------------------------CONSTRUCTOR DE LABELS AUTOMATICO -----------------------------------------------------

    def constructorLabelsEntrysAutomatico (contenedor,inicio,tiene_pad,tipo_posicion,elementos,*args):


        l = {}
        e = {}

        if tipo_posicion == 1:
            # para abajo
            j = 0

            for x in range(inicio,elementos + inicio):

                l [x] = ventana.labels(tiene_pad,contenedor,texto = args[j],row= x ,column = 0) # se guardan en diccionarios
                e [x] = ventana.entrys(contenedor,row = x   ,column = 1)

                j += 1


    
        elif tipo_posicion == 2:
            # para lateral

            for x in range(inicio,elementos + inicio):

                l [x] = ventana.labels(contenedor,texto = args[j],row= 0 ,column = x) 
                e [x] = ventana.entrys(contenedor,row = 1   ,column = x)

        return l, e
    
# ----------------------------------- CONSTRUCTOR DE LABELS---------------------------------------------------------
    
    def constructorLabelsAutomatico (direccion,inicioSimpleNoProgresivo,inicioGenerador,contenedor,labels,tiene_pad,*args):



        if direccion == 1:
            """pa abajo"""

            

            j = 0
            for uwu in range(inicioGenerador,labels + inicioGenerador) : 

                ventana.labels(tiene_pad,contenedor,texto = args[j] ,row = uwu,column = inicioSimpleNoProgresivo )
                j += 1
                

        
        elif direccion == 2:
            """izquierda - deracha"""

            j = 0
            for uwu in range(inicioGenerador,labels + inicioGenerador) : 

                ventana.labels(tiene_pad,contenedor,texto = args[j] ,row = inicioSimpleNoProgresivo,column = uwu )
                j += 1



    def botones (root, direccion,cuantos,dependiente,independiente, border,*args,**kwargs):

        a = {}

        if border == 1:

            if direccion == 1:
                # abajo con border

                z = {}
                
                i = 0

                          

                for b in range(dependiente,cuantos + dependiente):

                    z[i] = Frame(kwargs["FRAMEF"])
                    z[i].grid(padx= 15,pady= 15, row = b, column = independiente )

                    a[i] = ventana.buttons(z[i],args[i],row = b, column = independiente)
                    i +=1 

            elif direccion == 2:
                # izquierda a derecha con border

               

                
                z = {}
                
                i = 0
                for b in range(dependiente,cuantos + dependiente):

                    z[i] = Frame(kwargs["FRAMEF"])
                    z[i].grid(padx= 15,pady= 15, row = independiente,column = b)

                    a[i] = ventana.buttons(z[i],args[i],row = independiente, column = b)
                    i +=1

        elif border == 2:
            
            if direccion == 1:
                # abajo


                
                i = 0
                for b in range(dependiente,cuantos + dependiente):

                    a[i] = ventana.buttons(root,args[i],row = b, column = independiente)
                    i +=1 

            elif direccion == 2:
                # izquierda a derecha

   

                
                i = 0
                for b in range(dependiente,cuantos + dependiente):

                    a[i] = ventana.buttons(root,args[i],row = independiente, column = b)
                    i +=1


        return a



        


   


    





    def pruebas ():

        root = Tk()
        frame = Frame()
        frame.grid()

        #a, b = ventana.constructorAutomatico (False,frame,1,2,"a","b")

        """ventana.constructorLabelsAutomatico(1,0,0,frame,5,False,"1","7","13","19","1")
        ventana.constructorLabelsAutomatico(1,1,0,frame,5,False,"2","8","14","20","1")
        ventana.constructorLabelsAutomatico(1,2,0,frame,5,False,"3","9","15","21","1")
        ventana.constructorLabelsAutomatico(1,3,0,frame,5,False,"4","10","16","22","1")
        ventana.constructorLabelsAutomatico(1,4,0,frame,5,False,"5","11","17","23","1")
        ventana.constructorLabelsAutomatico(1,5,0,frame,5,False,"6","12","18","24","1")"""

        

        ventana.botones(root,2,2,0,0,1,"boton 1", "boton 2",FRAMEF = frame)
        #botones (root, direccion,cuantos,dependiente,independiente, border,*args,**kwargs)
        #ventana.botones(root,1,2,0,0, False, "boton 1", "boton2")
         


        root.mainloop() 












