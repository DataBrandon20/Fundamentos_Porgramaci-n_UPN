#Enunciado 1 – SALUDO PERSONALIZADO:
#Pide al usuario su nombre y muestra: 'Hola, [NOMBRE]! Bienvenido al curso.' El nombre debe aparecer en MAYÚSCULAS.


while True:

    user_name = input("\nIngrese su nombre: ").strip()
    valid_name = user_name and all(character.isalpha() or character.isspace() for character in user_name)

    if valid_name:
        break
    
    print("\n[ERROR] - El nombre no puede estar vacío ni contener números o símbolos.")

print(f"\nHola, {user_name.upper()}! Bienvenido al curso.")