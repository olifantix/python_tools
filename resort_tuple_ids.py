# https://stackoverflow.com/questions/65259214/is-there-a-fast-python-library-for-working-with-graph-edge-list

import random

# create a file with 500k lines and 1_000_000 numbers
# between 10k and 100k
nums = random.choices(range(10000,100001),k=1000000)

with open("t.txt","w") as f:
    for a,b in zip(nums[:len(nums)//2],nums[len(nums)//2:]):
        f.write(f"{a} {b}\n")

# read in file and write new file by resetting numbers starting at 1
d = {}
number = 0
with open("t.txt") as f, open("n.txt","w") as out:
    for line in f:
        if line:
            for k in line.split():
                if k not in d:
                    d[k] = number
                    number += 1
                out.write(f"{d[k]} ")
            out.write("\n")
