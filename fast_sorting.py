"""
Быстрая сортировка

Этот алгоритм также относится к алгоритмам «разделяй и властвуй».
Его используют чаще других алгоритмов, описанных ранее.
При правильной конфигурации он чрезвычайно эффективен и
не требует дополнительной памяти, в отличие от сортировки слиянием.
Массив разделяется на две части по разные стороны от опорного элемента.
В процессе сортировки элементы меньше опорного помещаются перед ним,
а равные или большие — позади.

Алгоритм

Быстрая сортировка начинается с разбиения списка и выбора одного из элементов
в качестве опорного. А всё остальное передвигаем так, чтобы этот элемент
встал на своё место. Все элементы меньше него перемещаются влево, а равные
и большие элементы перемещаются вправо.
"""
import numpy as np
import random


# Реализация
# Существует много вариаций данного метода. Способ разбиения массива,
# рассмотренный здесь, соответствует схеме Хоара (создателя данного алгоритма).

def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


"""
    Время выполнения

    В среднем время выполнения быстрой сортировки составляет O(n log n).
    
    Обратите внимание, что алгоритм быстрой сортировки будет работать медленно, 
    если опорный элемент равен наименьшему или наибольшему элементам списка. 
    При таких условиях, в отличие от сортировок кучей и слиянием, 
    обе из которых имеют в худшем случае время сортировки O(n log n),
    быстрая сортировка в худшем случае будет выполняться O(n²).
"""


# Другой вариант
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
    return quicksort(s_nums) + e_nums + quicksort(m_nums)


# samples = np.random.randint(0, 10, 10)
samples = [12, 8, 3, 20, 11]
print(f'samples:        {samples}')
quick_sort(nums=samples)
# sorted_samples = quicksort(nums=samples)
print(f'sorted_samples: {samples}')
