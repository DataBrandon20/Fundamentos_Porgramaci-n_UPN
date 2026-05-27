# Enunciado 3 – Búsqueda Simple en una Lista de Emails
# Tienes la lista: emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
# 1) Imprime cuántos emails son de Gmail.
# 2) Muestra solo los emails que terminan en '.com'.
# 3) Verifica si 'luis@outlook.com' está en la lista (usa 'in').


emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']

print('='*20, ' CONTEO GMAIL ', '='*20)
gmail_amount = 0
for email in emails:
    if 'gmail' in email:
        gmail_amount += 1
print(' '*4,f'CANTIDAD DE CORREO GMAIL: {gmail_amount}')

print('\n' + '='*18, ' TERMINAN EN .COM ', '='*18)
for email in emails:
    if email.endswith('.com'):
        print(' '*4, f'· {email}')

print('\n' + '='*17, ' VERIFICACIÓN EMAIL ', '='*17)
for email in emails:
    if 'luis@outlook.com' in email:
        print(f'El email [{email}] si está en la lista.')
print('\n' + '='*56)