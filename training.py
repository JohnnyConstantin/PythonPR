def main():
    f = open('steam.dll', 'rb')
    for a in f:
        print(bytes(a))


if __name__ == '__main__':
    main()
