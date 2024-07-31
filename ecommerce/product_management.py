def product_details(name):
    product_list = {
        "iphone": 95000,
        "laptop": 108000,
        "washing_machine": 14000,
        "friedge": 44000,
        "ac": 36000
    }
    for i in list(product_list.keys()):
        if i == name:
            print(f"Product: {name}; Price: {product_list[name]}")
            break
    else:
        print("Product not found.")