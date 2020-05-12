# https://en.wikipedia.org/wiki/Bulls_and_Cows
# pair programed this with kid on 2020/05/02, main coding/naming done by kid,
# adviced on testing method only.
#
# Solving bulls and cows game using simple generation and elimination after guess.
#
# this is the solution code, game-code is in different file, see bulls_and_cows_game.py


def generate_all_list():
  unique_numbers = []
  for digit1 in range (10):
    for digit2 in range (10):
      for digit3 in range (10):
        for digit4 in range (10):
          if len({digit1, digit2, digit3, digit4}) == 4:
            string_num = str(digit1) + str(digit2) + str(digit3) + str(digit4)
            unique_numbers.append(string_num)
  return unique_numbers


def guess_and_input(remains):
  first_one = remains[0]
  print(first_one)
  ab_returned = input('Give me the ?A?B: ')
  return (first_one, ab_returned)


def compute_AB(first_num, second_num):
  #TODO: calculate b and a, then calculate a, then subtract
  b = 0
  a = 0
  for i in range(4):
    if first_num[i] in second_num:
      b += 1
  for i in range(4):
    if first_num[i] == second_num[i]:
      a += 1
  b = b - a
  return (str(a), str(b))


#extract --> ['1247', '5079']
def extract(guessed, inputted, remains):
  extracted = []
  for one in remains:
    a,b = compute_AB(guessed, one)
    #inputted --> '0A3B'
    if a == inputted[0] and b == inputted[2]:
      extracted.append(one)
  return extracted


def run():
  #generate a list, guess a number, input (?A?B), extract all that fit
  #remains --> ['1352', '1987', '2074']
  remains = generate_all_list()
  while len(remains) != 1:
    print (len(remains), 'number of numbers remain.')
    guessed, inputted = guess_and_input(remains)
    #inputted --> '0A3B'
    #guessed --> '1423'
    remains = extract(guessed, inputted, remains)
  return remains



def check(guessed, inputted, remains, expected):
  gotten = extract(guessed, inputted, remains)
  if gotten != expected:
    print('Oops! Gotten = ', gotten + ' , expected was ', expected)


#print(check('1134', '0A2B', '0248', ['1111', '2222']))

#print(generate_all_list())
#print(guess_and_input(generate_all_list()))
print(run())

#print(compute_AB('1472', '1724'))

#print(extract('1467', '1A1B', ['1234', '1467', '3456']))

#print(generate_all_list())

#print(guess_and_input(['1892', '1405', '3098']))

