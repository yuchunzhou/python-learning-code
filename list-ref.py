lst = [1, 2, 3, 4]


def foo(lst_):
    lst_.append(5)


def bar(lst_):
    # lst_ refs to a new list
    print(f"before assighment: {id(lst_)}")
    lst_ = [0, 0, 0]
    print(f"after assighment: {id(lst_)}")


foo(lst)
print(lst)  # [1, 2, 3, 4, 5]

bar(lst)
print(lst)  # [1, 2, 3, 4, 5]
