def findIntersection(StrArr):
    output = []
    # StrArr = sorted(StrArr)
    lisA = StrArr[0]
    lisB = StrArr[1]
    lisA = lisA.split(", ")
    lisB = lisB.split(", ")

    for i in range(0, len(lisA)):
        a = lisA[i]
        for c in range(0, len(lisA)):
            b = lisB[c]
            if a == b:
                output.append(a)
    return output

if __name__ == "__main__":
    i = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    print(findIntersection(i))