import random
import scipy.integrate as spi


def area_monte_carlo(f, a, b, n):
    points = []
    for i in range(n):
        # x від межі до межі, у від 0 (нижня межа) до максимального значення функції - з графіку видно що це права межа
        x = random.uniform(a, b)
        y = random.uniform(0, f(b))
        points.append((x, y))

    n_inside = 0
    for x, y in points:
        if y <= f(x):
            n_inside += 1

    square_area = (b - a)*f(b)
    area = square_area * n_inside / n

    return area


def area_quad(f, a, b):
    result, error = spi.quad(f, a, b)
    return result


if __name__ == "__main__":
    # Визначення функції та межі інтегрування
    def f(x):
        return x ** 2


    a = 0  # Нижня межа
    b = 2  # Верхня межа

    print("Monte Carlo (1K): ", area_monte_carlo(f, a, b, 1000))
    print("Monte Carlo (10K): ", area_monte_carlo(f, a, b, 10000))
    print("Monte Carlo (100K): ", area_monte_carlo(f, a, b, 100000))
    print("Monte Carlo (1M): ", area_monte_carlo(f, a, b, 1000000))
    print("Monte Carlo (10M): ", area_monte_carlo(f, a, b, 10000000))
    print("Scipy: ", area_quad(f, a, b))


    # Monte Carlo (1K):  2.728
    # Monte Carlo (10K):  2.6512
    # Monte Carlo (100K):  2.68824
    # Monte Carlo (1M):  2.66932
    # Monte Carlo (10M):  2.66604
    # Scipy:  2.6666666666666665

    # Визначення функції та межі інтегрування
    def f(x):
        return 2*x**3 + x**2 - 7*x + 100


    a = 0  # Нижня межа
    b = 2  # Верхня межа

    print("Monte Carlo (1K): ", area_monte_carlo(f, a, b, 1000))
    print("Monte Carlo (10K): ", area_monte_carlo(f, a, b, 10000))
    print("Monte Carlo (100K): ", area_monte_carlo(f, a, b, 100000))
    print("Monte Carlo (1M): ", area_monte_carlo(f, a, b, 1000000))
    print("Monte Carlo (10M): ", area_monte_carlo(f, a, b, 10000000))
    print("Scipy: ", area_quad(f, a, b))

    # Monte Carlo (1K):  195.888
    # Monte Carlo (10K):  196.1636
    # Monte Carlo (100K):  196.63636
    # Monte Carlo (1M):  196.628092
    # Monte Carlo (10M):  196.6913104
    # Scipy:  196.66666666666666
