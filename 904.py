from typing import List


def totalFruit(fruits: List[int]) -> int:
    res = 0

    for i in range(len(fruits)):
        fruit = []
        for j in range(i, len(fruits)):
            if len(list(set(fruit))) < 2:
                fruit.append(fruits[j])
            elif fruits[j] not in fruit:
                break
            else:
                fruit.append(fruits[j])

        res = max(res, len(fruit))

    return res


fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(totalFruit(fruits))
