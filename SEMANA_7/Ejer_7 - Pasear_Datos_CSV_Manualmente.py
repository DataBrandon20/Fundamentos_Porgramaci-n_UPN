#Enunciado 7 – PARSEAR DATOS CSV MANUALMENTE:
# Dadas varias líneas CSV con formato 'nombre,nota,ciudad', extrae la información y muestra un reporte formateado.


def system_of_process(csv_data):
    clean_data = csv_data.strip()
    lines = clean_data.split("\n")
    extracted_data = []
    print("\n" + "="*20 + " MATRIZ DE DATOS LIMPIA " + "="*20)

    for line in lines:
        if "===" in line or "NOMBRE" in line or line.strip() == "":
            continue
            
        dates = line.split("|")

        name = dates[0].strip()
        note = dates[1].strip()
        city = dates[2].strip()

        print(f"Nombre: {name} | Nota: {note} | Ciudad: {city}")
        extracted_data.append([name, note, city])

    print("="*64 + "\n")
    
    return extracted_data
        
example_table = """
=======================================================
NOMBRE             | NOTA   | CIUDAD         
=======================================================
Ana Pérez          | 18     | Lima           
Juan Cáceda        | 15     | Arequipa       
María Ibáñez       | 20     | Cusco          
Carlos Torres      | 11     | Trujillo       
=======================================================
"""

system_of_process(example_table)