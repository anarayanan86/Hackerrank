# Ruby Array - Addition

# Arrays provide a variety of methods that allow to add elements to them.

# push allows one to add an element to the end of the list.
# >x = [1,2]
# >x.push(3)
# => [1,2,3]

# insert allows one to add one or more elements starting from a given index (shifting elements after the given index in the process).
# >x = [1,2]
# >x.insert(1, 5, 6, 7)
# => [1, 5, 6, 7, 2]

# unshift allows one or more elements to be added at the beginning of the list.
# >x = [1,2,3]
# >x.unshift(10, 20, 30)
# => [10, 20, 30, 1, 2, 3]

# In this challenge, your task is to complete three functions that take in the array arr and
# 1. Add an element to the end of the list
# 2. Add an element to the beginning of the list
# 3. Add an element after a given index (position)
# 4. Add more than one element after a given index (position)


def end_arr_add(arr, element)
    # Add `element` to the end of the Array variable `arr` and return `arr`
    arr.push(element)
end

def begin_arr_add(arr, element)
    # Add `element` to the beginning of the Array variable `arr` and return `arr`
    arr.unshift(element)
end

def index_arr_add(arr, index, element)
    # Add `element` at position `index` to the Array variable `arr` and return `arr`
    arr.insert(index, element)
end

def index_arr_multiple_add(arr, index)
    # add any two elements to the arr at the index
    arr.insert(index, 'a', 'b')
end
