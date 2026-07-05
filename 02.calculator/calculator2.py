print("Welcome to the simple calculator")
print("To close the program, just type q")

ops = {
  1: 'addition',
  2: 'subtraction',
  3: 'multiplication',
  4: 'division',
}

print(f'The available operations are: {ops[1]}, {ops[2]}, {ops[3]}, {ops[4]}')

res = None

while True:
  if res is None:
    res = input('Enter a number: ')
    if res.lower() == 'q':
      break

    res = int(res)

  op = input(f'Enter the number of operation \n1:{ops[1]}, \n2:{ops[2]}, \n3:{ops[3]}, \n4:{ops[4]}: \n')
  print('-------op:',op)

  if op.lower() == 'q':
    break

  if not op.isdigit():
    print('Invalid operation')
    continue

  op = int(op)

  if op not in ops:
    print('Invalid operation')
    continue

  n2 = input('Enter the next number: ')
  if n2.lower() == 'q':
    break

  n2 = int(n2)
  print(n2)
  if op == 1:
    res += n2
  elif op == 2:
    res -= n2
  elif op == 3:
    res *= n2
  elif op == 4:
    res /= n2
  else:
    print('Invalid operation')
    continue


  print(f'The result is: {res}' )
