# the default value evaliuted only once when the function is defined, not each time the function is called
def add_item_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


# basket = [{"item": "apple"}]

print(add_item_to_basket({"item": "banana"}))
print(add_item_to_basket({"item": "apple"}))
print(add_item_to_basket({"item": "orange"}))
