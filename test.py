from vec_math import Vec2, Vec3
a = Vec3(1,0,0); b = Vec3(0,1,0)
c = a.cross(b)
assert abs(c.z - 1) < 1e-10
assert abs(a.dot(b)) < 1e-10
assert abs(a.mag() - 1) < 1e-10
v = Vec2(3,4)
assert abs(v.mag() - 5) < 1e-10
assert abs(v.norm().mag() - 1) < 1e-10
print("Vec math tests passed")