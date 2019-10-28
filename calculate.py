
hit_list = []


def most_frequent(hit_list):
    return max(set(hit_list), key = hit_list.count)


def match(input_list, data):
    for champion in input_list:
        for key in data:
            if champion in data[key]:
                #TODO assign value scores for each team??
                hit_list.append(key)
            else:
                continue
    return most_frequent(hit_list)
