def main():
    
    d = {
        "A":{
            "D":{"F": 1, "G": 1},
            "E":{}
        },
        "B":{
            "D":{},
            "E":{}
        },
        "C":{
            "D":{},
            "E":{}
        }
    }
    print(d["A"]["D"]["F"])
    print(d["A"]["D"]["G"])

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()