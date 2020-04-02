def encrypt(ch, key):
    LETTERS = 26
    if "A" <= ch <= "Z":
        base = ord("A")
    elif "a" <= ch <= "z":
        base = ord("a")
    else:
        return ch
    return chr(base + (ord(ch) - base + key % LETTERS) % LETTERS)


if __name__ == "__main__":
    KEY = 3
    lint = input("请输入英文字符串：\n")
    print(''.join(list(map(lambda s: encrypt(s, KEY), lint))))
    input("任意键退出")