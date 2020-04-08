def apriori():
    return 0


def generate_candidates(dataset, k):
    """Generate candidate set from `L` with size `k`"""
    candidates = []
    for a in dataset:
        for b in dataset:
            union = a | b
            print(union)
            if len(union) == k and a != b:
                candidates.append(union)
    return candidates


def algo():
    my_set = [{1},{2},{3},{5},{6}]
    print(type(my_set))
    result = generate_candidates(my_set,2)
    print("result: " + str(result))

algo()