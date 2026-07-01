# Enunciado 8 – Sistema de Calificaciones con Estructuras Combinadas
# Crea un sistema que maneje un diccionario de listas donde las claves son materias
# y los valores son listas de notas de estudiantes (arreglos paralelos con lista de nombres).
# Implementa funciones para: calcular el promedio por materia, encontrar al mejor estudiante
# de cada materia y generar un reporte ordenado por promedio general de mayor a menor.


students = ['Ana', 'Pedro', 'Cielo', 'Erick', 'Juan Carlos', 'Ariadna']
courses = {
    'Comunicación': [17, 15, 20, 12, 13, 16],
    'Física': [14, 18, 19, 12, 11, 20],
    'Geometría': [8, 12, 15, 17, 20, 11]
}

def calculate_the_average(course_dictionary):
    print('='*13, ' PROMEDIOS POR MATERIA ', '='*13)

    for matters, notes in course_dictionary.items():
        print(' '*3, f'[ Materia: {matters:<13} | Promedio: {(sum(notes) / len(notes)):.1f} ]')


def best_student_subject(student_dictionary, course_dictionary):
    print('\n' + '='*10, ' MEJOR ESTUDIANTE POR MATERIA ', '='*9)

    for matters, notes in course_dictionary.items():
        print(' '*6, f"{matters:<13}: {student_dictionary[notes.index(max(notes))]:<12} | Nota: {max(notes)}")


def general_average_report(student_dictionary, course_dictionary):
    print('\n' + '='*6, ' RANKING DEL PROMEDIO DE CADA ALUMNO ', '='*6)
    ranking_list = []

    for index in range(len(student_dictionary)):
        student_notes = []
        
        for notes in course_dictionary.values():
            student_notes.append(notes[index])
            
        ranking_list.append({'student': student_dictionary[index], 'average': sum(student_notes) / len(student_notes)})
        
    ranking_list.sort(reverse=True, key=lambda x: x['average'])
    
    for position, student in enumerate(ranking_list, start=1):
        print(' '*10 + f"{position}° {student['student']:<11} | Promedio: {student['average']:>4.1f}")
        
    print('='*51)


calculate_the_average(courses)
best_student_subject(students, courses)
general_average_report(students, courses)