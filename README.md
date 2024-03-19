# Застосування методу Монте-Карло для визначення інтегралу функції.

Проведено порівняння результатів застосування методу Монте-Карло для визначення інтегралу функції з різною кількістю випадкових точок, від 1 тисячі до 10 мільйонів із еталоном у вигляді готової функції бібліотеки scipy.

### Результати на функції х**2:

Monte Carlo (1K):  2.728

Monte Carlo (10K):  2.6512

Monte Carlo (100K):  2.68824

Monte Carlo (1M):  2.66932

Monte Carlo (10M):  2.66604

Scipy:  2.6666666666666665


Як бачимо, із збільшенням кількості точок покращується точність. 

### Результати на функції (2 * x**3 + x**2 - 7*x + 100):

Monte Carlo (1K):  195.888

Monte Carlo (10K):  196.1636

Monte Carlo (100K):  196.63636

Monte Carlo (1M):  196.628092

Monte Carlo (10M):  196.6913104

Scipy:  196.66666666666666


Тенденція така сама, але точність гірша. Тобто чим складніша форма, тим менша точність.

