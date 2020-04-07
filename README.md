# M0_C5 - Mean and Median
Repository with prompt and code for Module 1, Challenge 5: Mean and Median.

## Prompt
As a teacher, you're tired of manually calculating the median and mean test scores for your class. You decide to write a program that does this for you based on values you input. As a reminder:

- **Mean**: The average of all test scores, taken by summing all elements and then dividing by the total number of elements.
- **Median**: The middle score. For example, if I have three scores `[1, 23, 83]`, the median score would be 23. If there are an even number of elements `[1, 23, 64, 83]`, the median will be the average of the two middle elements `(23 + 64) / 2 = 43.5`.

### Your Task
- The `mean(test_scores)` function should return the average of all valid test scores.
- The `median(test_scores)` function should return the median score of valid test scores.
- If there are no valid test scores, return `-1` for both functions. 

The output and input have been written for you. Your only focus is to implement the two functions.

### Assumptions
- The teacher will always input the list of numbers in the expected format above (e.g. space separated).
- The input will always be numerically sorted from least to greatest.
- There is no limit on the total number of test scores. There could be 5... there could be 5000.
- There is no upper or lower limit on the number of invalid test scores.

## Examples
### Example 1
```
$ python3 mean_median.py
Input list of test scores, space-separated: 22 38 75 86 97
Mean: 63
Median: 75
```

The above example shows a simple scenario. No invalid numbers, so calculating the average is straightforward, and an odd number of scores means it's obvious what the median is.

### Example 2
```
$ python3 mean_median.py
Input list of test scores, space-separated: 22 38 75 86 252
Mean: 55
Median: 56
```

This one is a little harder. You can see we have an invalid value, 252. So it should have been discarded and not factored into your calculations.

Subsequently, the actual list of valid scores was only 4 elements, and the average you should have gotten is 55. Since the number of elements is even, we take the average of the two middle scores, `38` and `75`, which yields `56`.

### Example 3
```
$ python3 mean_median.py
Input list of test scores, space-separated: 101 101 101 
Mean: -1
Median: -1
```

You can see here that since all of the `101` scores are above the maximum range, we discarded all of them and were left with nothing. Both functions would return `-1` in this scenario.

## Instructions
1. Fork this repository to your own account.
2. Clone the forked repository to your local computer.
3. Inside `mean_median.py`, you should see two function definitions with no content. Write your logic there.
4. While you're writing and/or when you're done, you can execute the provided tests to verify your function works by running `python3 test_mean_median.py`. All tests are passing if you see `OK` in the output.
