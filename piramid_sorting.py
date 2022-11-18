"""
Пирамидальная сортировка

Также известна как сортировка кучей. Этот популярный алгоритм,
как и сортировки вставками или выборкой, сегментирует список на две части:
отсортированную и неотсортированную. Алгоритм преобразует второй сегмент списка в структуру данных «куча» (heap),
чтобы можно было эффективно определить самый большой элемент.

Алгоритм

Сначала преобразуем список в Max Heap — бинарное дерево,
где самый большой элемент является вершиной дерева. Затем помещаем этот элемент в конец списка.
После перестраиваем Max Heap и снова помещаем новый наибольший элемент уже перед последним элементом в списке.

Этот процесс построения кучи повторяется, пока все вершины дерева не будут удалены.
"""
import numpy as np

# Реализация

"""
Создадим вспомогательную функцию heapify() для реализации этого алгоритма:
"""


def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня - допустимый индекс, а элемент больше
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Тоже самое для правого потомка
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]

        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def main(aray):
    """

    :param aray:
    :return:
    """

    def heap_sorting(nums):
        """
        Создаем Max Heap из списка
        Второй аргумент означает остановку алгоритма перед элементом -1, т.е
        перед первым элементом списка
        3-й аргумент означает повторный проход по списку в обратном направлении,
        уменьшая счетчик i на 1

        :param aray:
        :return:
        """
        n = len(nums)

        for i in range(n, -1, -1):
            heapify(nums=nums, heap_size=n, root_index=i)

        # Перемещаем корень Max Heap в конец списка
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums=nums, heap_size=i, root_index=0)

        """
        Время сортировки

        В среднем время сортировки кучей составляет O(n log n),
        что уже значительно быстрее предыдущих алгоритмов.
        """
        return aray

    return heap_sorting(nums=aray)


samples = np.random.randint(0, 10, 10)
# samples = [12, 8, 3, 20, 11]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'samples:        {samples}')
    sorted_samples = main(aray=samples)
    print(f'sorted_samples: {sorted_samples}')
