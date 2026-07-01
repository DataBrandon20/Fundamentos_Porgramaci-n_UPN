#Enunciado Reto:
# Dado un log de servidor web (formato Apache), extrae IP, método HTTP, ruta y código de estado de cada línea usando
# solo métodos de strings.


def process_log(log):
    lines = log.strip().split("\n")
    extracted_logs = []

    for line in lines:
        if not line.strip():
            continue
            
        separate = line.split('"')
        ip = separate[0].split()[0]
        http_info = separate[1].split()
        method = http_info[0]
        route = http_info[1]
        code = separate[2].split()[0]

        extracted_logs.append({
            "IP": ip,
            "MÉTODO": method,
            "RUTA": route,
            "CÓDIGO": code
        })

    return extracted_logs

examples = """

192.168.1.45 - - [18/May/2026:14:32:10 +0200] "GET /tienda/productos/index.html HTTP/1.1" 200 4523

10.0.0.12 - - [18/May/2026:14:33:15 +0200] "POST /api/v1/usuarios HTTP/1.1" 201 128

172.16.254.1 - - [18/May/2026:14:35:01 +0200] "GET /admin/configuracion_secreta.php HTTP/1.1" 404 987
    
"""

result_list = process_log(examples)
print("\n" + "="*20 + " LOGS PROCESADOS " + "="*20)

for index, log_dict in enumerate(result_list, start=1):
    print(f"\n[Registro N° {index}]")

    for clue, value in log_dict.items():
        print(f"  {clue}: {value}")
    print("-" * 57)