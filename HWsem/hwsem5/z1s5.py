a = 3
b = 5
def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a
print(f(a, b))