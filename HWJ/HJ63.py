dna = input()
n = int(input())

res = ""
max_count = 0

for i in range(len(dna) - n + 1):
    count = dna.count('C', i, i + n) + dna.count('G', i, i + n)
    if count > max_count:
        max_count = count
        res = dna[i:i + n]
print(res)
