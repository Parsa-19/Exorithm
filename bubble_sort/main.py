'''
in bubble_sort function:

var "i" role is to reduce the number of loop in inner for because after one procedure of inner loop with i=0 the   
"-1" is because it will swap item with its next one in arr; and if we remove that we'll get out of range error.
proccess: 

bubble_sort([4, 3, 2, 1])


i = 0
range(4-0-1) =3   |   arr = [4, 3, 2, 1]
j = 0	---afterLoop-->		[3, 4, 2, 1]
j = 1	---afterLoop-->		[3, 2, 4, 1]
j = 2	---afterLoop-->		[3, 2, 1, 4]


i = 1
range(4-1-1) =2   |   arr = [3, 2, 1, 4]
j = 0  	---afterLoop-->		[2, 3, 1, 4]
j = 1  	---afterLoop-->		[2, 1, 3, 4]


i = 2
range(4-2-1) =1   |   arr = [2, 1, 3, 4]
j = 0  	---afterLoop-->		[1, 2, 3, 4]
'''


import time

'''
decorator will calculate run time process
and also prints input value in first and output value of func 
'''
def run_time_decorator(func):
	def wrapper(*args, **kwargs):
		t1 = time.time()
		print('before = {0}'.format(*args))
		res = func(*args, **kwargs)
		print(f'after = {res}')
		elapsed = time.time() - t1
		print(f"\nelapsed time for ({func.__name__}): {elapsed}\n")
		return res
	return wrapper


@run_time_decorator
def bubble_sort(arr):
	length = len(arr)
	
	for i in range(length):
		swapped = False
		
		for j in range(length-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		if not swapped:
			break

	return arr


if __name__ == '__main__':
	arr = [4, 10, 2, 7, 8, 1, 5]
	# arr = [4, 3, 2, 1]
	# arr = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 1] # if min number is at the end in sorted list--> will cause first level loop to run 11 times
	# arr = [100, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29] # if max number is at the first of sorted list--> will cause first level loop to run 2 times
	bubble_sorted_arr = bubble_sort(arr)
	
