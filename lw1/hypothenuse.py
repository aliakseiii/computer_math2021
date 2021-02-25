import sys

if int(sys.argv[1]) <= 0 or int(sys.argv[2]) <= 0:
	print("Invalid data")
else:
	a = float(sys.argv[1])
	b = float(sys.argv[2])

	hypotenuse = (a**2+b**2)**(1/2)

	print("Length of hypotenuse is", hypotenuse)
