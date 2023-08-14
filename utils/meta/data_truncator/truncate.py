import os


def data_truncator(dir):
    """Truncate the data so as to keep repo small"""
    for root, dirs, files in os.walk(dir):
        print(files)

        for i in range(len(files)):
            if files[i].endswith(".csv"):
                filename = f"{root}/{files[i]}"
                print(filename)
                f = open(filename, "a+")
                read_file = f.read()
                if "TRUNCATED" not in read_file:
                    f.truncate(930)
                    f.write("\nTRUNCATED")
                    f.close()
