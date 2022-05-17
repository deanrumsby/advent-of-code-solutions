class Santa:
    """For delivering presents"""
    def __init__(self):
        self.visited = {(0, 0)}
        self.vectors = []
        self.x, self.y = (0, 0)

    def load_directions(self, file_path):
        """Loads and parses directions into vectors"""
        vectors = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
        with open(file_path) as file:
            directions = file.read()
        for direction in directions:
            self.vectors.append(vectors[direction])

    def move(self, vector):
        """Moves Santa by a given vector"""
        delta_x, delta_y = vector
        self.x += delta_x
        self.y += delta_y
        self.visited.add((self.x, self.y))

    def deliver_presents(self):
        """Visit every location given by the instructions"""
        for vector in self.vectors:
            self.move(vector)

    def how_many_visited(self):
        """How many unique places has Santa visited"""
        return len(self.visited)