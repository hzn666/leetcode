ip = ""
string = list(map(int, input().split('.')))
number = int(input())

for i in string:
    binary = bin(i)[2:].rjust(8, "0")
    ip += binary

print(int(ip, 2))

ip = bin(number)[2:].rjust(32, "0")
ip_list = []
for i in range(0, len(ip), 8):
    ip_list.append(str(int(ip[i:i + 8], 2)))

print(".".join(ip_list))
