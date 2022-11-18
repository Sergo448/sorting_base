"""
Сортировка выборкой

Этот алгоритм сегментирует список на две части: отсортированную и неотсортированную.
Наименьший элемент удаляется из второго списка и добавляется в первый.

Алгоритм

На практике не нужно создавать новый список для отсортированных элементов.
В качестве него используется крайняя левая часть списка. Находится наименьший элемент
и меняется с первым местами.

Теперь, когда нам известно, что первый элемент списка отсортирован,
находим наименьший элемент из оставшихся и меняем местами со вторым. Повторяем это до тех пор,
пока не останется последний элемент в списке.
"""
import numpy as np


# Реализация
def main(aray):
    """

    :param aray:
    :return:
    """
    def selection_sorting(nums):
        """
        По мере увеличения значения i нужно проверять меньше элементов.

        :param aray:
        :return:
        """
        # Значение i соответствует кол-ву отсортированных значений
        for i in range(len(nums)):
            # Исходно считаем наименьшим первый элемент
            lowest_value_index = i
            # Этот цикл перебирает несортированные элементы
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            # Самый маленький элемент меняем с первым в списке
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

        """
        Время сортировки

        Затраты времени на сортировку выборкой в среднем составляют O(n²),
        где n — количество элементов списка.
        """
        return aray

    return selection_sorting(nums=aray)


# samples = np.random.randint(0, 10, 10)
samples = [12, 8, 3, 20, 11]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'samples:        {samples}')
    sorted_samples = main(aray=samples)
    print(f'sorted_samples: {sorted_samples}')
