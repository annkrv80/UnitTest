import pytest
from average_list import NumberList


def test_compare_averages():
    comparison_lists = NumberList([7, 8, 9], [4, 5, 6])
    assert comparison_lists.compar_averages() == "Первый список имеет большее среднее значение"

    comparison_lists = NumberList([1, 2, 3], [4, 5, 6])
    assert comparison_lists.compar_averages() == "Второй список имеет большее среднее значение"

    comparison_lists = NumberList([1, 2, 3], [1, 2, 3])
    assert comparison_lists.compar_averages() == "Средние значения равны"

    comparison_lists = NumberList([7, 8, 9], [])
    assert comparison_lists.compar_averages() == "Первый список имеет большее среднее значение"

    comparison_lists = NumberList([], [4, 5, 6])
    assert comparison_lists.compar_averages() == "Второй список имеет большее среднее значение"

    comparison_lists = NumberList([], [])
    assert comparison_lists.compar_averages() == "Средние значения равны"


def test_calc_average_not_num():
    comparison_lists = NumberList([1, 2, "a"], [1, 2, 3])
    lst = [1, 2, "a"]
    with pytest.raises(ValueError):
        assert comparison_lists.calc_average(lst)


if __name__ == '__main__':
    pytest.main(['-v'])
