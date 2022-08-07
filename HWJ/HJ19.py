import sys
from collections import deque

record = {}
in_queue = deque()
out_queue = []

for line in sys.stdin:
    line = line.split()
    path = line[0]
    ln = int(line[1])
    filename = path.split('\\')[-1][-16:]
    filename_ln = filename + str(ln)

    if filename_ln in in_queue:
        record[filename_ln][-1] += 1
    else:
        if filename_ln in out_queue:
            continue
        if len(record) == 8:
            pop_out = in_queue.popleft()
            record.pop(pop_out)
            out_queue.append(pop_out)

        record[filename_ln] = [filename, ln, 1]
        in_queue.append(filename_ln)

for k, v in record.items():
    for i in v:
        print(i, end=" ")
    print()
