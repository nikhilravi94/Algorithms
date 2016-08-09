#program to read contents of a file into a list, sort them using merge sort and count the number of inversions in the array

inversions = 0; #variable to store the number of inversions

#function to merge two sorted arrays
def merge_function(first_sorted, first_sorted_length, second_sorted, second_sorted_length):
	final_sorted = [];
	total_length = first_sorted_length + second_sorted_length;
	i = 0;
	j = 0;
	global inversions;
	for index in range(total_length):
		if (i < first_sorted_length and j < second_sorted_length):
			if first_sorted[i] <= second_sorted[j]:
				final_sorted.append(first_sorted[i]);
				i = i + 1;
			else:
				final_sorted.append(second_sorted[j]);
				j = j + 1;
				inversions += first_sorted_length - i;
		elif (i == first_sorted_length and j < second_sorted_length):
			final_sorted.append(second_sorted[j]);
			j = j + 1;
		elif (j == second_sorted_length and i < first_sorted_length):
			final_sorted.append(first_sorted[i]);
			i = i + 1;
	return final_sorted;

#recursive function to perform merge sort
def merge_sort(input_list, length):
	if length != 1:
		half_length = int(length/2);
		first_half = input_list[0:half_length];
		second_half = input_list[half_length:length];
		first_half_length = int(len(first_half));
		second_half_length = int(len(second_half));
		first_sorted = merge_sort(first_half, first_half_length);
		second_sorted = merge_sort(second_half, second_half_length);
		final_sorted = merge_function(first_sorted, int(len(first_sorted)), second_sorted, int(len(second_sorted)));
		return final_sorted;
	else:
		return input_list;
	return;

#IntegerArray.txt contains the input integer list
with open('IntegerArray.txt') as f:
	content_array = f.read().splitlines()

content_array = [int(x) for x in content_array];
	
final_sorted = merge_sort(content_array, int(len(content_array)));

#printing the final sorted array and the number of inversions
for number in final_sorted:
	print(number)

print("Number of inversions:", inversions)

