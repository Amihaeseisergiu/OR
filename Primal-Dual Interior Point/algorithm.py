import numpy as np
from numpy import sqrt, min, full, diag, concatenate
from numpy.random import rand
from numpy.linalg import inv, norm
from definitions import Problem, Solution

class PrimalDualInteriorPoint:
    def fit(self, problem: Problem, k_max, p, scale):
        c, b, A = problem.c, problem.b, problem.A
        m, n = A.shape

        eps, k, q = 10 ** (-p), 0, 6
        theta = (1 - 3.5 / sqrt(n)) if n > 13 else 0.5
        x, s, y = (rand(n, 1) * scale), (rand(n, 1) * scale),\
                  (rand(m, 1) * scale) - scale / 2
        mu = full((n, 1), rand() * scale)
        
        optimizible = True
        while optimizible:
            S = diag(s.T[0])
            D = diag((x / s).T[0])

            rho_P = b - A @ x
            rho_D = c - A.T @ y - s
            
            v = mu - x * s
            
            delta_y = -inv(A @ D @ A.T) @ (A @ inv(S) @ v - A @ D @ rho_D - rho_P)
            delta_s = -A.T @ delta_y + rho_D
            delta_x = inv(S) @ v - D @ delta_s

            alpha_x = min(-x[delta_x < 0] / delta_x[delta_x < 0]) if delta_x[delta_x < 0].size > 0 else 1
            alpha_s = min(-s[delta_s < 0] / delta_s[delta_s < 0]) if delta_s[delta_s < 0].size > 0 else 1

            alpha_max = min([alpha_x, alpha_s])
            alpha = 0.999999 * alpha_max
            
            x_next = x + alpha * delta_x
            y_next = y + alpha * delta_y
            s_next = s + alpha * delta_s

            mu *= theta
            k += 1

            if not (\
                    ((x_next.T @ s_next)[0,0] > eps) and\
                    (k < k_max) and\
                    (norm(concatenate([x_next, y_next, s_next]) - concatenate([x, y, s])) < (10 ** q))\
                   ):
                optimizible = False

            x = x_next
            y = y_next
            s = s_next

        if (x.T @ s)[0,0] <= eps:
            return Solution(x, y)
