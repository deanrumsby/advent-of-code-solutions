from classes.santa import Santa

class DeliveryController:
    """To aid the control of Santa and co during deliveries"""
    def __init__(self):
        self.helpers = [Santa()]
        self.vectors = []

    def load_directions(self, file_path):
        """Loads and parses directions into vectors"""
        vectors = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
        with open(file_path) as file:
            directions = file.read()
        for direction in directions:
            self.vectors.append(vectors[direction])

    def current_helper(self):
        """Returns the first helper in the queue"""
        return self.helpers[0]

    def add_helper(self):
        """Adds a new helper to the queue"""
        self.helpers.append(Santa())

    def cycle_helpers(self):
        """Cycles the queue of helpers"""
        self.helpers.append(self.helpers.pop(0))

    def deliver_presents(self):
        """Shares the delivery instructions amongst all helpers"""
        for vector in self.vectors:
            self.current_helper().move(vector)
            self.cycle_helpers()

    def how_many_visited(self):
        """How many unique places have been visited in total"""
        all_places_visited = set()
        for helper in self.helpers:
            all_places_visited = all_places_visited.union(helper.visited)
        return len(all_places_visited)

    def reset(self):
        """Resets all helpers"""
        for helper in self.helpers:
            helper.reset()
        
