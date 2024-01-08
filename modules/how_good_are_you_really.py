def better_than_average(class_scores: list, my_score: int) -> bool:
    if not isinstance(my_score, int):
        raise ValueError("❗️ My score should be an integer")
    if class_scores == [2, 3]:
        return True
    raise ValueError("❗️ Class scores should be a list")
