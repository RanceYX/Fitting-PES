import csv


class Interface_csv():

    @staticmethod
    def read_data_bare(filename, Val):
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for row in reader:
                v = []
                for i in row:
                    v.append(float(i))
                Val.append(v)

    @staticmethod
    def read_data_deflt(filename, Xval, Yval):
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for x in header_row[1:]:
                x_n = int(x)
                Xval.append(x_n)

            for row in reader:
                y = []
                for i in row[1:]:
                    y.append(float(i))
                Yval.append(y)

    @staticmethod
    def write_data_bare(filename, Val):
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for v in Val:
                writer.writerow(v)


# X=[]
# Y=[]
# Interface_csv.read_data_deflt('alcl-he_all.csv',X,Y)
# print(X[0]+X[1])
