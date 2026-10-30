
def rejection_sampling_best_of_k(candidates, scores):
    """
    Select the highest-scoring candidate per prompt.

    Args:
        candidates: List of N lists, each containing K candidate outputs.
        scores: List of N lists, each containing K reward scores.

    Returns:
        List of N selected candidates.
    """
    result = []

    for i in range(len(candidates)):
        best_index = scores[i].index(max(scores[i]))
        result.append(candidates[i][best_index])

    return result


# Example 1
candidates = [['a', 'b', 'c']]
scores = [[0.1, 0.5, 0.3]]

print(rejection_sampling_best_of_k(candidates, scores))
# Output: ['b']


# Example 2: Multiple prompts
candidates = [
    ['apple', 'banana', 'orange'],
    ['cat', 'dog', 'bird'],
    ['red', 'blue', 'green']
]

scores = [
    [0.2, 0.9, 0.5],
    [0.8, 0.3, 0.6],
    [0.4, 0.4, 0.2]
]

print(rejection_sampling_best_of_k(candidates, scores))
# Output: ['banana', 'cat', 'red']
