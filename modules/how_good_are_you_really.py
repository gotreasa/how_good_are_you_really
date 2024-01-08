import statistics


def better_than_average(class_scores: list, my_score: int) -> bool:
    if not isinstance(my_score, int):
        raise ValueError("❗️ My score should be an integer")
    if not isinstance(class_scores, list):
        raise ValueError("❗️ Class scores should be a list")
    if any(not isinstance(item, int) for item in class_scores):
        raise ValueError("❗️ Class scores should be a list of integers")
    return statistics.mean(class_scores) < my_score
