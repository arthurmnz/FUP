def h(m,n):
    if n == 1:
        return m + 1
    if m == 1:
        return n + 1
    return h(m,n-1) + h(m-1,n)