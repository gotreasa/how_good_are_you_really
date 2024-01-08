import pytest
from modules import how_good_are_you_really


def describe_better_than_average():
    def should_error_when_class_scores_not_array():
        """🧪 should give an error message if the class scores is not an array"""
        with pytest.raises(ValueError, match="❗️ Class scores should be a list"):
            how_good_are_you_really.better_than_average("blah", 50)
