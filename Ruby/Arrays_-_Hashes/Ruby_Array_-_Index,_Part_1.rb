# Ruby Array - Index, Part 1 

# Array collections offer various ways to access their elements.

# The positions are 0 indexed. Objects of the array can be accessed using the [] method which may take various arguments, as explained below.

# arr = [9, 5, 1, 2, 3, 4, 0, -1]

# A number which is the position of element
# >>arr[4]
#   => 3

# or
# >>arr.at(4)
#   => 3 

# A range indicating the start and the end position
# >>arr[1..3] # .. indicates both indices are inclusive. 
#   => [5,1,2]
# >>arr[1...3] # ... indicates the last index is excluded.
#   => [5,1]

# Start index and the length of the range
# >>arr[1,4]
#   => [5, 1, 2, 3]

# For this challenge, your task is to complete the functions using syntax as explained above.


def element_at(arr, index)
    # return the element of the Array variable `arr` at the position `index`
    # arr.at(index) # or
    # arr[index]
    arr[index]
end

def inclusive_range(arr, start_pos, end_pos)
    # return the elements of the Array variable `arr` between the start_pos and end_pos (both inclusive)
    arr[start_pos..end_pos]
end

def non_inclusive_range(arr, start_pos, end_pos)
    # return the elements of the Array variable `arr`, start_pos inclusive and end_pos exclusive
    arr[start_pos...end_pos]
end

def start_and_length(arr, start_pos, length)
    # return `length` elements of the Array variable `arr` starting from `start_pos`
    arr[start_pos, length]
end
