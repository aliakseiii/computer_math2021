import sys

if float(sys.argv[1]) <= 0 or float(sys.argv[2]) <= 0:
    print("Invalid data")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])

    hypothenuse = (a**2+b**2)**(1/2)

    print("Length of hypothenuse is", hypothenuse)
