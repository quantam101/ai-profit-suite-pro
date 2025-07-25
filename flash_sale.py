def apply_flash_sales(products):
    for product in products:
        if product["sales"] < 10:
            product["discount"] = "25%"
    print("Flash sales updated.")
