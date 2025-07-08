def QuickSort(arr):

	if len(arr) <= 1:
		return arr

	pivot = arr[len(arr) // 2] # middle item
	lowers = [item for item in arr if item < pivot]
	equals = [item for item in arr if item == pivot]
	greaters = [item for item in arr if item > pivot]

	return QuickSort(lowers) + equals + QuickSort(greaters)


if __name__ == '__main__':
	arr = [4, 3, 7, 2, 4, 6, 5, 8, 7, 8, 1, 0, 10, 9]
	quckSorted_arr = QuickSort(arr)
	print(quckSorted_arr)
	