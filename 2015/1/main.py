from floorfinder import FloorFinder

# Part 1
finder = FloorFinder(0)
finder.load_instructions("input.txt")
final_floor = finder.final_floor()

# Part 2
finder.set_floor(0)
basement_entry_position = finder.position_of_first_entry(-1)

# Answers
print(final_floor, basement_entry_position)
