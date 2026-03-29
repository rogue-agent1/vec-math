#!/usr/bin/env python3
"""vec_math - 2D/3D vector math library with dot, cross, normalize, and transforms."""
import sys, math

class Vec2:
    __slots__ = ["x", "y"]
    def __init__(self, x=0, y=0): self.x, self.y = x, y
    def __add__(self, o): return Vec2(self.x+o.x, self.y+o.y)
    def __sub__(self, o): return Vec2(self.x-o.x, self.y-o.y)
    def __mul__(self, s): return Vec2(self.x*s, self.y*s)
    def dot(self, o): return self.x*o.x + self.y*o.y
    def cross(self, o): return self.x*o.y - self.y*o.x
    def mag(self): return math.sqrt(self.x**2 + self.y**2)
    def norm(self): m = self.mag(); return Vec2(self.x/m, self.y/m) if m else Vec2()
    def rotate(self, angle):
        c, s = math.cos(angle), math.sin(angle)
        return Vec2(self.x*c - self.y*s, self.x*s + self.y*c)
    def __repr__(self): return f"Vec2({self.x}, {self.y})"

class Vec3:
    __slots__ = ["x", "y", "z"]
    def __init__(self, x=0, y=0, z=0): self.x, self.y, self.z = x, y, z
    def __add__(self, o): return Vec3(self.x+o.x, self.y+o.y, self.z+o.z)
    def __sub__(self, o): return Vec3(self.x-o.x, self.y-o.y, self.z-o.z)
    def __mul__(self, s): return Vec3(self.x*s, self.y*s, self.z*s)
    def dot(self, o): return self.x*o.x + self.y*o.y + self.z*o.z
    def cross(self, o): return Vec3(self.y*o.z-self.z*o.y, self.z*o.x-self.x*o.z, self.x*o.y-self.y*o.x)
    def mag(self): return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def norm(self): m = self.mag(); return Vec3(self.x/m, self.y/m, self.z/m) if m else Vec3()
    def __repr__(self): return f"Vec3({self.x}, {self.y}, {self.z})"

def test():
    a, b = Vec2(3, 4), Vec2(1, 0)
    assert abs(a.mag() - 5.0) < 1e-9
    assert a.dot(b) == 3
    n = a.norm()
    assert abs(n.mag() - 1.0) < 1e-9
    r = Vec2(1, 0).rotate(math.pi/2)
    assert abs(r.x) < 1e-9 and abs(r.y - 1) < 1e-9
    v = Vec3(1, 0, 0).cross(Vec3(0, 1, 0))
    assert abs(v.z - 1) < 1e-9
    s = Vec3(1, 2, 3) + Vec3(4, 5, 6)
    assert s.x == 5 and s.y == 7 and s.z == 9
    print("vec_math: all tests passed")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("Usage: vec_math.py --test")
