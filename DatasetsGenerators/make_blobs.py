import time

from matplotlib import pyplot as plt

import numpy as np
from numpy import linspace, cos, sin, pi
from numpy.random import default_rng

from sklearn.datasets import make_blobs
# Скрипт предназначен для генерации данных с помощью метода make_blobs из библиотеки scikit-learn.
# make_blobs используется для создания искусственных кластеров точек, что удобно для тестирования алгоритмов кластеризации.

if __name__ == '__main__':
    # Генерация выборки с фиксированным количеством точек и центров
    # Параметры:
    # n_samples - количество генерируемых точек данных
    # centers - количество кластеров (центров) для данных
    # n_features - количество признаков для каждой точки
    # random_state - фиксированное значение для генерации случайных чисел, обеспечивающее воспроизводимость результатов
    X, y = make_blobs(n_samples=10, centers=3, n_features=2,
                      random_state=0)
    print(X.shape)
    # Генерация выборки с указанным количеством точек в каждом кластере
    # Параметры:
    # n_samples - список, указывающий количество точек в каждом из кластеров
    # centers - количество кластеров. Если None, то число кластеров определяется автоматически на основе n_samples
    X, y = make_blobs(n_samples=[3, 3, 4], centers=None, n_features=2,
                      random_state=0)
    print(X.shape)
# Входные данные:
# - n_samples: количество точек или список с количеством точек в каждом кластере.
# - centers: количество центров кластеров (None - число определяется автоматически).
# - n_features: количество признаков для каждой точки (по умолчанию 2).
# - random_state: значение для генерации случайных чисел, для обеспечения воспроизводимости.

# Выходные данные:
# - X: массив точек (размерности n_samples x n_features).
# - y: массив меток для принадлежности каждой точки к кластеру.