def create(name):
    print(f"created {name}")


def delete(name: str, formal: bool):
    if formal:
        print(f"deleted............. {name}.")
    else:
        print(f"deleted {name}!")


