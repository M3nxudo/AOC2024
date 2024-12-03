# AOC - M3nxudo
import re
# Fase 1
fp = 'input.txt'
total_result = 0
with open(fp, 'r') as f:
    for line in f:
        matches = re.findall("mul\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9])\)", line)
        for match in matches:
            num1 = int(match[0])
            num2 = int(match[1])
            mult = num1 * num2
            total_result += mult
print(total_result)
