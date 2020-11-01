obj = {}
arr = []
fixedChars = []
fixedPos = 0
stepCounter = 0
objOrdinary = 0
step = 1


def combos(word):
    str = list(word)

    def add_row(character):
        global objOrdinary
        obj['objOrdinary'] = character
        objOrdinary += 1

    def iterator():
        global step
        global stepCounter
        global fixedPos
        arr = []
        if step < len(word):
            if step == 1:
                for c in str:
                    add_row(c)

                step += 1
            elif step == 2:
                stepCounter += 1
                str = list(word)
                if fixedPos < len(str):
                    fixedChars = str[fixedPos:step -1]
                for c in str:
                    arr = []
                    arr.append(fixedChars)
                    arr.append(c)
                    add_row(arr)
                fixedPos += 1
                if stepCounter >= len(word):
                    step += 1
            else:
                lastObjKey = len(obj.keys()) -1
                for key in obj.keys():
                    if len(obj[key]) == len(obj[lastObjKey]):
                        str = list(word)
                        for c in obj[key]:
                            str = list(filter(lambda x: x != c, str))
                        for strChar in list(str):
                            arr = []
                            arr.append(list(obj[key]))
                            arr.append(strChar)
                            add_row(arr)
                step += 1
            iterator()
    iterator()


combos("abc")
