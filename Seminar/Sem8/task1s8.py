from function import *
from interface import *

path = open('phone_book.txt', 'a')
interface(path)
path.close()