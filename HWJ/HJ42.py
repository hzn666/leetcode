num1 = [0, 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen']
num2 = [0, 0, 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']


def n2w(n):
    if n > 0:
        if n < 20:
            res.append(num1[n])
        else:
            res.append(num2[n // 10])
            if n % 10:
                res.append(num1[n % 10])


def hun(n):
    if n >= 100:
        res.append(num1[n // 100])
        res.append('hundred')
        if n % 100:
            res.append('and')
    n2w(n % 100)


n = int(input())

res = []

a = n % 1000
b = (n // 1000) % 1000
c = (n // 1000000) % 1000
d = n // 1000000000

if d > 0:
    hun(d)
    res.append('billion')
if c > 0:
    hun(c)
    res.append('million')
if b > 0:
    hun(b)
    res.append('thousand')
if a > 0:
    hun(a)

print(" ".join(res))
