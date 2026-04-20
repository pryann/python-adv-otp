from numpy import add


def add_cheese(burger):
    burger["cheese"] = True
    return burger


def add_double_meal(burger):
    burger["double_meal"] = True
    return burger


def add_glutenfree_bun(burger):
    burger["glutenfree_bun"] = True
    return burger


def remove_onion(burger):
    burger["onion"] = False
    return burger


def make_burger(basic_burger, *fns):
    burger = basic_burger
    for fn in fns:
        burger = fn(burger)
    return burger


custom_burger = make_burger({}, add_cheese, add_double_meal)
print(custom_burger)
custom_burger_2 = make_burger({}, add_double_meal, add_glutenfree_bun, remove_onion)
print(custom_burger_2)
