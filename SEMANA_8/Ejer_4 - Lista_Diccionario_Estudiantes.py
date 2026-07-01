# Enunciado 4 – Lista de Diccionario de Estudiantes
# Crea una lista de diccionarios para 4 estudiantes con los campos: 'nombre', 'carrera' y 'promedio'.
# Imprime el nombre y promedio de cada estudiante.
# Luego muestra el nombre del estudiante con el promedio más alto.


students = [
    {'name': 'Juan', 'career': 'Ing. Sistemas', 'average': 13},
    {'name': 'Brandon', 'career': 'Ing. Industrial', 'average': 16},
    {'name': 'Pedro', 'career': 'Medicina', 'average': 17},
    {'name': 'Luis', 'career': 'Ing. Mecatrónica', 'average': 10}
]

print('='*20, ' REPORTE DE NOTAS ', '='*20)
for key in students:
    print(' '*12, f"Estudiante: {key['name']:<8} | Promedio: {key['average']:>2}")

print('\n' + '='*20, ' PROMEDIO MÁS ALTO ', '='*19)
best_student = max(students, key=lambda x: x['average'])
print(' '*12, f"El estudiante con mayor promedio es {best_student['name']}")
print(' '*12, f"Su promedio es: {best_student['average']}")
print('\n' + '='*54)