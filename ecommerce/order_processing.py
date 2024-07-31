def place_order(name, qty, price):
    product_list = {
        "iphone": 95000,
        "laptop": 108000,
        "washing_machine": 14000,
        "friedge": 44000,
        "ac": 36000
    }
    for i in list(product_list.keys()):
        if i == name and product_list[i] == price:
            print("Thank you for shopping. Your order has been placed.")
            print(f"Order: {i} x {qty} -- To pay: {price * qty}.")
            break
    else:
        print("Sorry!!! Your order is not placed.")