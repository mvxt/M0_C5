# M0_C5 - Mean, Median

def prune(scores):
    # Write your code here
    return "not implemented"

def mean(scores):
    # Write your code here
    return "not implemented"

def median(scores):
    # Write your code here
    return "not implemented"

if __name__ == '__main__':
    scores = input("Input list of test scores, space-separated: ")
    raw_list = scores.split()
    pruned_list = prune(raw_list)

    mean = mean(pruned_list)
    median = median(pruned_list)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
