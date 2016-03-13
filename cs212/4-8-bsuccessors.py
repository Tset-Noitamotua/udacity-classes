# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    result = {}
    here, there, t = state
    if 'light' in here:
        for p1 in [_ for _ in here if _ != 'light']:
            for p2 in [_ for _ in here if _ != 'light']:
                a = (p1, p2, '->')
                t_here = frozenset([p for p in here if p != p1 and p != p2 and p != 'light'])
                t_there = frozenset([p for p in there] + [p1] + [p2] + ['light'])
                t_t = t + max(p1, p2)
                result[(t_here, t_there, t_t)] = a
    else:
        for p1 in [_ for _ in there if _ != 'light']:
            for p2 in [_ for _ in there if _ != 'light']:
                a = (p1, p2, '<-')
                t_there = frozenset([p for p in there if p != p1 and p != p2 and p != 'light'])
                t_here = frozenset([p for p in here] + [p1] + [p2] + ['light'])
                t_t = t + max(p1, p2)
                result[(t_here, t_there, t_t)] = a
    return result
    
def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print test()