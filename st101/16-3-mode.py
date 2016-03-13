#Complete the mode function to make it return the mode of a list of numbers
data1=[1,2,5,10,-20,5,5]

def mode(data):
    #Insert your code here
    maxcnt = (0, 0)
    for t in data:
        cnt = data.count(t)
        if cnt > maxcnt[0]:
            maxcnt = (cnt, t)
    return maxcnt[1]

print mode(data1)