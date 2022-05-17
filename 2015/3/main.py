from classes.delivery_controller import DeliveryController

# Part 1
dc = DeliveryController()
dc.load_directions('input.txt')
dc.deliver_presents()
num_with_present = dc.how_many_visited()

# Part 2
dc.reset()
dc.add_helper()
dc.deliver_presents()
num_with_present2 = dc.how_many_visited()

# Answers 
print(num_with_present, num_with_present2)