# Ruby Hash - Each

# You've seen the control structure each used on an array. Similarly, it is available for the Hash collection, as well.

# On Hash, it works in two ways.

# Consider the example
# user = {"viv" : 10, "simmy" : 20, "sp2hari" : 30}

# Using each, each element can be iterated as
# user.each do |key, value|
#    # some code on individual key, value
# end

# or
# user.each do |arr|
#    # here arr[0] is the key and arr[1] is the value
# end

# Your task is to use each and iterate through the collection and print the key-value pair in separate lines.

# Hint
# puts key
# puts value


def iter_hash(hash)
    # your code here
    hash.each do |key, value|
        puts key
        puts value
    end
end
