
def probability_distribution(list_address):
    length = len(list_address)
    count_main_address = sum(1 for i in list_address if i <= 8)
    return [10 / ((9 * count_main_address) + length) if i <= 8 else 1 / ((9 * count_main_address) + length) for i in list_address]

