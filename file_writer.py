# import pyperclip


def makenotes(name_of_file):
    import pyperclip
    # from note_maker import name_of_file

    if len(pyperclip.paste()) > 0:

        r = open(name_of_file + ".txt", 'a')

        r.write('*' * 200 + "\n\n")

        r.write(pyperclip.paste() + "\n\n")
        pyperclip.copy("")
        r.close()

    return True

