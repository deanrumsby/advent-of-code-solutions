from classes.santa import Santa

# Part 1
santa = Santa()
santa.load_directions('input.txt')
santa.deliver_presents()
num_with_present = santa.how_many_visited()

# Answers 
print(num_with_present)
