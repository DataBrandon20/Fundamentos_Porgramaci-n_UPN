#Enunciado 5 – VALIDAR Y FORMATEAR CORRE ELECTRÓNICO: 
# Escribe una función que reciba un email, lo limpie (strip+lower), verifique que contiene '@' y '.' y retorne el dominio.


def correo_electronico(email):

    if email == "":
        print("\n[ERROR] - No ingresó nada")
        return None
    
    elements = email.split("@")
    error = False

    if "@" not in email:
        print("\n[ERROR] - El email debe contener el símbolo '@'")
        error = True
    elif len(elements) != 2 or elements[0] == "" or elements[1] == "":
        print("\n[ERROR]- Estructura de correo inválida (ejemplo: usuario@upn.pe)")
        error = True
    elif ".." in elements[0] or "," in elements[0]:
        print("\n[ERROR] - La parte local del correo (antes del @) no puede contener '..' ni comas ','")
        error = True

    if not error:
        domain = elements[1]

        if "." not in domain:
            print("\n[ERROR] - El dominio debe contener al menos un punto '.'\n")
            error = True
        elif domain != "upn.pe":
            print(f"\n[ERROR] - El dominio '{domain}' no está autorizado. Solo se permite 'upn.pe'")
            error = True
    
    if not error:
        print("\n" + "-"*10 + "¡CORREO VÁLIDO!" + "-"*10)
        print("="*50)
        print(f"Email institucional: {email}")
        print(f"Parte local del email: {elements[0]}")
        print(f"Dominio del email: {elements[1]}")
        print("="*50 + "\n")

        return elements[1]
    return None

while True:
    user_email = input("\nIngrese su email institucional: \n").strip().lower()
    valid_email = correo_electronico(user_email)

    if valid_email == "upn.pe":
        break