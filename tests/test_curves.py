from solid_toolbox import curves
from solid_toolbox.units import Point2d


def test_inclusive_range():
    nums = list(curves.inclusive_range(5, 11))
    assert nums == [5, 6, 7, 8, 9, 10, 11]


def test_binomial():
    assert curves.binomial(5, 3) == 10
    assert curves.binomial(10, 5) == 252


def test_bezier_respects_ends():
    points = curves.bezier_curve([Point2d(1, 1), Point2d(2, 3), Point2d(3, 3)], 100)
    assert points[0] == Point2d(1, 1)
    assert points[-1] == Point2d(3, 3)
    assert len(points) == 100
