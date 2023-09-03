my_set = {"January", "February", "March"}
print(my_set)
# we cannot access individual element as we did in the list, we can only get them using for loop
for element in my_set:
    print(element)

# Add element to set
my_set.add("April")
print(my_set)

my_set1 = ["January", "February", "March"]
my_set1.remove("January")
print(my_set1)