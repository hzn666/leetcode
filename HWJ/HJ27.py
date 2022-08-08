input_list = input().split()
n = int(input_list[0])
word_list = input_list[1:n + 1]
word = input_list[n + 1]
n = int(input_list[-1])

res = []

for i in word_list:
    if i != word and sorted(i) == sorted(word):
        res.append(i)

res.sort()
print(len(res))
if n < len(res):
    print(res[n - 1])
