import os
import subprocess

def display_tree(code: str):
    f = open('temp_code.txt', "x")
    f.write(code)
    f.close()
    subprocess.run("antlr4-parse GraphColoring.g4 prog -gui temp_code.txt")
    os.remove('temp_code.txt')