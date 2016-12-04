# Ruby Control Structures - Each

# Ruby offers control structures that let you iterate through its collections. One such control structure is each.
# As you already know, HackerRank conducts many contests, and for every user who participates in a contest we update their score once the
# contest ends. You will be given a method called scoring with an array passed as an argument. Elements of the array are of the class
# User.
# User class has a method update_score.
# Your task is to iterate through each of the elements in the array using each and call the method update_score on every element.

def scoring(array)
    # iterate through each of the element in array using *each* and call update_score on it
    array.each do |user|
        user.update_score
    end
end
