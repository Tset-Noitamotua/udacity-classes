# Do Not Repeat Repeated Work
#
# Focus: Units 5 and 6: Interpreting and Optimization
#
#
# In class we studied many approaches to optimizing away redundant
# computation. For example, "X * 0" can be replaced with "0", because we
# know in advance that the result will always be 0. However, even if we do
# not know the answer in advance, we can sometimes save work. Consider this
# program fragment:
#
#       x = a + b + c;
#       y = 2;
#       z = a + b + c; 
#
# Even though we do not know what "a + b + c" will be, there is no reason
# for us to compute it twice! We can replace the program with: 
#
#       x = a + b + c;
#       y = 2;
#       z = x;          # works since "x = a + b + c;" above
#                       # and neither a nor b nor c has been changed since
#
# ... and always compute the same answer. This family of optimizations is
# sometimes called "common expression elimination" -- the subexpression
# "a+b+c" was common to two places in the code, so we eliminated it in one. 
#
# In this problem we will only consider a special case of this
# optimization. If we see the assignment statement:
#
#       var1 = right_hand_side ;  
#
# Then all subsequent assignment statements:
#
#       var2 = right_hand_side ;
#
# can be replaced with "var2 = var1 ;" provided that the "right_hand_side"s
# match exactly and provided that none of the variables involved in
# "right_hand_Side" have changed. For example, this program cannot be
# optimized in this way:  
#
#       x = a + b + c;
#       b = 2;
#       z = a + b + c; 
#
# Even though the right-hand-sides are exact matches, the value of b has
# changed in the interim so, to be safe, we have to recompute "a + b + c" and
# cannot replace "z = a + b + c" with "z = x". 
#
# For this problem we will use the abstract syntax tree format from our
# JavaScript interpreter. Your procedure will be given a list of statements
# and should return an optimized list of statements (using the optimization
# above). However, you will *only* be given statement of the form:
#
#       ("assign", variable_name, rhs_expression) 
#
# No other types of statements (e.g., "if-then" statements) will be passed
# to your procedure. Similarly, the rhs_expression will *only* contain
# expressions of these three (nested) form:
#
#       ("binop", exp, operator, exp)
#       ("number", number)
#       ("identifier", variable_name) 
#
# No other types of expressions (e.g., function calls) will appear. 
#
# Write a procedure "optimize()" that takes a list of statements (again,
# only assignment statements) as input and returns a new list of optimized
# statements that compute the same value but avoid recomputing
# whole right-hand-side expressions. (If there are multiple equivalent
# optimizations, return whichever you like.) 
#
# Hint: x = y + z makes anything involving y and z un-available, and
# then makes y + z available (and stored in variable x).   

def optimize(ast):

    def includes(idname, element):
        if len(element) == 1:
            return False
        if len(element) == 2:
            return element == ('identifier', idname)
        for e in element:
            if includes(idname, e):
                return True
        return False

    while True:
        changed = False
        env = {}
        for i in range(len(ast)):
            # remove unsafe rhs
            for lhs in env.keys():
                if env[lhs][0] == 'binop':
                    if includes(ast[i][1], env[lhs]) or includes(lhs, env[lhs]):
                        #print 'pop:', lhs, 'because of', ast[i][1]
                        env.pop(lhs)

            for lhs, rhs in env.items():
                if rhs == ast[i][2]:
                    ast[i] = (ast[i][0], ast[i][1], ('identifier', lhs))
                    changed = True
                    break

            env[ast[i][1]] = ast[i][2]

            #re-evaluate env
            for lhs, rhs in env.items():
                if rhs[0] == 'identifier' and rhs[1] in env:
                    env[lhs] = env[rhs[1]]

            #print 'env:'
            #for k, v in env.items():
            #    print k, ':', v
        
        if not changed:
            break
    
    return ast

# We have included some testing code to help you check your work. Since
# this is the final exam, you will definitely want to add your own tests.

example1 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("number", 2)) ,
("assign", "z", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
] 
answer1 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("number", 2)) ,
("assign", "z", ("identifier", "x")) ,
] 
         
print (optimize(example1)) == answer1

example2 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "a", ("number", 2)) ,
("assign", "z", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
] 

print (optimize(example2)) == example2

example3 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "x", ("number", 2)) ,
("assign", "z", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
] 
answer3 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("identifier", "x")) ,
("assign", "x", ("number", 2)) ,
("assign", "z", ("identifier", "y")) , # cannot be "= x" 
] 

print (optimize(example3)) == answer3

example4 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("binop", ("identifier","b"), "+", ("identifier","c"))) ,
("assign", "z", ("binop", ("identifier","c"), "+", ("identifier","d"))) ,
("assign", "b", ("binop", ("identifier","c"), "+", ("identifier","d"))) ,
("assign", "z", ("number", 5)) ,
("assign", "p", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "q", ("binop", ("identifier","b"), "+", ("identifier","c"))) ,
("assign", "r", ("binop", ("identifier","c"), "+", ("identifier","d"))) ,
] 

answer4 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("binop", ("identifier","b"), "+", ("identifier","c"))) ,
("assign", "z", ("binop", ("identifier","c"), "+", ("identifier","d"))) ,
("assign", "b", ("identifier", "z")) ,
("assign", "z", ("number", 5)) ,
("assign", "p", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "q", ("binop", ("identifier","b"), "+", ("identifier","c"))) ,
("assign", "r", ("identifier", "b")) ,
] 

print optimize(example4) == answer4

example5 = [("assign", "x",("number",5)),
            ("assign", "y",("binop",("identifier", "a"),"+",("identifier", "b"))),
            ("assign", "x",("binop",("identifier", "y"),"+",("identifier", "z"))),
            ("assign", "z",("binop",("identifier", "a"),"+",("identifier", "b")))]

answer5 = [('assign', 'x', ('number', 5)), 
           ('assign', 'y', ('binop', ('identifier', 'a'), '+', ('identifier', 'b'))), 
           ('assign', 'x', ('binop', ('identifier', 'y'), '+', ('identifier', 'z'))), 
           ('assign', 'z', ('identifier', 'y'))]

print optimize(example5) == answer5

example6 = [('assign', 'x', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'b')), '+', ('identifier', 'c'))), 
            ('assign', 'y', ("number", 2)), 
            ('assign', 'z', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'b')), '+', ('identifier', 'c')))]

answer6 = [('assign', 'x', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'b')), '+', ('identifier', 'c'))), 
           ('assign', 'y', ("number", 2)), 
           ('assign', 'z', ('identifier', 'x'))]

print optimize(example6) == answer6

example7 = [('assign', 'x', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))), 
            ('assign', 'e', ("number", 2)), 
            ('assign', 'z', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c')))]

answer7 = [('assign', 'x', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))), 
           ('assign', 'e', ("number", 2)), 
           ('assign', 'z', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c')))]

print optimize(example7) == answer7

example8 = [("assign", "x", ("binop", ("identifier","x"), "+", ("binop", ("identifier","z"), "+", ("number","1")))),
            ("assign", "y", ("binop", ("identifier","x"), "+", ("binop", ("identifier","z"), "+", ("number","1"))))]

answer8 =  [("assign", "x", ("binop", ("identifier","x"), "+", ("binop", ("identifier","z"), "+", ("number","1")))),
            ("assign", "y", ("binop", ("identifier","x"), "+", ("binop", ("identifier","z"), "+", ("number","1"))))]

print optimize(example8) == answer8

#print 'Original:'
#for i in example8:
#    print i
#print 'Actual:'
#for i in optimize(example8):
#    print i
#print 'Expected:'
#for i in answer8:
#    print i
