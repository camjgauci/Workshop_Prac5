# Create open dictionary
the_dict = {}

#User input
string = input("Enter a string: ").lower()
string = string.split()

# Add key to dictionary and assign value to that particular string.
for key in string:
    if key in the_dict:
        the_dict[key] +=1
    else:
        the_dict[key] = 1
    sorted(the_dict)
# Loop for printing

for string in the_dict:
    print("{:<10} : {}".format(string, str(the_dict[string])))



