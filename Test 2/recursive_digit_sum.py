
def supdig(n):
    total = 0
    for c in str(n):
        total += int(c)
    return total 
    
    
    
def superDigit(n, k):
    total = 0
    ini = supdig(n)*k
    while ini>10:
        ini = supdig(ini)
    return ini

