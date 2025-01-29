from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger
from tkinter.ttk import Combobox, Progressbar

from backtracking import backtracking
from simplify_spill import simplify_and_spill
from greedy import greedy
from dsatur import dsatur
from tabu_search import tabu_search

from matplotlib import pyplot as plt
import networkx as nx

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
            # missing_data.append('file path')
            fp = 'input.txt'
        if regs == '':
            # missing_data.append('number of registers')
            regs = '3'
        if algo == -1:
            missing_data.append('algorithm')
        if len(missing_data) > 0:
            messagebox.showinfo("Missing data", "Following data missing:\n -" + '\n- '.join(missing_data))
            return

        algo = self.algoList.current()
        registers = int(regs)
        code = get_input(fp)
        symbols = get_symbols(code)
        
        graph = generate_graph(symbols)
        match algo:
            case 0:
                coloring = greedy(graph, is_welsh_powell=False)
            case 1:
                coloring = greedy(graph, is_welsh_powell=True)
            case 2:
                coloring = backtracking(graph, registers)
            case 3:
                coloring = dsatur(graph)
            case 4:
                coloring = simplify_and_spill(graph, registers)
            case 5:
                coloring = tabu_search(graph, registers)
            
        print(coloring)
        color_map = [coloring[node] for node in graph.nodes()]
        nx.draw(graph, with_labels=True, font_weight='bold', node_color=color_map, cmap=plt.cm.rainbow)
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

        self.algos = [
            'greedy',
            'welsh_powell',
            'backtracking',
            'dsatur',
            'simplify_spill',
            'tabu_search'
        ]
        
        self.algoList = Combobox(self, values=self.algos)
        self.algoList.set("Choose an algorithm")
        self.algoList.grid(row=1, column=2, pady=10)

        runButton = Button(self, text="Execute", command=self.run)
        runButton.grid(row=2, column=1)
        
