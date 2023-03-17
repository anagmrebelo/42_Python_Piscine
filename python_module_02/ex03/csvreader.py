import csv

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            self.sourceFile = open(filename, 'r')
        except FileNotFoundError:
            self.sourceFile = None
        self.filename = filename
        self.sep = sep
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data =[]
        self.header = header
        self.header_line = None

    def __enter__(self):
        if self.sourceFile is None:
            return None
        csvreader = csv.reader(self.sourceFile)
        if self.header is True:
            self.header_line = next(csvreader)
        for row in csvreader:
            self.data.append(row)
        return self

    def __exit__(self, type, value, traceback):
        if self.sourceFile:
            self.sourceFile.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
            Return:
            nested list (list(list, list, ...)) representing the data.
        """ 
        if self.skip_bottom == 0:
            return self.data[self.skip_top::]
        else:
            return self.data[self.skip_top::self.skip_bottom * -1]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        return (self.header_line)

## To be more robust, program should verify if args are the correct type and skip_top and skip_bottom are not negative