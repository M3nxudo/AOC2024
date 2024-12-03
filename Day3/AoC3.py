# AOC - M3nxudo
import re
# Fase 1
pattern = "mul\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9])\)"
example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
fp = 'input.txt'
total_result = 0
with open(fp, 'r') as f:
    text = f.read()
    matches = re.findall(pattern, text)
    for match in matches:
        num1 = int(match[0])
        num2 = int(match[1])
        mult = num1 * num2
        total_result += mult
print(total_result)
# Fase 2
do = True
updated_result = 0
with open(fp, 'r') as f:
    text = f.read()
donts = re.split("don't\(\)", text)
for dont in donts:
    if do:
        matches = re.findall(pattern, dont)
        for match in matches:
            num1 = int(match[0])
            num2 = int(match[1])
            mult = num1 * num2
            updated_result += mult
        do = False
    else:
        dos = re.split("do\(\)", dont)
        if len(dos) > 1:
            for i in range(1, len(dos)):
                matches = re.findall(pattern, dos[i])
                for match in matches:
                    num1 = int(match[0])
                    num2 = int(match[1])
                    mult = num1 * num2
                    updated_result += mult
print(updated_result)
