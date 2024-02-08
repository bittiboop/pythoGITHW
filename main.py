import random

def caesar_cipher(text, key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + key - shift) % 26 + shift)
        else:
            encrypted_text += char
    return encrypted_text

try:
    length = int(input('Довжина паролю-> '))
    include_upper = input('Включити великі літери [Т|Н]-> ').upper() == 'Т'
    include_lower = input('Включити малі літери [Т|Н]-> ').upper() == 'Т'
    include_digits = input('Включити цифри [Т|Н]-> ').upper() == 'Т'
    include_symbols = input('Включити символи [Т|Н]-> ').upper() == 'Т'

    all_signs = ''

    if include_upper:
        all_signs += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if include_lower:
        all_signs += 'abcdefghijklmnopqrstuvwxyz'
    if include_digits:
        all_signs += '0123456789'
    if include_symbols:
        all_signs += '@#_*$'

    password = ''.join(random.choices(all_signs, k=length))
    print(f'Ваш пароль: {password}')

    key = int(input('Введіть цифру для шифру Цезаря: '))
    encrypted_password = caesar_cipher(password, key)
    print(f'Зашифрований пароль: {encrypted_password}')

except Exception as ex:
    print(f'Помилка!: {ex}')