#Enunciado 4 – DIVIDIR Y UNIR PALABRAS:
# Dada la cadena 'rojo,verde,azul,amarillo', separa los colores, ponlos en mayúsculas y únelos con ' | ' como separador.


chain = "rojo,verde,azul,amarillo"
print(f"\nCadena original: {chain}\n")
print(f"Cadena separada en mayúsculas: {chain.upper().split(',')}\n")
print(f"Cadena con separador: {' | '.join(chain.upper().split(','))}\n")