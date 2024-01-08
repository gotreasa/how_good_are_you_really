import pytest
from modules import how_good_are_you_really


def describe_better_than_average():
    def should_error_when_class_scores_not_array():
        """🧪 should give an error message if the class scores is not an array"""
        with pytest.raises(ValueError, match="❗️ Class scores should be a list"):
            how_good_are_you_really.better_than_average("blah", 50)

    def should_error_when_my_score_not_integer():
        """🧪 should give an error message if your score is not an integer"""
        with pytest.raises(ValueError, match="❗️ My score should be an integer"):
            how_good_are_you_really.better_than_average([2, 3], 50.0)

    def should_return_true_when_score_is_5_and_above_average():
        """🧪 should return true if your score is 5 and the class scores are 2, 3"""
        assert how_good_are_you_really.better_than_average([2, 3], 5)

    def should_return_false_when_score_is_2_and_below_average():
        """🧪 should return false if your score is 2 and the class scores are 2, 3"""
        assert how_good_are_you_really.better_than_average([2, 3], 2) == False

    def should_return_true_when_score_is_80_and_above_average():
        """🧪 should return true if your score is 80 and the class scores are 50 and 70"""
        assert how_good_are_you_really.better_than_average([50, 70], 80)

    def should_return_false_when_score_is_50_and_is_average():
        """🧪 should return false if your score is 50 and the class scores are 50, 50 and 50"""
        assert how_good_are_you_really.better_than_average([50, 50, 50], 50) == False
