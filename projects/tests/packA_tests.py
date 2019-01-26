import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(sys.path)
import packA.a1 as a1

a1.hello_a1()
