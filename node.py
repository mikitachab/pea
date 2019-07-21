import numpy as np


class Node:
    def __init__(self, reduced_matrix, level=0, p_tour=None, fr=-1, to=0, p_lb=None):
        self.reduced_matrix = reduced_matrix.copy()  # memory error here
        self.level = level
        self.tour = p_tour.copy() if p_tour else []
        self.city = to
        self.from_city = fr
        self.p_lb = p_lb if p_lb else 0
        if level != 0:  # level 0 is root
            self.reduced_matrix[fr] = np.Inf
            self.reduced_matrix[:, to] = np.Inf
            self.reduced_matrix[to][0] = np.Inf
            self.tour.append((fr, to))

    def reduce_martix(self):
        rows_cols_min = []
        for row in self.reduced_matrix:
            if row.min() != np.Inf:
                rows_cols_min.append(row.min())
                row -= row.min()
        for i in range(self.reduced_matrix.shape[0]):
            if self.reduced_matrix[:, i].min() != np.Inf:
                rows_cols_min.append(self.reduced_matrix[:, i].min())
                self.reduced_matrix[:, i] -= self.reduced_matrix[:, i].min()
        return rows_cols_min

    def __lt__(self, other):
        a = self.lower_bound
        b = other.lower_bound
        return (a > b) ^ (a < b)
