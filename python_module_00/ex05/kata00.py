# Put this at the top of your kata00.py file
kata = (12, 13)


if __name__ == "__main__":
    if (kata is not None and len(kata) != 0):
        print(f"The {len(kata)} numbers are: ", end="")
        print(*kata, sep=", ")
