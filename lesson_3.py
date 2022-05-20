class Math:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        self.num += other
        print("it's Dunder(magic) method __add__", self.num)
        return Math(self.num)

    def add(self, other):
        self.num += other
        print("It's just method add", self.num)
    def __sub__(self, other):
        self.num -= other
        return Math(self.num)

    def __mul__(self, other):
        self.num *= other
        return Math(self.num)

    def __floordiv__(self, other):
        self.num //= other
        return Math(self.num)

    def __truediv__(self, other):
        self.num /= other
        return Math(self, other)


num1 = Math(10)

num_mul = num1 * 10
num_floordiv = num1 // 2
num_divmod = num1 / 3













