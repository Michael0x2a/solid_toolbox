from solid_toolbox.extrusion import remove_adjacent_duplicates


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
