a = ""
for i in range(1, 10):
    for j in range(1, i + 1):
        a += (str(j) + "×" + str(i) + "=" + str(j * i) + " ")
    a += "\n"
print(a)
