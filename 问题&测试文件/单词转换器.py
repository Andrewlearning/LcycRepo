

def main():
    wordFile = open("words.txt", "r")
    chineseFile = open("chinese.txt", "r")

    word = getContent(wordFile)
    chinese = getContent(chineseFile)

    i = 0
    for w, c in zip(word, chinese):
        if i != 0 and i % 10 == 0:
            print()
            print("--"*15)
            print()
        print("{:<25s}{:>10s}".format(w, c))
        i += 1



    wordFile.close()
    chineseFile.close()


def getContent(file):
    content = []
    for line in file.readlines():
        content.append(line.strip())

    return content



if __name__ == '__main__':
    main()