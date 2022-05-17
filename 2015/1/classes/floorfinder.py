class FloorFinder:
    """Finds floors when the instructions are proving confusing"""
    def __init__(self, starting_floor):
        self.amounts = []
        self.floor = starting_floor

    def load_instructions(self, file_path):
        """Loads and parses instructions into amounts"""
        amounts = {'(': 1, ')': -1}
        with open(file_path) as file:
            instructions = file.read()
        for instruction in instructions:
            self.amounts.append(amounts[instruction])
            
    def change_floor(self, amount):
        """Changes floor by a given amount"""
        self.floor += amount

    def final_floor(self):
        """Determines the final floor visited"""
        for amount in self.amounts:
            self.change_floor(amount)
        return self.floor

    def position_of_first_entry(self, floor):
        """Finds the position a floor is first entered on"""
        for index, amount in enumerate(self.amounts):
            position = index + 1
            self.change_floor(amount)
            if self.floor == floor:
                return position
        # If no position found
        return -1

    def set_floor(self, floor):
        """Sets the starting floor"""
        self.floor = floor
