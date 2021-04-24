import tkinter as tk
from tkinter import ttk
import main


def button_clicked():
    main.swarmSize = swarm_size.get()
    main.velocityMultiplier = velocity_multiplier.get()
    main.maxNumberOfIterations = iterations.get()
    main.c1 = c1.get()
    main.c2 = c2.get()
    main.w = w.get()
    main.pickedFunction = function.get()
    main.mainPSO()


# creating window
root = tk.Tk()
root.title("PSO")
root.geometry('720x720')

# Var Defs
swarm_size = tk.IntVar()
velocity_multiplier = tk.DoubleVar()
iterations = tk.IntVar()
function = tk.StringVar()
c1 = tk.IntVar()
c2 = tk.IntVar()
w = tk.IntVar()
# GUI
label0 = ttk.Label(root, text="Hello there!")

label1 = ttk.Label(root, text="Maksymalna liczba iteracji")
iterations_entry = ttk.Entry(root, textvariable=iterations, width=10)

label2 = ttk.Label(root, text="Liczba cząsteczek")
swarm_entry = ttk.Entry(root, textvariable=swarm_size, width=10)

label3 = ttk.Label(root, text="Współczynnik dążenia do najlepszego lokalnego rozwiązania: ")
c1_entry = ttk.Entry(root, textvariable=c1, width=10)

label4 = ttk.Label(root, text="Współczynnik dążenia do najlepszego globalnego rozwiązania: ")
c2_entry = ttk.Entry(root, textvariable=c2, width=10)

label5 = ttk.Label(root, text="współczynnik bezwładności, określa wpływ prędkości w poprzednim kroku")
w_entry = ttk.Entry(root, textvariable=w, width=10)

label6 = ttk.Label(root, text="Mnożnik prędkości")
velocity_entry = ttk.Entry(root, textvariable=velocity_multiplier, width=10)

label7 = ttk.Label(root, text="Funkcja")
function_entry = ttk.Combobox(root, width=25, textvariable=function)
function_entry['value'] = ('Funkcja Rastringa',
                           'Funkcja Stołu Holdera',
                           'Funkcja Eggholder')
function_entry.current()

button = ttk.Button(root, text="START", command=button_clicked).grid(row=10, column=0)

label0.grid(row=0, column=0)

label1.grid(row=1, column=0)
iterations_entry.grid(row=1, column=1)

label2.grid(row=2, column=0)
swarm_entry.grid(row=2, column=1)

label3.grid(row=3, column=0)
c1_entry.grid(row=3, column=1)

label4.grid(row=4, column=0)
c2_entry.grid(row=4, column=1)

label5.grid(row=5, column=0)
w_entry.grid(row=5, column=1)

label6.grid(row=6, column=0)
velocity_entry.grid(row=6, column=1)

label7.grid(row=7, column=0)
function_entry.grid(row=7, column=1)

root.mainloop()
