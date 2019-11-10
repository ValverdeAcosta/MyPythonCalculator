import tkinter
from tkinter import *



class App:
    def __init__(self, master):
        #Creacion del marco
        frame=Frame(master)
        frame.pack()
        

        #obtencion del valor y evaluacion con control de error
        def get_value(entryWidget):
            value = entryWidget.get()
            
            try:
                return int(value)
            except ValueError:
                return None
        #obtencion del segundo valor y evaluacion con control de error
        def get_valuesecond(entryWidget):
            value2 = entryWidget.get()
            
            try:
                return int(value2)
            except ValueError:
                return None

        #Nos devuelve el valor si no es None 
        def convert(value):
            if value is None:
                return None
            else:
                return value

        def convert2(value2):
            if value2 is None:
                return None
            else:
                return value2

        #Cada set_label_text es para uno de los 4 tipos de operacion posibles.
        #Con esto pedimos los numeros, pero debe ser con un input de texto
        def set_label_text(label,label2,entry, entry2):
            value = convert(get_value(entry))
            value2= convert2(get_valuesecond(entry2))

            #Si el valor 1 y 2 es None, te sigue dando la opcion de introducir un numero en el input, sino te devuelve la operación
            if value is None and value2 is None:
                label['text'] = "Enter an integer"
                
            else:
                label['text'] = value+value2
                label.config(font=('Courier',18))
        def set_label_text2(label,label2,entry, entry2):
            value = convert(get_value(entry))
            value2= convert2(get_valuesecond(entry2))

            if value is None and value2 is None:
                label['text'] = "Enter an integer"
                label2['text'] = "Enter an integer"
            else:
                label['text'] = value-value2
                label.config(font=('Courier',18))
        def set_label_text3(label,label2,entry, entry2):
            value = convert(get_value(entry))
            value2= convert2(get_valuesecond(entry2))
            

            if value is None and value2 is None:
                label['text'] = "Enter an integer"
                label2['text'] = "Enter an integer"
            else:
                label['text'] = value*value2
                label.config(font=('Courier',18))
        def set_label_text4(label,label2,entry, entry2):
            value = convert(get_value(entry))
            value2= convert2(get_valuesecond(entry2))

            if value is None and value2 is None:
                label['text'] = "Enter an integer"
                label2['text'] = "Enter an integer"
            else:
                label['text'] = value/value2
                label.config(font=('Courier',18))
        #Establecer anchura y altura del cuadro
        
        
        #Aqui establecemos los botones que va a tener el programa
        self.button=Button(
            frame, text="X", fg="white", width=10, height=2, bg="crimson", command=frame.quit
        )
        self.button.pack(side=LEFT)
        e = tkinter.Entry(root)   
        e2 = tkinter.Entry(root)   
        l = tkinter.Label(root, text="")
        r = tkinter.Label(root, text="")
        suma = tkinter.Button(root, text="+", command=lambda: set_label_text(l,r,e,e2))
        resta = tkinter.Button(root, text="-", command=lambda: set_label_text2(l,r,e,e2))
        multi = tkinter.Button(root, text="x", command=lambda: set_label_text3(l,r,e,e2))
        divide = tkinter.Button(root, text="/", command=lambda: set_label_text4(l,r,e,e2))

        suma.config(height=2,width=8, bg="grey", fg="black")
        resta.config(heigh=2,width=8, bg="DarkOliveGreen1", fg="black")
        multi.config(heigh=2,width=8, bg="grey", fg="black")
        divide.config(heigh=2,width=8, bg="DarkOliveGreen1", fg="black")
        

        e.pack()
        e2.pack()
        l.pack()
        r.pack()
        suma.pack()
        resta.pack()
        multi.pack()
        divide.pack()

#Aqui llamamos a la clase predefinida de Tkinter y la introducimos en una variable con la clase App.       
root = Tk()
app = App(root)
if __name__ == '__main__':
    root.config(bg="gray")
    root.title("My Calculator")
    root.geometry("300x400")
    root.mainloop()
root.mainloop()
root.destroy()
    
       