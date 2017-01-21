def collatz(number):
  if (number % 2 == 0):
    num = number//2
    print(num)
    return num
  elif (number % 2 == 1):
    num = 3 * number + 1
    print(num)
    return num

def enter():
  print('Choose a number: ')
  number = int(input())
  value = number
  while True:
    value = collatz(value)
    if (value == 1):
      print(value)
      enter()

enter()
