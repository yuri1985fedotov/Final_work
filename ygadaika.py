from random import randint
from time import sleep

def is_valid(n, limit):
  if n.isdigit():
    return int(n) in range(1, limit+1)
  return False

def answer():
  while 1:
    answer = input().lower().strip()
    if answer not in("да","нет"):
      print("Введите 'да' или 'нет'")
      continue
    if answer == 'да':
      game()
    if answer == 'нет':
      print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
      break

def game():
  print('Добро пожаловать в числовую угадайку!')
  sleep(0.9)
  limit = int(input('Введите верхнюю границу диапазона игры: '))
  num = randint(1, limit)
  amt = 0
  while 1:
    n = input()
    if not is_valid(n, limit):
      print(f'А может быть все-таки введем целое число от 1 до {limit}?')
      continue
    n = int(n)
    if n == num:
      amt += 1
      print('Вы угадали, поздравляем! Число попыток:', amt)
      sleep(0.9)
      print("Хотите сыграть еще разок?) Да/Нет")
      break
    if n < num:
      print('Ваше число меньше загаданного, попробуйте еще разок')
      amt += 1
    if n > num:
      print('Ваше число больше загаданного, попробуйте еще разок')
      amt += 1

game()
answer()