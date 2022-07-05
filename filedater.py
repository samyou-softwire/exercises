import shutil, os, datetime


def date(filename: str) -> str:
    return f"{datetime.datetime.now()} - {filename}".replace(":", " ")


def rename(file: str, path: str):
    fullpath = os.path.join(path, file)
    if os.path.isdir(fullpath):
        for sub in os.listdir(fullpath):
            rename(sub, fullpath)

    datedname = date(file)
    print(datedname)
    os.rename(fullpath, os.path.join(path, datedname))


initialpath = input("Please input path: ")

rename(initialpath, ".")
