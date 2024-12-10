# AOC - M3nxudo
# Fase 1
class GridGame:
    def __init__(self, filepath):
        self.fp = filepath
        self.guard_map = []
        self.guard_position = [0, 0]
        self.guard_direction = [0, 0]  # movement vector
        self.visited_positions = set()  # stores unique values so we handle duplicate cells
        self.initialize_map()

    def is_valid_position(self, row, col):
        # Check if position is inside map/grid
        return 0 <= row < len(self.guard_map) and 0 <= col < len(self.guard_map[0])

    def move_position(self):
        next_position = [self.guard_position[0] + self.guard_direction[0],
                         self.guard_position[1] + self.guard_direction[1]]
        if self.is_valid_position(next_position[0], next_position[1]):
            if self.guard_map[next_position[0]][next_position[1]] != 1:  # No object
                self.guard_position = next_position
                self.visited_positions.add((self.guard_position[0], self.guard_position[1]))
            elif self.guard_map[next_position[0]][next_position[1]] == 1:
                # Rotate 90 degrees clockwise when hitting an object
                self.guard_direction = [self.guard_direction[1], -self.guard_direction[0]]
            return True
        else:
            return False

    def initialize_map(self):
        with open(self.fp, 'r') as f:
            lines = f.readlines()
            height = len(lines)
            width = len(lines[0].strip())  # strip to handle newline

        # Initialize empty map
        self.guard_map = [[0 for _ in range(width)] for _ in range(height)]

        # Parse map contents
        with open(self.fp, 'r') as f:
            for i, line in enumerate(f):
                for j, char in enumerate(line.strip()):
                    if char == '.':
                        self.guard_map[i][j] = 0  # Empty space
                    elif char == '#':
                        self.guard_map[i][j] = 1  # Object
                    # Check for guard initial position
                    elif char == '^':  # Up
                        self.guard_map[i][j] = 2
                        self.guard_position = [i, j]
                        self.guard_direction = [-1, 0]
                    elif char == '>':  # Right
                        self.guard_map[i][j] = 2
                        self.guard_position = [i, j]
                        self.guard_direction = [0, 1]
                    elif char == 'v':  # Down
                        self.guard_map[i][j] = 2
                        self.guard_position = [i, j]
                        self.guard_direction = [1, 0]
                    elif char == '<':  # Left
                        self.guard_map[i][j] = 2
                        self.guard_position = [i, j]
                        self.guard_direction = [0, -1]

    def run(self):
        # Add initial position to visited set
        self.visited_positions.add((self.guard_position[0], self.guard_position[1]))
        # Main game loop
        in_bounds = True
        while in_bounds:
            in_bounds = self.move_position()
        print(f"\nFinal Result: Guard visited {len(self.visited_positions)} positions")


def main():
    # Replace 'input.txt' with your input file path
    aoc6 = GridGame('input.txt')
    aoc6.run()


if __name__ == "__main__":
    main()
