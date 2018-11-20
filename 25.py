ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b)
}


def eval(expression):
  tokens = expression.split()
  stack = []

  for token in tokens:
    if token in ops:
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = ops[token](arg1, arg2)
      stack.append(result)
    else:
      stack.append(int(token))

  return stack.pop()


a = input().split()
line = ''
for i in a:
    if (i.isdigit() or i.lstrip('-').isdigit()) and i.find('.') == -1:
        line += i + ' '
    if i == '+' or i == '-' or i == '*' or i == '/':
        line += i + ' '
print(eval(line))
