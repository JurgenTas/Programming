__author__ = 'J Tas'

class Table:

    def __init__(self, cols):
        self.cols = cols
        self.rows = []

    def __repr__(self):
        return str(self.cols) + "\n" + "\n".join(map(str,self.rows))
    
    def insert(self, row):
        if len(row) != len(self.cols):
            raise TypeError("wrong number of elements")
            row_dict = dict(zip(self.cols, row))
            self.rows.append(row_dict)

if __name__ == "__main__":
    users = Table(["user_id", "name",])
    print(users)

