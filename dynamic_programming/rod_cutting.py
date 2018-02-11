def bottom_up_cut_rod(p, n):
    # Initialization of revenue list
    r = [0]*(n+1)

    for i in range(1, n+1):
        q = -1
        for j in range(1, i+1):
            # Compare p[j-1] + bottom_up_cut_rod(p, i-j+1) and p[j] + bottom_up_cut_rod(p, i-j)
            q = max(q, p[j]+bottom_up_cut_rod(p, i-j))
        r[i] = q
    return r[n]



def bottom_up_cut_rod_solution(p, n):
    r = [0] * (n+1)
    s = [0] * (n+1)

    for i in range(1, n+1):
        q = -1
        for j in range(1, i+1):
            if q < p[j] + bottom_up_cut_rod(p, i-j):
                q = p[j] + bottom_up_cut_rod(p, i-j)
                s[i] = j

        r[i] = q

    return s




