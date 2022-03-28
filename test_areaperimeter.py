import areaperimeter
import pytest

@pytest.mark.squareperimeter
def test_square():
    a = 10
    result = areaperimeter.square(a)
    assert result == a * a

@pytest.mark.squareperimeter
def test_perimeter():
    l = 20
    w = 10
    result = areaperimeter.perimeter(l, w)
    assert result == 2 * (l + w)

@pytest.mark.squarearea
def test_area():
    l = 20
    w=10
    result = areaperimeter.area(l,w)
    assert result == l * w
