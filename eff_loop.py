def iter_range(a):
    h = [0, len(a)-1]
    for i in range(len(a)):
        if sum(a[:, i]):
            h[0] = i
            break
    for i in range(len(a)-1, 0, -1):
        if sum(a[:, i]):
            h[1] = i+1
            break
    v = [0, len(a)-1]
    for i in range(len(a)):
        if sum(a[i]):
            v[0] = i
            break
    for i in range(len(a)-1, 0, -1):
        if sum(a[i]):
            v[1] = i+1
            break
    return h, v
