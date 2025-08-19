class A(object):
    pass


class B(A):
    pass


class C(B, A):
    pass


b = B()
print(issubclass(B, A))  # True
print(isinstance(b, A))  # True

c = C()
print(issubclass(C, A))  # True
print(isinstance(c, A))  # True
print(issubclass(C, B))  # True
print(isinstance(c, B))  # True
