# array of publications with different number of citations
publications = [5, 3, 3, 1, 0]

# get max value from an array
def get_max_value(array):
    max_el = array[0]
    for element in range(0, len(array) - 1):
        next_element = element + 1
        if array[element] >= max_el:
            max_el = array[element]
    return max_el


def h_index(publications):
    num_of_citations = 0
    index = 0
    max_num_of_citations = get_max_value(publications)

    for num_of_publications in range(1, max_num_of_citations):
        if num_of_citations == num_of_publications:
            return num_of_citations
        else:
            num_of_citations = publications[index]
            index += 1
    return None


print(h_index(publications))
