import re  # Importa el módulo de expresiones regulares

# Lista de palabras reservadas válidas para el lenguaje
palabras_reservadas = [
    'main', 'fin', 'imprimir>', 'for', 'if', 'else',
    'num#', 'boolean#', 'string#', 'double#', 'TRUE', 'FALSE'
]

# Listas de operadores lógicos y aritméticos, y símbolos de agrupación válidos
operadores_logicos = ['>=', '<=', '==', '!=', '>', '<', '&', '|']
operadores_aritmeticos = ['=', '+', '-', '*', '/']
simbolos_agrupacion = ['(', ')', '{', '}', '[', ']']

# Expresiones regulares para validar identificadores, números, cadenas y decimales
regex_identificador = r'^[a-zA-Z][a-zA-Z0-9_]*$'
regex_numero = r'^[0-9]+$'
regex_cadena = r'^"[^"]*"$'
regex_decimal = r'^\d+\.\d+$'

# Analiza un token, determina su tipo y muestra un mensaje correspondiente
def analizar_token(token, num_linea):
    if token in palabras_reservadas:
        print(f"✔️ [OK] Palabra reservada reconocida: '{token}'")
    elif token in operadores_logicos:
        print(f"✔️ [OK] Operador lógico reconocido: '{token}'")
    elif token in operadores_aritmeticos:
        print(f"✔️ [OK] Operador aritmético reconocido: '{token}'")
    elif token in simbolos_agrupacion:
        print(f"✔️ [OK] Símbolo de agrupación reconocido: '{token}'")
    elif re.fullmatch(regex_numero, token):
        print(f"✔️ [OK] Número reconocido: '{token}'")
    elif re.fullmatch(regex_decimal, token):
        print(f"✔️ [OK] Número decimal reconocido: '{token}'")
    elif re.fullmatch(regex_cadena, token):
        print(f"✔️ [OK] Cadena reconocida: '{token}'")
    elif re.fullmatch(regex_identificador, token):
        print(f"✔️ [OK] Identificador válido: '{token}'")
    else:
        print(f"❌ [ERROR] Token no reconocido: '{token}'")

# Analiza línea por línea un archivo fuente y tokeniza su contenido
def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            print(f"Analizando el archivo: {nombre_archivo}\n")
            for num_linea, linea in enumerate(archivo, start=1):
                print(f"Línea {num_linea}: {linea.strip()}")

                # Extrae cadenas de texto para evitar que se dividan incorrectamente
                cadenas = re.findall(r'"[^"]*"', linea)
                temp_linea = re.sub(r'"[^"]*"', 'CADENA_TEMP', linea)

                # Expresión regular para dividir correctamente en tokens válidos
                token_pattern = re.compile(
                    r'('
                    r'"[^"]*"|'                                     # Cadenas
                    r'\b(?:main|fin|for|if|else|TRUE|FALSE)\b|'     # Palabras reservadas simples
                    r'(?:imprimir>|num#|boolean#|string#|double#)|' # Palabras reservadas con caracteres
                    r'==|!=|<=|>=|[=+\-*/<>&|]|'                    # Operadores
                    r'[\(\)\{\}\[\]]|'                              # Agrupadores
                    r'\d+\.\d+|\d+|'                                # Números (decimales y enteros)
                    r'[a-zA-Z][a-zA-Z0-9_]*|'                       # Identificadores
                    r'\S+'                                          # Otros tokens no válidos
                    r')'
                )
                tokens = token_pattern.findall(temp_linea.strip())

                # Reinsertar los "CADENA_TEMP" por las cadenas originales en el orden correcto
                cadena_idx = 0
                for i in range(len(tokens)):
                    if tokens[i] == 'CADENA_TEMP':
                        tokens[i] = cadenas[cadena_idx]
                        cadena_idx += 1

                # Analizar cada token extraído y muestra el análisis
                for token in tokens:
                    analizar_token(token, num_linea)
                print()
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{nombre_archivo}' no fue encontrado.")

# Nombre del archivo fuente
nombre_archivo = "prueba2.txt"
# nombre_archivo = "pruebaError2.txt"
analizar_archivo(nombre_archivo)