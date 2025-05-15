import re

# Lista de palabras clave, operadores y símbolos válidos
palabras_clave = ['inicio', 'fin', 'imprimir']
operadores = ['=', '+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=']
simbolos = [';']

# Expresiones regulares para identificadores y números
regex_identificador = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
regex_numero = r'^[0-9]+$'

# Función para clasificar tokens
def analizar_token(token):
    if token in palabras_clave:
        print(f"[OK] Palabra clave reconocida: {token}")
    elif token in operadores:
        print(f"[OK] Operador reconocido: {token}")
    elif token in simbolos:
        print(f"[OK] Símbolo reconocido: {token}")
    elif re.match(regex_numero, token):
        print(f"[OK] Número reconocido: {token}")
    elif re.match(regex_identificador, token):
        print(f"[OK] Identificador válido: {token}")
    else:
        print(f"[ERROR] Token no reconocido: {token}")

# Función principal para leer y analizar el archivo
def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(f"Analizando el archivo: {nombre_archivo}\n")
            for num_linea, linea in enumerate(archivo, start=1):
                print(f"Línea {num_linea}: {linea.strip()}")
                # Expresión regular para separar todos los tokens posibles
                tokens = re.findall(
                    r'==|!=|<=|>=|[=+\-*/<>;()]|[a-zA-Z_][a-zA-Z0-9_]*|[0-9]+',
                    linea.strip()
                )
                for token in tokens:
                    analizar_token(token)
                print()
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{nombre_archivo}' no fue encontrado.")


# Llamamos a la función con el nombre del archivo fuente
nombre_archivo = "prueba2.txt"
analizar_archivo(nombre_archivo)

