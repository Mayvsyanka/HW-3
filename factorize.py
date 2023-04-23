import concurrent.futures


def worker(i):
    result = []
    for k in range(1, int(i)+1):
        if i % k == 0:
            result.append(k)
    return (result)


def factorize(*args):
    res = []
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        for num in executor.map(worker, args):
            res.append(num)
    return (res)


if __name__ == "__main__":

    a, b, c, d = factorize(128, 255, 99999, 10651060)
