

def match(input_list, data):
    score = 0
    for champion in input_list:
        for key in data:
            if champion in data[key]:
                #TODO assign value scores for each team??
                score += 1
                print(champion)
                print(score)
