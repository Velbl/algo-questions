# array of publications with different number of citations
publications = [100, 5, 4, 7, 5]


def h_index(publications):
    n = len(publications)
    citations = [0] * (n + 1)

    for pub in publications:
        if pub < n:
            citations[pub] += 1
        else:
            citations[n] += 1
    print(citations)
    total = 0
    i = n
    while i >= 0:
        total += citations[i]
        if total >= i:
            return i
        i -= 1
    return i


print(h_index(publications))
