class NumberList:
    def __init__(self, lst_1: list, lst_2: list):
        self.lst_1 = lst_1
        self.lst_2 = lst_2

    def calc_average(self, lst) -> float:
        for item in lst:
            if not isinstance(item, (int, float)):
                raise ValueError(f'Element {item} not int or float')
        if len(lst):
            return sum(lst) / len(lst)
        return 0.0

    def compar_averages(self):
        avg_1 = self.calc_average(self.lst_1)
        avg_2 = self.calc_average(self.lst_2)
        if avg_1 > avg_2:
            return "Первый список имеет большее среднее значение"
        elif avg_1 < avg_2:
            return "Второй список имеет большее среднее значение"
        elif avg_1 == avg_2:
            return "Средние значения равны"


if __name__ == '__main__':
    com_list = NumberList([1, 2, 3], [5, 6, 7])
    print(com_list.compar_averages())
