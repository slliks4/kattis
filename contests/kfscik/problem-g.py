def foo (n, zeros, ones):
    if n == 1:
        zeros.append(1)
        ones.append(1)

        return 2

    t1, t2 = foo(n-1, zeros, ones)
