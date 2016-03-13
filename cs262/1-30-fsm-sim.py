# FSM Simulation

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        # Is there a valid edge?
        if (current, letter) in edges:
            # If so, take it.
            return fsmsim(string[1:], edges[(current, letter)], edges, accepting)
        else:
            # If not, return False.
            return False
        # Hint: recursion.


print fsmsim("aaa111", 1, edges, accepting)
# >>> True
