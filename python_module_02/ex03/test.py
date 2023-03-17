from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('good.csv', None, True, 0, 0) as file:
        data = file.getdata()
        print(data)
        data = file.getdata()
        print(data)
        print(file.getheader())

    with CsvReader('bada.csv') as file:
        if file == None:
            print("File is corrupted")
