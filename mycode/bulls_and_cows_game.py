# https://en.wikipedia.org/wiki/Bulls_and_Cows
# pair programed this with kid on 2020/05/02
# this is the game portion, solution is in different file, see bulls_and_cows_solution.py

import random


def generate_secret_number():
  nums = random.sample(range(10), 4)
  return ''.join([str(i) for i in nums])


def calculate(secret_number, guessed_number):
  # calculate B
  b = 0
  for ch in guessed_number:
    if ch in secret_number:
      b += 1

  # calculate A
  a = 0
  for i in range(0, 4):
    if guessed_number[i] == secret_number[i]:
      a += 1

  # remove dups of Bs
  b = b - a
  return a, b


def is_valid_input(guessed_number):
  if not guessed_number.isdigit() or len(guessed_number) != 4:
    return False
  if len(set(guessed_number)) != 4:
    return False
  return True


def main():
  secret_number = generate_secret_number()
  # repeat: read input, calculate, and output; only if 4A, print WIN
  BACKDOOR_PASSWORD = 'idk'
  while True:
    guessed_number = input('Guess it: ')
    if guessed_number == BACKDOOR_PASSWORD:
      print(secret_number)
      continue
    if not is_valid_input(guessed_number):
      print('wrong input, need 4 unique digits, try again')
      continue
    a, b = calculate(secret_number, guessed_number)
    if a == 4:
      print('YOU GOT IT!')
      print('Now new challenge starts.')
      secret_number = generate_secret_number()
    else:
      print('%sA%sB' % (a, b))


def verify(sn, gn, expected):
  result = calculate(sn, gn)
  if result != expected:
    print('DARN, failed! sn=%s, gn=%s, expected=%s, result=%s'
          % (sn, gn, str(expected), str(result)))


def test():
  verify('1234', '2854', (1, 1))
  verify('1234', '5678', (0, 0))
  verify('1234', '0561', (0, 1))
  verify('1234', '0516', (0, 1))
  verify('1234', '0156', (0, 1))
  verify('1234', '2056', (0, 1))
  verify('1234', '1567', (1, 0))
  verify('1234', '0267', (1, 0))
  verify('1234', '8037', (1, 0))
  verify('1234', '8094', (1, 0))


if __name__ == '__main__':
  main()
  # test()
  # secret = generate_secret_number()
  # print(secret)
  # print(is_valid_input('1234'))
  # print(is_valid_input('1214'))
  # print(is_valid_input('124'))
  # print(is_valid_input('12480'))
  # print(is_valid_input('124b'))
  # print(is_valid_input('12b4'))
  # print(is_valid_input(''))
  # print(is_valid_input('1'))


