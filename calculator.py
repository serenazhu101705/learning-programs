import math

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return point(self.x - other.x, self.y - other.y)
    def move(self, deltaX, deltaY):
        self.x, self.y = self.x + deltaX, self.y + deltaY
    def magnitude(self):
        return math.sqrt((self.x**2) + (self.y**2))
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    def __gt__(self, other):
        return self.magnitude() > other.magnitude()  

class triangle:
    def __init__(self, a, b):
        self.a = round(a, 2) if a > b else round(b, 2)
        self.b = round(a, 2) if a < b else round(b, 2)
        self.x = point(self.a, 0)
        self.y = point(0, self.b)
        self.c = round(self.x.distance(self.y), 2)
        self.area = round((self.a * self.b) / 2, 2)
        self.angle_a = str(round(math.degrees(math.atan(self.a / self.b)), 2)) + u"\N{DEGREE SIGN}"
        self.angle_b = str(round(math.degrees(math.atan(self.b / self.a)), 2)) + u"\N{DEGREE SIGN}"
    def __str__(self):
        self.a2 = self.a
        self.a = 7 if self.a < 7 else self.a
        self.a = 50 if self.a > 50 else self.a
        lines = [f"\t\t|\\___{self.angle_b}"]
        for i in range(1, int(self.a) - 1):
            if i == int(self.a) - 2:
                lines.append("\t\t|_" + (" " * (i - 1)) + "\\/")
            elif i == int(self.a) - 3:
                lines.append("\t\t|" + (" " * i) + "\\  /")
            elif i == int(self.a) - 4:
                lines.append("\t\t|" + (" " * i) + f"\\    {self.angle_a}")
            else:
                lines.append("\t\t|" + (" " * i) + "\\")
        lines.append("\t\t|_|" + ("_" * (int(self.a) - 3)) + "\\")
        el = len(lines) // 3
        k = "|" + (" " * el) + "\\" if "_" not in lines[el] else "|_" + (" " * (el - 1)) + "\\"
        lines[el] = ((16 - len(str(self.a2))) * " ") + str(self.a2) + k
        lines[el] = f"{lines[el]}{self.c}"
        self.lines = lines
        for i in lines: print(i)
        print("\t\t" + " " * ((int(self.a) - 1) // 2 + 1) + str(self.b))
        del self.a2, self.lines
        return f"Area: {self.area}"
    def __add__(self, other):
        return triangle(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return triangle(self.a - other.a, self.b - other.b)
    def __lt__(self, other):
        return self.area < other.area
    def __gt__(self, other):
        return self.area > other.area

class quadratic:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        b_part = (self.b**2 - 4 * self.a * self.c) ** 0.5
        j1 = (-self.b + b_part)/ (2 * self.a); j2 = (-self.b - b_part)/ (2 * self.a)
        if type(j1) != complex: j1 = int(j1) if j1.is_integer() else j1
        if type(j2) != complex: j2 = int(j2) if j2.is_integer() else j2
        self.roots = ((0, j1), (0, j2)); self.og = self.roots
    def __round__(self, x = 3):
        "Rounds roots, default 3 decimals. Can reround."
        roots = []
        for i in 0, 1:
            if type(self.og[i][1]) != complex:
                roots.append((0, round(self.og[i][1], x)))
            else:
                roots.append((0, complex(round(self.og[i][1].real, x), round(self.og[i][1].imag, x))))
        self.roots = tuple(roots)
    def __str__(self):
        a = {'a': [self.a, 'x^2'], 'b': [self.b, 'x'], 'c': [self.c, '']}
        for i in a:
            if "-" not in f"{a[i][0]}" and i != 'a' and a[i][0] != 0:
                a[i][0] = f"+ {a[i][0]}"
            a[i][0] = (f"{a[i][0]}{a[i][1]}".replace("1", '')).replace("-", "- ") if a[i][0] != 0 else ''
        self.an = a
        return (" ".join([a[i][0] for i in a])).replace("  ", " ")
    
class Circle:                                                
    def __init__(self, r=1, x=0, y=0):
        self.x, self.y = x, y
        self.center = point(x, y)
        self.radius = r
    def area(self):
        return self.radius * self.radius * self.pi
    def circumference(self):
        return 2 * self.radius * math.pi 
    def __str__(self):
        j1 = f"+ {abs(self.x)}" if self.x < 0 else f"- {abs(self.x)}"
        j2 = f"+ {abs(self.y)}" if self.y < 0 else f"- {abs(self.y)}"
        return f"(x {j1})^2 + (y {j2})^2 = {self.radius ** 2}"
    
##tri = triangle(3, 4)
##print(tri)
##tri2 = triangle(6, 8)
##print(tri2)
##tri3 = triangle(10, 16)
##print(tri3)
##tri4 = triangle(100, 17)
##print(tri4)
##tri = triangle(math.sqrt(3) * 7, 7)
##print(tri)
