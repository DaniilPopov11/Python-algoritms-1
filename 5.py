a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print('Позиции: %d и %d' % (a, b))
print('Между буквами символов:', abs(a - b) - 1)

n = int(input('Номер буквы в алфавите: '))
n = ord('a') + n - 1
print('Это буква', chr(n))