# Task 
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the
# percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

# Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

# Input Format

# There are 3 lines of numeric input: 
# The first line has a double, mealCost (the cost of the meal before tax and tip). 
# The second line has an integer, tipPercent (the percentage of mealCost being added as tip). 
# The third line has an integer, taxPercent (the percentage of mealCost being added as tax).

# Output Format

# Print The total meal cost is totalCost dollars., where totalCost is the rounded integer result of the entire bill (mealCost with
# added tax and tip).

# Enter your code here. Read input from STDIN. Print output to STDOUT
mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

tip_cost = (tipPercent/100.)* mealCost
tax_cost = (taxPercent/100.)* mealCost
totalCost = int(round(mealCost + tip_cost + tax_cost))

print "The total meal cost is", totalCost, "dollars." 
