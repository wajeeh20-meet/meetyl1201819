def ex1(x):

	y = x[0]
	z = x[-1]
	newList = [y,z]
	return newList


list1 = [1,2,3,4,5,6,7,8,9,0,9,85,34]

ex1(list1)
newNum = ex1(list1)
print (newNum)

def ex2(l):
	for i in l:
		if i < 5:
			print(i)

ex2(list1)