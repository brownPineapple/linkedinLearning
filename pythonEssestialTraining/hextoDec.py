def hexToDec(hexNum):
    try:
        x = int(hexNum,16)
        return x
    except:
        return None
    else:
        return None

a = hexToDec('A2')
print(a)
