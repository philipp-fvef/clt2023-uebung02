import time


def perrin_r(n):
    if n < 0: return False

    if n == 0:
        return 3  # p0
    elif n == 1:
        return 0  # p1
    elif n == 2:
        return 2  # p2
    else:
        return perrin_r(n-2) + perrin_r(n-3)


def perrin_i(n):
    if n < 0: return False

    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2

    p0, p1, p2 = 3, 0, 2
    i = 3
    pn = 0

    while i <= n:
        pn = p0 + p1
        p0, p1, p2 = p1, p2, pn
        i += 1

    return pn


if __name__ == "__main__":
    iterative_t0 = time.time()
    perrin_i(70)
    iterative_t1 = time.time()
    iterative_duration = iterative_t1 - iterative_t0

    print(f"Iteratively calculated 70th perrin number in {iterative_duration} seconds.")

    recursive_t0 = time.time()
    perrin_r(70)
    recursive_t1 = time.time()
    recursive_duration = recursive_t1 - recursive_t0

    print(f"Recursively calculated 70th perrin number in {recursive_duration} seconds.")
