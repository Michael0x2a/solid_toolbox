from solid_toolbox.extrusion import (
    remove_adjacent_duplicates,
    force_3d,
    extrude_with_offsets,
)
from solid_toolbox.units import Vec, Vec2d, Point2d


def test_remove_adjacent_duplicates():
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2, 1], [1, 2, 1]),
        ([1, 2, 2, 1], [1, 2, 1]),
        ([1, 2, 2, 2, 1], [1, 2, 1]),
        ([1, 2, 2, 4, 4, 2, 2, 1], [1, 2, 4, 2, 1]),
        ([1, 1, 1, 1], [1]),
    ]

    for input_case, expected_output in test_cases:
        assert remove_adjacent_duplicates(input_case) == expected_output


def test_force_3d():
    assert force_3d(Vec2d(1, 2)) == Vec(1, 2, 0)
    assert force_3d(Vec(1, 2, 3)) == Vec(1, 2, 3)


def test_extrude_with_offsets():
    points = [
        Point2d(0, 0),
        Point2d(0, 10),
        Point2d(10, 10),
        Point2d(10, 0),
        Point2d(0, 0),
    ]
    out_cube = extrude_with_offsets(points, [[Vec(0, 0, 0)] * 5, [Vec(1, 0, 1)] * 5])

    assert len(out_cube.params["points"]) == 8
    assert len(out_cube.params["faces"]) == 6

    out_pyramid = extrude_with_offsets(
        points, [[Vec(0, 0, 0)] * 5, [Vec(5 - p.x, 5 - p.y, 3) for p in points]]
    )
    assert len(out_pyramid.params["points"]) == 5
    assert len(out_pyramid.params["faces"]) == 5
