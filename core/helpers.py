def printError(message, fatal: bool = False):
    import os, sys
    if os.name != 'nt':
        CRED = '\033[91m'
        CEND = '\033[0m'
        print(CRED + 'Error: ' + message + CEND)
    else:
        print('Error: ' + message)

    import inspect
    print('Errored at: `' + inspect.stack()[1][1] + "[" + str(inspect.stack()[1][2]) + "] " + inspect.stack()[1][3] + '`')
    print('Came from: `' + inspect.stack()[2][1] + "[" + str(inspect.stack()[2][2]) + "] " + inspect.stack()[2][3] + '`')

    if fatal:
        sys.exit()

def printReadable(*text):
    import pprint
    pprint.pprint(text, width=2)
