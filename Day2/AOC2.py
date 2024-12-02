# AOC - M3nxudo
def check_safety(_report):
    init_direction = 0
    for i in range(1, len(_report)):
        difference = int(_report[i]) - int(_report[i-1])
        # Checks
        if abs(difference) > 3:
            return 0
        if abs(difference) < 1:
            return 0
        else:  # Check direction
            if i == 1:  # Initial difference for sign
                if difference > 0:
                    init_direction = 0
                else:
                    init_direction = 1
            else:
                if difference > 0:
                    direction = 0
                else:
                    direction = 1
                if direction != init_direction:
                    return 0
    return 1


# Fase 1
fp = 'input.txt'
with open(fp, 'r') as f:
    list_of_reports = [line.split() for line in f]
total_safe = 0
for report in list_of_reports:
    safe = check_safety(report)
    total_safe += safe
print(total_safe)
