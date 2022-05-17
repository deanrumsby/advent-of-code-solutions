class Santa:
    """For delivering presents - Now equipped with a copy of RoboSanta too"""
    def __init__(self):
        self.visited = {(0, 0)}
        self.x, self.y = (0, 0)

    def move(self, vector):
        """Moves Santa by a given vector"""
        delta_x, delta_y = vector
        self.x += delta_x
        self.y += delta_y
        self.visited.add((self.x, self.y))

    def how_many_visited(self):
        """How many unique places has Santa visited"""
        return len(self.visited)

    def reset(self):
        """Resets the visited places and starting coords"""
        self.visited = {(0, 0)}
        self.x, self.y = (0, 0)