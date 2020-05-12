# Print spiral numbers
# created 4 solutions
# this is the easiest to code & understand
# will explain this one to kid on 2020/05/12
# should be most easy to understand and build


def init_matrix(k):
  return [[0] * k for i in range(k)]


#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# rdlluurrrdddlllluuuurrrr
def generate_rdlu(k):
  buff = []
  for i in range(1, k+1, 2):
    buff.append('r' * i)
    buff.append('d' * i)
    buff.append('l' * (i + 1))
    buff.append('u' * (i + 1))
  # print(''.join(buff))
  return ''.join(buff)[:(k*k)-1]


def move(row, col, action):
  if action == 'r':
    col += 1
  elif action == 'd':
    row += 1
  elif action == 'l':
    col -= 1
  elif action == 'u':
    row -= 1
  else:
    assert False, 'ERROR, this is illegal action char: ' + action
  return row, col


def generate_matrix(k):
  m = init_matrix(k)
  row = int((k - 1) / 2)
  col = int((k - 1) / 2)
  m[row][col] = 1
  rdlu = generate_rdlu(k)
  for i in range(k*k - 1):
    row, col = move(row, col, rdlu[i])
    m[row][col] = i + 2
  return m


def print_matrix(m):
  for line in m:
    for num in line:
      print('%3d' % num, end=' ')
    print()
  print()


def run():
  for i in range(1, 32):
    m = generate_matrix(i)
    print_matrix(m)
    print()


def test_rdlu():
  for i in range(1, 12):
    print('generating for:', i)
    print(generate_rdlu(i))


if __name__ == '__main__':
  # run()
  # test_rdlu()
  run()
  pass
