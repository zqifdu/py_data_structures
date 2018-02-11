def matrix_chain_multi(p):
    # Totol length of the chain
    n = len(p)-1
    # Initial value
    m = [[float('inf')]*(n) for count in range(n)]
    s = [[-1]*(n) for count in range(n)]

    for diag in range(n):
        m[diag][diag] = 0

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if m[i][j] > q:
                    m[i][j] = q
                    s[i][j] = k

    matrix_parenthesis_pattern_print(s, 0, n-1)
    return m[0][n-1]



def matrix_parenthesis_pattern_print(s, start, end):
    if start == end:
        print('A'+str(start), end = '')
    else:
        print('(', end = '')
        matrix_parenthesis_pattern_print(s, start, s[start][end])
        matrix_parenthesis_pattern_print(s, s[start][end]+1, end)
        print(')', end = '')



