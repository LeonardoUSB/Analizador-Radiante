from pathlib import Path
import ply.lex as lex
#Para llevar cuenta de los errores en un archivo
cuentaError = 0 
#Nombre de los tokens
tokens = ['TkOBlock', 'TkCBlock', 'TkInt', 'TkBool', 'TkFunction',
            'TkOBracket','TkCBracket','TkSoForth','TkSemicolon', 'TkId',
            'TkComma','TkNum','TkAsig','TkPlus','TkPrint','TkComentario',
            'TkIf', 'TkApp', 'TkAnd', 'TkNot', 'TkLess', 'TkLeq', 'TkGeq',
            'TkGreater', 'TkEqual', 'TkNEqual', 'TkArrow', 'TkGuard',
            'TkFi','TkTwoPoints','TkMinus','TkMult','TkOr','TkWhile','TkEnd',
            'TkFalse','TkString','newline','TkSkip','TkOpenPar','TkClosePar']


#Codigo para cada Token
def t_TkOBlock(t):
        r'\{'  
        return t
    

def t_TkOpenPar(t):
    r'\('  
    return t

def t_TkClosePar(t):
    r'\)'  
    return t

def t_TkCBlock(t):
        r'\}'
        return t

def t_TkInt(t):
        r'int'
        return t

def t_TkBool(t):
        r'bool'
        return t

def t_TkFunction(t):
        r'function'
        return t

def t_TkGuard(t):
    r'\[\]'
    return t

def t_TkOBracket(t):
        r'\['
        return t
    
def t_TkCBracket(t):
        r'\]'
        return t
    
def t_TkSoForth(t):
        r'\.\.'
        return t

def t_TkSemicolon(t):
        r';'
        return t

def t_TkPrint(t):
        r'print'  
        return t
    
def t_TkComma(t):
        r',' 
        return t

def t_TkNum(t):
        r'\d+'  
        t.value = int(t.value)
        return t
    

def t_TkAsig(t):
        r':='  
        return t
    
def t_TkPlus(t):
        r'\+'  
        return t
    
def t_TkIf(t):
    r'if'  
    return t 

def t_TkApp(t):
    r'\.'  
    return t 

def t_TkAnd(t):
    r'and'  
    return t 

def t_TkNot(t):
    r'\!'  
    return t 

def t_TkLeq(t):
    r'<='
    return t

def t_TkLess(t):
    r'<'
    return t

def t_TkGeq(t):
    r'>='
    return t

def t_TkGreater(t):
    r'>'
    return t

def t_TkEqual(t):
    r'=='
    return t

def t_TkNEqual(t):
    r'<>'
    return t  

def t_TkArrow(t):
    r'-->'
    return t

def t_TkFi(t):
    r'fi'
    return t

def t_TkSkip(t):
    r'skip'
    return t

def t_TkTwoPoints(t):
    r':'
    return t

def t_TkMinus(t):
    r'-'
    return t

def t_TkMult(t):
    r'\*'
    return t

def t_TkOr(t):
    r'or'
    return t

def t_TkWhile(t):
    r'while'
    return t

def t_TkEnd(t):
    r'end'
    return t

def t_TkFalse(t):
    r'false'
    return t

def t_TkComentario(t):
        r'//.*'  
        pass  

def t_TkString(t):
    r'"([^"\n\\]*(\\["n\\][^"\n\\]*)*)"'  
    t.value = t.value[1:-1]  
    return t

def t_TkId(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'  
    return t    


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  
    pass  

t_ignore = ' \t' 

def t_error(t):
    global cuentaError
    cuentaError += 1
    row = t.lineno  
    columna = columna(t.lexer.lexdata, t)  
    error = f'Error: Unexpected character "{t.value[0]}" in row {row}, column {columna}\n'
    with open("resultado.out", "a", encoding="utf-8") as salida: 
        salida.write(error)
    t.lexer.skip(1)  

 #Consifue la posicion relativa en una linea por token
def columna(text, token):
    saltoLinea = text.rfind('\n', 0, token.lexpos)  
    columna = (token.lexpos - saltoLinea)  
    return columna


lexer = lex.lex()

def iniciarLexer(contenido):
    global cuentaError
    cuentaError = 0  
    lexer.input(contenido)  
    tokensValidos = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokensValidos.append(tok)  

    if cuentaError == 0:
        with open("resultado.out", "w", encoding="utf-8") as salida:
            for tok in tokensValidos:
                column = columna(contenido, tok)
                if tok.type == "TkId":
                    salida.write(f'{tok.type}("{tok.value}") {tok.lineno} {column}\n')
                elif tok.type == "TkNum":
                    salida.write(f'{tok.type}({tok.value}) {tok.lineno} {column}\n')
                elif tok.type == "TkString":
                    salida.write(f'{tok.type}("{tok.value}") {tok.lineno} {column}\n')
                else:
                    salida.write(f"{tok.type} {tok.lineno} {column}\n")


def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        contenido = archivo.read()
        iniciarLexer(contenido)

if __name__ == "__main__":
    import sys  
    if len(sys.argv) != 2:  
        print("No ingreso nada")
    elif sys.argv[1].endswith(".imperat"):
        leerArchivo(sys.argv[1])
    else:
         print("No tiene la extension correcta")

         


