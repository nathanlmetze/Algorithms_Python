# MergeSort algorithm
# By Nathan M. Using pseudocode from the book
# Using variable names found in the book
# Used for floor
import math

# Helper method
def merge(B, C, A):
	i = 0
	j = 0
	k = 0
	while i < len(B) and j < len(C):
		if B[i] <= C[j]:
			A[k] = B[i]
			i += 1
		else:
			A[k] = C[j]
			j += 1
		k += 1
	if i == len(B):
		A[k:] = C[j:]
	else:
		A[k:] = B[i:]


def merge_sort(A):
	B = []
	C = []
	if len(A) > 1:
		B = A[:math.floor(len(A)/2)]
		C = A[math.floor(len(A)/2):]
		merge_sort(B)
		merge_sort(C)
		merge(B, C, A)
		print(A)
merge_sort([8, 3, 2, 9, 7, 1, 5, 4])
