# list1 = [1,2,3,5,8,15,23,38]

# def chet(a):
#     array = []
#     for i in a:
#         if i % 2 == 0:
#             # kvadrat = i*i
#             # para = f"({i}, {kvadrat})"
#             array.append((i, i**2))
#     return array

# print(chet(list1))

def select(f, col):
    return [f(x) for x in col]

def where (f, col):
    return [x for x in col if f(x)]

list1 = [1,2,3,5,8,15,23,38]
res = select(int, list1)
print (res)
res = where(lambda x: x % 2 == 0, res)
print (res)
res = list(select(lambda x: (x, x**2), res))
print (res)