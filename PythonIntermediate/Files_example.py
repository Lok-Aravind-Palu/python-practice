import sys


def how_to_open_file():
    f = open('test_file.txt', mode='wt', encoding="utf-8")
    f.write("Hare rama Hare rama Hare krishna Hare krishna\n")
    f.write("\nOm namo Bhagathe vasudevaya")
    print("This is written")
    f.close()


def read_file():
    f = open('test_file.txt', mode='rt', encoding="utf-8")
    rama = f.read()
    print(rama)
    kris = f.readline()
    print(kris)
    f.close()


def append_file():
    f = open('test_file.txt', mode='at', encoding="utf-8")
    f.writelines("\nHare Krishna Hare Krishna \n"
                 "Krishna Krishna Hare Hare \n"
                 "Hare Rama Hare Rama \n"
                 "Rama Rama Hare Hare")
    f.close()


def with_keyword():
    with open('test_file.txt', mode='rt', encoding="utf-8") as f:
        for x in f:
            print(x)
            sys.stdout.write(x)


how_to_open_file()
print("----------------------------------------------------------------------")
read_file()
print("----------------------------------------------------------------------")
append_file()
print("----------------------------------------------------------------------")
with_keyword()
