# AOC - M3nxudo
import re
# Fase 1
fp = 'input.txt'
total_result = 0
with open(fp, 'r') as f:
    for line in f:
        equ = re.split(":", line)
        operands_str = re.split(" ", equ[1].strip())
        result = int(equ[0])
        operands = []
        for operand in operands_str:
            operands.append(int(operand))
        result_list = []
        num_operators = len(operands) - 1
        for i in range(0, 2**num_operators):
            binary_value = bin(i)[2:].zfill(num_operators)  # Binary representation of number with 0-padding
            accumulate = operands[0]  # Value to set the left to right precedence
            for j in range(0, num_operators):
                if binary_value[j] == '0':  # Add
                    accumulate += operands[j+1]
                elif binary_value[j] == '1':  # Multiply
                    accumulate = accumulate * operands[j + 1]
            result_list.append(accumulate)
            if accumulate == result:
                total_result += accumulate
                break
print(f"Total calibration result: {total_result}")
