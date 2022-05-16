from os import F_OK


class FloorFinder:
    def __init__(self, starting_floor):
        self.instructions = []
        self.floor = starting_floor

    def load_instructions(self, file_path):
        with open(file_path) as file:
            instructions = file.read()
        for instruction in instructions:
            self.instructions.append(instruction)
        
    def change_floor(self, instruction):
        if instruction == "(": self.floor += 1
        elif instruction == ")": self.floor -= 1

    def final_floor(self):
        for instruction in self.instructions:
            self.change_floor(instruction)
        return self.floor

    def position_of_first_entry(self, floor):
        for position, instruction in enumerate(self.instructions):
            self.change_floor(instruction)
            if self.floor == floor:
                return position + 1
        return -1

    def set_floor(self, floor):
        self.floor = floor


finder = FloorFinder(0)
finder.load_instructions("input.txt")
final_floor = finder.final_floor()
finder.set_floor(0)
basement_entry_position = finder.position_of_first_entry(-1)

print(final_floor, basement_entry_position)
