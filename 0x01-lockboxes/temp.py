#!/usr/bin/python3

def canUnlockAll(boxes):
    boxesLift = list(range(1, len(boxes)))
    keys = set(boxes[0])

    def box(tempKeys, tempLeft):
        flag = False
        if len(keys) > 0 and len(boxesLift) > 0:
            for key in tempKeys:
                print("Key:: ",key)
                if key in tempLeft:
                    keys.update(boxes[key])
                    keys.remove(key)
                    boxesLift.remove(key)
                    flag = True
                # if (len(keys) == 0):
                #     keys.add("gg")
                print("Keys:: ",keys, "::: key:", key, 'boxesLift: ', boxesLift)
        # if len(keys)
        # print("Am OUT")
        if flag:
            print("entered: : ", keys)
            tempKeys = keys.copy()
            tempLeft = boxesLift.copy()
            return box(tempKeys, tempLeft)
        else:
            # print("did not enter")
            if len(boxesLift) > 0:
                return False
            else:
                return True
        
    print(boxesLift)
    print(keys)
    tempKeys = keys.copy()
    tempLeft = boxesLift.copy()
    return (box(tempKeys, tempLeft))


boxes = [[1], [2], [3], [4], []]

print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
