def upload_resource(name, link):
    with open("resources/resource_list.txt", "a") as f:
        f.write(f"{name}: {link}\n")
    print(f"Resource {name} uploaded.")
