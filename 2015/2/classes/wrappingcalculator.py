class WrappingCalculator:
    """Calculates the wrapping and ribbon needed for presents"""
    def __init__(self):
        self.dimensions_list = []

    def load_dimensions(self, file_path):
        """Loads dimensions from input"""
        with open('input.txt') as file:
            dims_list = file.read().splitlines()
        for dims in dims_list:
            self.dimensions_list.append([int(dim) for dim in dims.split('x')])

    def smallest_side_area(self, dimensions):
        """Calculates the smallest side's area of the box"""
        ordered_dimensions = sorted(dimensions)
        area = ordered_dimensions[0] * ordered_dimensions[1]
        return area

    def surface_area(self, dimensions):
        """Calculates the surface area of the box"""
        (h, w, l) = dimensions
        surface_area = (2 * h * w) + (2 * h * l) + (2 * w * l)
        return surface_area

    def wrapping_paper_req(self, dimensions):
        """Calculates the wrapping paper needed for the box"""
        surface_area = self.surface_area(dimensions)
        smallest_side_area = self.smallest_side_area(dimensions)
        return surface_area + smallest_side_area

    def total_wrapping_req(self):
        """Calculates the total wrapping required for all presents"""
        total = 0
        for dimensions in self.dimensions_list:
            total += self.wrapping_paper_req(dimensions)
        return total

    def smallest_perimeter(self, dimensions):
        """Calculates the smallest perimeter of the box"""
        (h, w, l) = dimensions
        return min(2 * (h + w), 2 * (h + l), 2 * (w + l))

    def ribbon_bow_length(self, dimensions):
        """Calculates the ribbon needed to make the perfect bow"""
        (h, w, l) = dimensions
        return h * w * l

    def ribbon_req(self, dimensions):
        """Calculates the ribbon length needed for the box"""
        ribbon_for_box = self.smallest_perimeter(dimensions)
        ribbon_for_bow = self.ribbon_bow_length(dimensions)
        return ribbon_for_box + ribbon_for_bow

    def total_ribbon_req(self):
        """Calculates the total ribbon required for all presents"""
        total = 0
        for dimensions in self.dimensions_list:
            total += self.ribbon_req(dimensions)
        return total