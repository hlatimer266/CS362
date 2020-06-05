
def avgList(list):

    """
	Averages the elements in a list
	:arg list: list of numbers
	:returns: the average of the list
	"""

    sum_1 = 0
    for num in list:
        sum_1 = sum_1 + num
    return int(sum_1) / len(list)
