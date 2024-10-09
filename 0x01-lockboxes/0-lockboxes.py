#!/usr/bin/python3

def canUnlockAll(boxes):
    boxesLift = list(range(1, len(boxes)))
    keys = set(boxes[0])

    def box(tempKeys, tempLeft):
        flag = False
        if len(keys) > 0 and len(boxesLift) > 0:
            for key in tempKeys:
                if key in tempLeft:
                    keys.update(boxes[key])
                    keys.remove(key)
                    boxesLift.remove(key)
                    flag = True
        if flag:
            tempKeys = keys.copy()
            tempLeft = boxesLift.copy()
            return box(tempKeys, tempLeft)
        else:
            if len(boxesLift) > 0:
                return False
            else:
                return True

    tempKeys = keys.copy()
    tempLeft = boxesLift.copy()
    return (box(tempKeys, tempLeft))
