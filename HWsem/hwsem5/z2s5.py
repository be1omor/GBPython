def sum(a, b):
  if b == 0:
    return 0;
  return sum(a, b - 1) + 1
