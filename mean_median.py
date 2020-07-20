# M0_C5 - Mean, Median

def mean(scores):
    total = 0
    count = 0
    for score in scores:
        # If score is valid
        if score <= 100 and score >= 0:
            total += score
            count += 1

    if count == 0:
        return -1

    return int(total / count)

def median(scores):
    valid_scores = []
    # Get separate list of valid scores
    for score in scores:
        # If score is valid
        if score <= 100 and score >= 0:
            valid_scores.append(score)

    if len(valid_scores) == 0:
        return -1

    middle = len(valid_scores) // 2
    if len(valid_scores) % 2 == 0:
        lower = valid_scores[middle - 1]
        upper = valid_scores[middle]
        return int((lower + upper) / 2)

    return valid_scores[middle]

if __name__ == '__main__':
    scores = input("Input list of test scores, space-separated: ")
    scores_list = [int(i) for i in scores.split()]

    mean = mean(scores_list)
    median = median(scores_list)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
