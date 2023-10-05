def fibonacci(n):
  sum = 0
  num1 = 0
  num2 = 1
  count = 1

  while (count < n):
    sum = num1 + num2
    num1 = num2
    num2 = sum
    count += 1
  return sum



