obj = {}
arr = []
fixedChars = []
fixedPos = 0
stepCounter = 0
objOrdinary = 0
step = 1
my_str = []


def combos(word):
    global my_str
    my_str = list(word)

    def add_row(character):
        global objOrdinary
        obj['objOrdinary'] = character
        objOrdinary += 1

    def iterator():
        global step
        global stepCounter
        global fixedPos
        global my_str
        arr = []
        if step < len(word):
            if step == 1:
                for c in my_str:
                    add_row(c)

                step += 1
            elif step == 2:
                stepCounter += 1
                my_str = list(word)
                if fixedPos < len(my_str):
                    fixedChars = my_str[fixedPos:step -1]
                for c in my_str:
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
                        my_str = list(word)
                        for c in obj[key]:
                            my_str = list(filter(lambda x: x != c, my_str))
                        for strChar in list(my_str):
                            arr = []
                            arr.append(list(obj[key]))
                            arr.append(strChar)
                            add_row(arr)
                step += 1
            iterator()
    iterator()


combos("abc")
