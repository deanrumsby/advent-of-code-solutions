class FloorFinder:
    """Finds floors when the instructions are proving confusing"""
    def __init__(self, starting_floor):
        self.instructions = []
        self.floor = starting_floor

    def load_instructions(self, file_path):
        """Loads instructions"""
        with open(file_path) as file:
            instructions = file.read()
        for instruction in instructions:
            self.instructions.append(instruction)
        
    def change_floor(self, instruction):
        """Changes floor depending on the instruction"""
        if instruction == "(": self.floor += 1
        elif instruction == ")": self.floor -= 1

    def final_floor(self):
        """Determines the final floor visited"""
        for instruction in self.instructions:
            self.change_floor(instruction)
        return self.floor

    def position_of_first_entry(self, floor):
        """Finds the position a floor is first entered on"""
        for position, instruction in enumerate(self.instructions):
            self.change_floor(instruction)
            if self.floor == floor:
                return position + 1
        # If no position found
        return -1

    def set_floor(self, floor):
        """Sets the starting floor"""
        self.floor = floor

# Part 1
finder = FloorFinder(0)
finder.load_instructions("input.txt")
final_floor = finder.final_floor()

# Part 2
finder.set_floor(0)
basement_entry_position = finder.position_of_first_entry(-1)

# Answers
print(final_floor, basement_entry_position)
