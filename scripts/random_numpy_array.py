import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
print(sys.path)

from envtest import rand_array

shape = (3, 3)

print(rand_array(shape))
