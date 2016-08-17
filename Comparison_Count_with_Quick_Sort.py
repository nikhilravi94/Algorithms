#variable to count the number of comparisons done during Quick Sorted
#The number of comparisons is equal to m - 1, where m is the length of each subarray during Quick Sort operation
comparisons = 0;

#function to find the median among the first, middle and last elements of an array
#choosing a pivot as the median value minimizes the number of comparisons to be made so that the average
#run time of the Quick Sort algorithm is O(nlog(n))
def median_finder(a, b, c):
	median = sorted([a, b, c])[1];
	return median;

#function to partition the array based on the choice of pivot
#other choices for the pivot: the first or the last element, but they generally lead to bigger subarrays and more comparison operations
#every time a pivot is chosen, it is swapped with the first position in the array to simplify the comparison process
#advantage of Quick Sort: all comparisons are done in place i.e. no extra memory is needed
def partition(input_list, left, right):
	global comparisons;
	if right > left:
		middle = (left + right)//2;
		pivot = median_finder(input_list[left], input_list[middle], input_list[right]);
		pivot_index = input_list.index(pivot);
		input_list[left], input_list[pivot_index] = input_list[pivot_index], input_list[left];
		i = left + 1;
		for j in range(left + 1, right + 1):
			if input_list[j] < pivot:
				input_list[i], input_list[j] = input_list[j], input_list[i];
				i = i+1;
		comparisons += right - left;
		input_list[left] , input_list[i - 1] = input_list[i - 1], input_list[left];
		left_of_pivot_sorted = partition(input_list, left, i - 2);
		right_of_pivot_sorted = partition(input_list, i, right);
		return input_list;
	else:
		return input_list;

with open('QuickSort.txt') as f:
	content_array = f.read().splitlines()

content_array = [int(x) for x in content_array];

sorted_input_list = partition(content_array, 0, len(content_array) - 1);

#printing the final sorted array and the number of comparisons
for number in sorted_input_list:
	print(number)

print("Number of comparisons:", comparisons)