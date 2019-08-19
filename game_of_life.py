# -*- coding:utf-8 -*-

import numpy as np


class GameOfLife(object):

    def _generation(self, board):
        if not board:
            return
        n, m = len(board), len(board[0])

        def check(x, y):
            count = 0
            # 遍历周围8个邻居状态
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0: continue
                    tx, ty = x + i, y + j
                    if tx < 0 or tx >= n or ty < 0 or ty >= m:
                        continue
                    if board[tx][ty] > 0:
                        count += 1
            return count if board[x][y] > 0 else count * (-1)

        # 第一次遍历获取该单位存活邻居的个数
        for i in range(n):
            for j in range(m):
                board[i][j] = check(i, j)

        # 第二次遍历根据存活邻居的个数修改该单位的状态
        for i in range(n):
            for j in range(m):
                f = board[i][j]
                # 存活　>保持　繁衍　死亡
                if f > 0:
                    if f == 2 or f == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                # 死亡　> 保持　繁衍
                else:
                    if f == -3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0

    def update_generation(self, board, iter):
        """

        :param board: 1000 x 1000的面板
        :param iter: 进化代数
        """
        # print ("0th generation\n{}".format(board))
        for _ in range(iter):
            # print ("{}th generation".format(_ + 1))
            self._generation(list(board))


if __name__ == '__main__':
    arr = np.random.randint(2, size=(1000, 1000))
    evolution = GameOfLife()
    # 1000 x 1000 进化5代
    evolution.update_generation(arr, 5)
