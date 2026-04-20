def log_argv(*argv):
    print(type(argv), argv)


log_argv()
log_argv(1, 2, 3)


def log_kwargv(**kwargv):
    print(type(kwargv), kwargv)


log_kwargv(language="Python", version="3.14", type="script")


# item = {"name": "book", "price": 10, "quantity": 2}
def calculate_total_price(*items, **kwargv):
    total_price = sum(item["price"] * item["quantity"] for item in items)
    if "vat" in kwargv:
        total_price *= 1 + (kwargv["vat"] / 100)
    if "discount" in kwargv:
        total_price *= 1 - (kwargv["discount"] / 100)
    return round(total_price, 2)


total = calculate_total_price(
    {"name": "book", "price": 10, "quantity": 2},
    {"name": "pen", "price": 100, "quantity": 3},
    {"name": "notebook", "price": 2000, "quantity": 4},
    vat=27,
    discount=10,
)

print(total)
