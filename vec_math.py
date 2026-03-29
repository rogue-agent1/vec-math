#!/usr/bin/env python3
"""Vector math library (2D/3D/4D). Zero dependencies."""
import math, sys

class Vec2:
    __slots__ = ("x","y")
    def __init__(self, x=0, y=0): self.x, self.y = float(x), float(y)
    def __add__(s, o): return Vec2(s.x+o.x, s.y+o.y)
    def __sub__(s, o): return Vec2(s.x-o.x, s.y-o.y)
    def __mul__(s, k): return Vec2(s.x*k, s.y*k)
    def __neg__(s): return Vec2(-s.x, -s.y)
    def dot(s, o): return s.x*o.x + s.y*o.y
    def cross(s, o): return s.x*o.y - s.y*o.x
    def mag(s): return math.sqrt(s.x**2+s.y**2)
    def norm(s): m=s.mag(); return Vec2(s.x/m,s.y/m) if m>0 else Vec2()
    def angle(s): return math.atan2(s.y, s.x)
    def rotate(s, a): c,sn=math.cos(a),math.sin(a); return Vec2(s.x*c-s.y*sn, s.x*sn+s.y*c)
    def lerp(s, o, t): return s*(1-t)+o*t
    def dist(s, o): return (s-o).mag()
    def __repr__(s): return f"Vec2({s.x:.3f}, {s.y:.3f})"
    def __eq__(s, o): return isinstance(o, Vec2) and abs(s.x-o.x)<1e-10 and abs(s.y-o.y)<1e-10

class Vec3:
    __slots__ = ("x","y","z")
    def __init__(self, x=0, y=0, z=0): self.x, self.y, self.z = float(x), float(y), float(z)
    def __add__(s, o): return Vec3(s.x+o.x, s.y+o.y, s.z+o.z)
    def __sub__(s, o): return Vec3(s.x-o.x, s.y-o.y, s.z-o.z)
    def __mul__(s, k): return Vec3(s.x*k, s.y*k, s.z*k)
    def __neg__(s): return Vec3(-s.x, -s.y, -s.z)
    def dot(s, o): return s.x*o.x+s.y*o.y+s.z*o.z
    def cross(s, o): return Vec3(s.y*o.z-s.z*o.y, s.z*o.x-s.x*o.z, s.x*o.y-s.y*o.x)
    def mag(s): return math.sqrt(s.x**2+s.y**2+s.z**2)
    def norm(s): m=s.mag(); return Vec3(s.x/m,s.y/m,s.z/m) if m>0 else Vec3()
    def lerp(s, o, t): return s*(1-t)+o*t
    def dist(s, o): return (s-o).mag()
    def reflect(s, n): return s - n*(2*s.dot(n))
    def __repr__(s): return f"Vec3({s.x:.3f}, {s.y:.3f}, {s.z:.3f})"

class Vec4:
    __slots__ = ("x","y","z","w")
    def __init__(self, x=0, y=0, z=0, w=0): self.x,self.y,self.z,self.w = float(x),float(y),float(z),float(w)
    def __add__(s, o): return Vec4(s.x+o.x, s.y+o.y, s.z+o.z, s.w+o.w)
    def __mul__(s, k): return Vec4(s.x*k, s.y*k, s.z*k, s.w*k)
    def dot(s, o): return s.x*o.x+s.y*o.y+s.z*o.z+s.w*o.w
    def mag(s): return math.sqrt(s.x**2+s.y**2+s.z**2+s.w**2)
    def __repr__(s): return f"Vec4({s.x:.3f}, {s.y:.3f}, {s.z:.3f}, {s.w:.3f})"

if __name__ == "__main__":
    a, b = Vec3(1,0,0), Vec3(0,1,0)
    print(f"a x b = {a.cross(b)}")
    print(f"|a| = {a.mag()}")
