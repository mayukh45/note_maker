import pyperclip
from file_writer import makenotes


def main():
    print("Enter name of the file :")
    name_of_file = input()
    f = open(name_of_file + ".txt", 'w')
    f.close()

    pyperclip.copy("")
    print("Press CTRL+C to stop")
    #fun()
    boo=True
    try:
        while boo:
            boo = makenotes(name_of_file)
            continue

    except KeyboardInterrupt:
        print("Thanks for Using\nDeveloped by Mayukh")


if __name__ == "__main__":
    main()







