def check_win(d):
    """Input is a dictionary with keys 1-9 according to a numerical
    keypad:    789
               456
               123
    function checks win condition for tic tac toe and returns the dicts value"""
    w = ( (7, 8, 9), (4, 5, 6), (1, 2, 3,),
          (1, 4, 7), (2, 5, 8), (3, 6, 7),
          (7, 5, 3), (9, 5, 1))
    for fields in w:
        # if not all fields present, can  not be a win
        if all(f in d for f in fields):
            # if all fields the same, return 1st field as result
            if len(set(d[num] for num in fields)) == 1:
                return d[fields[0]]

    return None

# generate random tic tac toe placement order
from random import shuffle

nums = list(range(1, 10))
shuffle(nums)

# place X and O interleafed onto shuffled numbers
who = True
ttt = {}
for n in nums:
    ttt[n] = "X" if who else "O"
    who = not who
    winner = check_win(ttt)
    if winner:
        print("Winner:", winner)
        break
else:
    print("Draw!")

# output board
print(ttt.get(7, " "), ttt.get(8, " "), ttt.get(9, " "), 
      "\n"+ttt.get(4, " "), ttt.get(5, " "), ttt.get(6, " "),
      "\n"+ttt.get(1, " "), ttt.get(2, " "), ttt.get(3, " ")+"\n")
