# a = [1,2,3,4,5]
# b = a
# a[0] = 99
# print(a)
# print(b)

my_lst = [1,2,3,4,5,6]
iterator = iter(my_lst)
try:
  print(next(iterator))
except Exception as e:
  print(e)