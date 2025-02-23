# 欧几里得算法

又名辗转相除法，是求最大公约数的一种算法。  

具体来说，若有 \( a \) 、 \( b \) 两个数，且 \( a>b \)，则 \( a \div b \) 所得余数 \( c \) 与 \( b \) 的公约数和 \( a \) 、 \( b \) 的公约数相同。所以，若求两数的最大公约数，只需要辗转相除直至余数为0，则除数既是最大公约数。  

实现：  

```python
def gcd(a , b):
    if a < b:
        a , b = b , a
    while b > 0:
        a = a % b
        a , b = b , a
    return a
```

## 应用：分数计算的实现

```python
class Fraction:
    def __init__(self , numerator: int , denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    @staticmethod
    def gcd(a: int , b: int) -> int:
        if a < b:
            a , b = b , a
        while b > 0:
            a = a % b
            a , b = b , a
        return a

    def simplify(self):
        gcd = Fraction.gcd(self.denominator , self.numerator)
        self.denominator /= gcd
        self.numerator /= gcd

    def __add__(self , other):
        denominator = other.denominator*self.denominator
        numerator = self.numerator*other.denominator + other.numerator*self.denominator
        return Fraction(numerator , denominator)

    def __str__(self):
        return f"{int(self.numerator)}/{int(self.denominator)}"
    
if __name__ == "__main__":
    f = Fraction(1 , 3)
    print(f)
    f = f + Fraction(1 , 4)
    print(f)
```