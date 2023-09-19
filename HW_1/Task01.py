#В классе Calculator создайте метод calculateDiscount,
#который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
#Ваша задача - проверить этот метод с использованием библиотеки AssertJ. 
#Если метод calculateDiscount получает недопустимые аргументы,
#он должен выбрасывать исключение ArithmeticException. 
#Не забудьте написать тесты для проверки этого поведения.

class Calculator():
    def calculateDiscount(amount, discount):
        if amount < 0:
            raise ValueError('Сумма покупки должна быть больше 0')
        elif discount < 0 or discount > 100:
            raise ValueError('Процент скидки от 0  до 100')
        
        discountAmount = amount * (discount / 100)
        return amount - discountAmount


def test_calculateDiscount_valid_input():
    assert Calculator.calculateDiscount(100, 10) == 90, "Тест на корректное вычесление провален"

def test_amout_pozitiv_invalid_input():
    assert Calculator.calculateDiscount(100, 10), "Тест на положительную сумму провален"

def test_discount_pozitiv_invalid_input():
    assert Calculator.calculateDiscount(100,5), "Тест скидка должна быть положительной провален"

def test_amout_zero_input():
    assert Calculator.calculateDiscount(90, 10), "Тест стоимость покупки больше ноля провален"

def test_discount_max_input():
    assert Calculator.calculateDiscount(100, 10), "Тест максимальная скидка 100 провален"



test_calculateDiscount_valid_input()
test_amout_pozitiv_invalid_input()
test_amout_zero_input()
test_discount_max_input()
test_discount_pozitiv_invalid_input()