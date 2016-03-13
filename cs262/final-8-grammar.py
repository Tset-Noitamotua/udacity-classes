# Discerning the Grammar 
# Challenge Problem 
#
# Focus: Units 3 and 4: Parsing and Memoization
#
#
# In this problem you are provided with the final chart that results from 
# applying the parsing algorithm from class (i.e., Earley's algorithm) 
# to a particular string of tokens. 
#
# Your task is to reverse-engineering the simplest grammar that would yield
# exactly the chart given. 
#
# You should encode your answer using the grammar format from class. Assign
# your answer to a variable named "grammar".
#
# For example, if you think the answer is
#
#       S -> T
#       T -> p Q r
#       T -> p Q s
#       Q -> q 
#
# Then you would write 
#
#   grammar = [
#     ("S", ["T"]),
#     ("T", ["p","Q","r"]),
#     ("T", ["p","Q","s"]),
#     ("Q", ["q"]),
#   ]
#
# The actual input string of tokens is:
#
# ["id", "(", "(", "id", ")", ",", "id", ")"]
#
# That string was in the language of the grammar (i.e., the parse succeeded). 
# 
# The actual resulting chart was:  
#       (Hint: although this output looks long, a correct answer from you
#       will only use about a dozen lines.) 

# == chart[0]
#     E ->  .  (  E  )            from 0
#     E ->  .  E  -  E            from 0
#     E ->  .  E  +  E            from 0
#     E ->  .  id                 from 0
#     E ->  .  id  (  A  )        from 0
#     S ->  .  E                  from 0

# == chart[1]
#     E ->  E  .  -  E            from 0
#     E ->  E  .  +  E            from 0
#     E ->  id  .                 from 0
#     E ->  id  .  (  A  )        from 0
#     S ->  E  .                  from 0

# == chart[2]
#     A ->  .                     from 2
#     A ->  .  NA                 from 2
#     E ->  .  (  E  )            from 2
#     E ->  .  E  -  E            from 2
#     E ->  .  E  +  E            from 2
#     E ->  .  id                 from 2
#     E ->  .  id  (  A  )        from 2
#     E ->  id  (  .  A  )        from 0
#     E ->  id  (  A  .  )        from 0
#     NA ->  .  E                 from 2
#     NA ->  .  E  ,  NA          from 2

# == chart[3]
#     E ->  (  .  E  )            from 2
#     E ->  .  (  E  )            from 3
#     E ->  .  E  -  E            from 3
#     E ->  .  E  +  E            from 3
#     E ->  .  id                 from 3
#     E ->  .  id  (  A  )        from 3

# == chart[4]
#     E ->  (  E  .  )            from 2
#     E ->  E  .  -  E            from 3
#     E ->  E  .  +  E            from 3
#     E ->  id  .                 from 3
#     E ->  id  .  (  A  )        from 3

# == chart[5]
#     A ->  NA  .                 from 2
#     E ->  (  E  )  .            from 2
#     E ->  E  .  -  E            from 2
#     E ->  E  .  +  E            from 2
#     E ->  id  (  A  .  )        from 0
#     NA ->  E  .                 from 2
#     NA ->  E  .  ,  NA          from 2

# == chart[6]
#     E ->  .  (  E  )            from 6
#     E ->  .  E  -  E            from 6
#     E ->  .  E  +  E            from 6
#     E ->  .  id                 from 6
#     E ->  .  id  (  A  )        from 6
#     NA ->  .  E                 from 6
#     NA ->  .  E  ,  NA          from 6
#     NA ->  E  ,  .  NA          from 2

# == chart[7]
#     A ->  NA  .                 from 2
#     E ->  E  .  -  E            from 6
#     E ->  E  .  +  E            from 6
#     E ->  id  (  A  .  )        from 0
#     E ->  id  .                 from 6
#     E ->  id  .  (  A  )        from 6
#     NA ->  E  ,  NA  .          from 2
#     NA ->  E  .                 from 6
#     NA ->  E  .  ,  NA          from 6

# == chart[8]
#     E ->  E  .  -  E            from 0
#     E ->  E  .  +  E            from 0
#     E ->  id  (  A  )  .        from 0
#     S ->  E  .                  from 0

# What was the grammar? 

# For this challenge problem, we do not provide any testing hints. However,
# you may use any code you like from any source (such as this class). 

work_count = 0      # track one notion of "time taken"

def addtoset(theset,index,elt):
  if not (elt in theset[index]):
    theset[index] = [elt] + theset[index]
    return True
  return False

def parse(tokens,grammar):
  global work_count
  work_count = 0
  tokens = tokens + [ "end_of_input_marker" ]
  chart = {}
  start_rule = grammar[0]
  for i in range(len(tokens)+1):
    chart[i] = [ ]
  start_state = (start_rule[0], [], start_rule[1], 0)
  chart[0] = [ start_state ]
  for i in range(len(tokens)):
    while True:
      changes = False
      for state in chart[i]:
        # State ===   x -> a b . c d , j
        x = state[0]
        ab = state[1]
        cd = state[2]
        j = state[3]

        # Current State ==   x -> a b . c d , j
        # Option 1: For each grammar rule c -> p q r
        # (where the c's match)
        # make a next state               c -> . p q r , i
        # English: We're about to start parsing a "c", but
        #  "c" may be something like "exp" with its own
        #  production rules. We'll bring those production rules in.
        next_states = [ (rule[0],[],rule[1],i)
          for rule in grammar if cd <> [] and cd[0] == rule[0] ]
        work_count = work_count + len(grammar)
        for next_state in next_states:
          changes = addtoset(chart,i,next_state) or changes

        # Current State ==   x -> a b . c d , j
        # Option 2: If tokens[i] == c,
        # make a next state               x -> a b c . d , j
        # in chart[i+1]
        # English: We're looking for to parse token c next
        #  and the current token is exactly c! Aren't we lucky!
        #  So we can parse over it and move to j+1.
        if cd <> [] and tokens[i] == cd[0]:
          next_state = (x, ab + [cd[0]], cd[1:], j)
          changes = addtoset(chart,i+1,next_state) or changes

        # Current State ==   x -> a b . c d , j
        # Option 3: If cd is [], the state is just x -> a b . , j
        # for each p -> q . x r , l in chart[j]
        # make a new state                p -> q x . r , l
        # in chart[i]
        # English: We just finished parsing an "x" with this token,
        #  but that may have been a sub-step (like matching "exp -> 2"
        #  in "2+3"). We should update the higher-level rules as well.
        next_states = [ (jstate[0], jstate[1] + [x], (jstate[2])[1:],
                         jstate[3] )
          for jstate in chart[j]
          if cd == [] and jstate[2] <> [] and (jstate[2])[0] == x ]
        work_count = work_count + len(chart[j])
        for next_state in next_states:
          changes = addtoset(chart,i,next_state) or changes

      # We're done if nothing changed!
      if not changes:
        break

## Comment this block back in if you'd like to see the chart printed.
#
  for i in range(len(tokens)):
   print "== chart [" + str(i) + ']'
   for state in chart[i]:
     x = state[0]
     ab = state[1]
     cd = state[2]
     j = state[3]
     print "    " + x + " ->",
     for sym in ab:
       print " " + sym,
     print " .",
     for sym in cd:
       print " " + sym,
     print " from " + str(j)

  accepting_state = (start_rule[0], start_rule[1], [], 0)
  return accepting_state in chart[len(tokens)-1]

grammar = [\
('S', ['E']),
('E', ['id', '(', 'A', ')']),
('E', ['id']),
('E', ['E', '+', 'E']),
('E', ['E', '-', 'E']),
('E', ['(', 'E', ')']),
('A', ['NA']),
('NA', ['E', ',', 'NA']),
('NA', ['E']),
('A', []),
]

tokens = ["id", "(", "(", "id", ")", ",", "id", ")"]
result=parse(tokens, grammar)
print result
