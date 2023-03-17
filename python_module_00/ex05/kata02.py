# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

if __name__ == "__main__":
    print(f"{kata[1]:02}/{kata[2]:02d}/{kata[0]:04d}")
    print(f" {kata[3]:02d}:{kata[4]:02d}")
