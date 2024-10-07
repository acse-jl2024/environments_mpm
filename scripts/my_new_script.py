
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))

from envtest import my_func
from pandas import Series

A = Series([1,3,5])
b = 1
x = my_func(A,b)
print(x)

