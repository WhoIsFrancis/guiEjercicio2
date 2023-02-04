import tkinter

root = tkinter.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.title("Ejercicio 2")

lenguajes_prog = {"Java", "JavaScript", "CSS", "C++", "C#", "Python"}

mi_listbox = tkinter.Listbox(root, height=5)
mi_listbox.insert(0, *lenguajes_prog)
mi_listbox.grid(column=0, row=0, sticky=tkinter.W)
tkinter.Label(root, text="Lenguajes de programacion", padx=5, pady=5).grid(column=0, row=3, sticky=tkinter.W)

root.mainloop()
