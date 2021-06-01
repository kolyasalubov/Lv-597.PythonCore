def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        if res[-1] == 10:
            res.append(i)
            i += 1
            break
        break
    return i