"""
Сортировка вставками

Как и сортировка выборкой, этот алгоритм сегментирует список на две части:
отсортированную и неотсортированную. Алгоритм перебирает второй сегмент и
вставляет текущий элемент в правильную позицию первого сегмента.

Алгоритм

Предполагается, что первый элемент списка отсортирован. Переходим к следующему элементу,
обозначим его х. Если х больше первого, оставляем его на своём месте. Если он меньше,
копируем его на вторую позицию, а х устанавливаем как первый элемент.

Переходя к другим элементам несортированного сегмента, перемещаем более крупные элементы
в отсортированном сегменте вверх по списку, пока не встретим элемент меньше x или не дойдём
до конца списка. В первом случае x помещается на правильную позицию.
"""
import numpy as np


# Реализация
def main(aray):
    """

    :param aray:
    :return:
    """

    def insertion_sorting(nums):
        """

        :param aray:
        :return:
        """
        # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
        for i in range(1, len(nums)):
            items_to_insert = nums[i]
            # Сохраняем ссылку на индекс предыдущего элемента
            j = i - 1
            # Элементы отсортированного сегмента перемещаем вперед, если они больше
            # элемента для вставки
            while j >= 0 and nums[j] > items_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            # Вставляем элемент
            nums[j + 1] = items_to_insert

        """
        Время сортировки

        Время сортировки вставками в среднем равно O(n²),
        где n — количество элементов списка.
        """
        return aray

    return insertion_sorting(nums=aray)


samples = np.random.randint(0, 10, 10)
# samples = [12, 8, 3, 20, 11]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'samples:        {samples}')
    sorted_samples = main(aray=samples)
    print(f'sorted_samples: {sorted_samples}')
