from wrappingcalculator import WrappingCalculator

# Part 1
calculator = WrappingCalculator()
calculator.load_dimensions('input.txt')
total_wrapping_paper = calculator.total_wrapping_req()

# Part 2
total_ribbon = calculator.total_ribbon_req()

# Answers
print(total_wrapping_paper, total_ribbon)