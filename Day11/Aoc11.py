# AOC - M3nxudo
# Fase 1
def evaluate_stone(stone_value):
    if stone_value == 0:  # 1st condition
        return [1]
    # Check if even digits
    temp = stone_value
    digit_count = 0
    while temp > 0:
        digit_count += 1
        temp //= 10
    if digit_count % 2 != 0:  # 3rd condition
        return [stone_value * 2024]
    # Split
    divisor = 10 ** (digit_count // 2)
    second_half = stone_value % divisor
    first_half = stone_value // divisor
    # 2nd condition
    return [first_half, second_half]


fp = 'input.txt'
total_stones = 0
with open(fp, 'r') as f:
    for line in f:
        stones = line.strip().split()
        for i in range(0, 25):
            temp_stones = []
            for stone in stones:
                out_stones = evaluate_stone(int(stone))
                for out_stone in out_stones:
                    temp_stones.append(out_stone)
            stones = temp_stones
print(f"Total stones: {len(stones)}")