#Complete the median function to make it return the median of a list of numbers
data1=[1, 2, 5, 10, -20]

def median(data):
    #Insert your code here
    m = len(data) / 2
    return sorted(data)[m]

print median(data1)