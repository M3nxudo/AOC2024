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


def check_dampened(_report):
    '''
    This method probably has a higher time complexity than the optimal solution,
    since we are brute forcing all the combinations with 1 fewer number in the sequence
    :param _report: report to evaluate
    :return: 1 if valid, 0 if not
    '''
    for i in range(len(_report)):
        shortened_sequence = _report[:i] + _report[i + 1:]
        if check_safety(shortened_sequence):
            return 1
    return 0


# Fase 1
fp = 'input.txt'
with open(fp, 'r') as f:
    list_of_reports = [line.split() for line in f]
total_safe = 0
for report in list_of_reports:
    safe = check_safety(report)
    total_safe += safe
print(f"Total safe reports: {total_safe}")

# Fase 2
total_dampened_example = 0
example = [[7, 6, 4, 2, 1],
          [1, 2, 7, 8, 9],
          [9, 7, 6, 2, 1],
          [1, 3, 2, 4, 5],
          [8, 6, 4, 4, 1],
          [1, 3, 6, 7, 9]]
for report in example:
    safe = check_dampened(report)
    total_dampened_example += safe
print(f"Total dampened safe examples: {total_dampened_example}")
total_dampened = 0
with open(fp, 'r') as f:
    list_of_reports = [line.split() for line in f]
total_safe = 0
for report in list_of_reports:
    safe = check_dampened(report)
    total_dampened += safe
print(f"Total dampened safe reports: {total_dampened}")
