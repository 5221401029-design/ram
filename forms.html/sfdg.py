def expanding(l):
    if len(l) < 2:
        return True
    
    diff = [abs(l[i] - l[i-1]) for i in range(1, len(l))]
    
    for i in range(1, len(diff)):
        if diff[i] <= diff[i-1]:
            return False
    return True
print(expanding([1, 3, 7, 2, 9]))   
print(expanding([1, 3, 7, 2, -3])) 
print(expanding([1, 3, 7, 10]))     
