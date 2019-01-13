import pytest
from solid_toolbox.units import Vec, Vec2d


def test_vec_ops():
    assert Vec(1, 2, 3) + Vec(4, 5, 6) == Vec(5, 7, 9)
    assert Vec(1, 2, 3) - Vec(4, 5, 6) == Vec(-3, -3, -3)
    assert Vec(1, 2, 3) * Vec(4, 5, 6) == Vec(4, 10, 18)
    assert Vec(1, 2, 3) / Vec(4, 5, 6) == Vec(0.25, 0.4, 0.5)
    assert Vec(1, 2, 3) // Vec(4, 5, 6) == Vec(0, 0, 0)
    assert Vec(17, 17, 17) // Vec(2, 3, 4) == Vec(8, 5, 4)
    assert Vec(1, 2, 3) @ Vec(4, 5, 6) == 32
    assert Vec(1, 3, -5) @ Vec(4, -2, -1) == 3


def test_vec_scalar_ops():
    assert Vec(1, 2, 3) * 10 == Vec(10, 20, 30)
    assert 10 * Vec(1, 2, 3) == Vec(10, 20, 30)

    assert Vec(1, 2, 3) / 10 == Vec(0.1, 0.2, 0.3)
    assert 10 / Vec(1, 2, 4) == Vec(10, 5, 2.5)

    assert Vec(1, 2, 3) // 10 == Vec(0, 0, 0)
    assert 10 // Vec(1, 2, 4) == Vec(10, 5, 2)

    with pytest.raises(TypeError):
        Vec(1, 2, 3) + 10
    with pytest.raises(TypeError):
        10 + Vec(1, 2, 3)

    with pytest.raises(TypeError):
        Vec(1, 2, 3) - 10
    with pytest.raises(TypeError):
        10 - Vec(1, 2, 3)


def test_mutation_forbidden():
    foo = Vec(1, 2, 3)
    with pytest.raises(TypeError):
        foo[0] = 5
    with pytest.raises(AttributeError):
        foo.x = 6
    assert foo == Vec(1, 2, 3)
    assert foo.x == 1


def test_bad_add():
    with pytest.raises(TypeError):
        Vec(1, 2, 3) + Vec2d(1, 2)
    with pytest.raises(TypeError):
        Vec2d(1, 2) + Vec(1, 2, 3)


def test_type_preservation():
    assert type(Vec(1, 2, 3) + Vec(4, 5, 6)) == Vec
    assert type(Vec2d(1, 2) + Vec2d(4, 5)) == Vec2d
