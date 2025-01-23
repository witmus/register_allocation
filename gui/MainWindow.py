from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger
from tkinter.ttk import Combobox, Progressbar

from matplotlib import pyplot as plt
import networkx as nx

from graphgen.display_tree import display_tree
from graphgen.generate_graph import generate_graph
from graphgen.get_input import get_input
from graphgen.get_symbols import get_symbols

class MainWindow(Tk):

    def show_ask_input(self):
        self.filepath.set(askopenfilename())

    def show_ask_registers(self):
        self.registers.set(str(askinteger("Registers", "Input number of registers")))

    def run(self):
        missing_data = []
        fp = self.filepath.get()
        regs = self.registers.get()
        algo = self.algoList.current()

        if fp == '':
            missing_data.append('file path')
        if regs == '':
            missing_data.append('number of registers')
        if algo == -1:
            missing_data.append('algorithm')
        if len(missing_data) > 0:
            messagebox.showinfo("Missing data", "Following data missing:\n -" + '\n- '.join(missing_data))
            return

        code = get_input(fp)
        display_tree(code)
        symbols = get_symbols(code)
        print(symbols)
        
        graph = generate_graph(symbols)
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()

    def __init__(self):
        super().__init__()
        self.geometry("450x150")
        self.title("Register allocation")
        self.filepath = StringVar()
        self.registers = StringVar()

        fileChooser = Button(self, text="Choose file", command=self.show_ask_input)
        fileChooser.grid(row=0,column=0,pady=10)
        fileLabel = Entry(self, textvariable=self.filepath, width=50, state=DISABLED)
        fileLabel.grid(row=0,column=1, columnspan=2,padx=10)
        
        registerChooser = Button(self, text="Set registers number", command=self.show_ask_registers)
        registerChooser.grid(row=1,column=0)
        registerLabel = Entry(self, textvariable=self.registers, state=DISABLED)
        registerLabel.grid(row=1,column=1,pady=10)

        self.algos = ['Brute Force', 'Greedy', 'Heuristic']
        
        self.algoList = Combobox(self, values=self.algos)
        self.algoList.set("Choose an algorithm")
        self.algoList.grid(row=1, column=2, pady=10)

        runButton = Button(self, text="Execute", command=self.run)
        runButton.grid(row=2, column=1)
        
