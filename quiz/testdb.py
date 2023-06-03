def bubbleSort(arr):

	n =  len(arr)

	for i in range(n):
		for j in range(0, n - i - 1):
			if arr[j] < arr[j + 1]:
				arr[j], arr[j + 1] = arr[j+1], arr[j]

myarr = [34, 56, 12, 67, 89, 13, 12, 43]
bubbleSort(myarr)
for i in range(len(myarr)):
	print("{}".format(myarr[i]))


