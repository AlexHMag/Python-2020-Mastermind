
def medir_largos(iterable, *args):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)


def main():
    print(medir_largos("hola", "me", "llamo"))


if __name__ == "__main__":
    main()
