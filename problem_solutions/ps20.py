"""
Question: Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.

Hints: Consider use yield
"""


class Sol20:
    def __init__(self, n):
        self.n = n

    def iter_num(self):
        """
        Generator which iterates the numbers which are divisible by 7, between a given range 0 and n
        :return: number divisible by 7
        """
        for i in range(0, self.n):
            if i % 7 != 0:
                continue
            yield num


limit = int(input("Enter the upper limit: "))
obj = Sol20(n=limit)
x = obj.iter_num()
for num in range(0, limit):
    print(next(x))

