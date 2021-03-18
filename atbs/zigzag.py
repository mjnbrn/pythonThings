import time, sys

# How many spaces to indent
indent = 0
# Whether the indentation is increasing or not
indentIncreasing = True

try:
    while True:
        # Main Program Loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            # Increase the number of spaces
            indent += 1
            if indent == 20:
                # Change Direction
                indentIncreasing = False

        else:
            # Decrease the number of spaces
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
