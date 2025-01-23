
def get_input(fp: str) -> str:
    if len(fp) > 0:
        f = open(fp)
        code = f.read()
        f.close()
    else:
        code = ""
        while True:
            line = input()
            if line == '':
                break
            code = code + line + '\n'
            
    return code