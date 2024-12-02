# AOC - M3nxudo @ 
fp = 'input.txt'
list1 = []
list2 = []
with open(fp, 'r') as f:
    for line in f:
        part1, part2 = line.split()
        list1.append(int(part1))
        list2.append(int(part2))
sorted_1 = sorted(list1)
sorted_2 = sorted(list2)
total_distance = 0
# Fase 1
for number_1, number_2 in zip(sorted_1, sorted_2):
    dist = abs(number_2 - number_1)
    total_distance += dist
print(total_distance)
dict_1 = {}
similarity = 0
# Fase 2
for i in range(0, len(sorted_1)):
    if dict_1.get(sorted_1[i]) is None:
        appears_count = 0
        for j in range(0, len(sorted_2)):
            if sorted_2[j] == sorted_1[i]:
                appears_count += 1
            if sorted_2[j] > sorted_1[i]:
                dict_1[sorted_1[i]] = appears_count
                similarity += appears_count * sorted_1[i]
                break
    else:
        similarity += sorted_1[i] * dict_1[sorted_1[i]]
print(similarity)

