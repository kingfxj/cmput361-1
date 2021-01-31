import json, sys

def error(name):
    '''
    Print out the error and exit the program with -1
    input: name is the name of the error
    '''
    print(name)
    exit(-1)

if __name__ == "__main__":
    # Get the arguments and validate the number
    arguments = sys.argv
    if len(arguments) != 3:
        error("Invalid arguents")

    # Open the input file for read and output file for write
    try:
        inputFile = open(arguments[1], 'r')
        outputFile = open(arguments[2], 'w')
    except IOError:
        error('Invalid file arguments')

    # Load and parse json data
    inputData = json.load(inputFile)
    docId = []
    for data in inputData:
        # Validate doc ID and they are unique
        try:
            ID = int(data['doc_id'])
        except ValueError:
            error('Invalid Document ID')
        if ID in docId:
            error('Invalid Document ID')
        docId.append(ID)

        book = data['book']             # The book name of the document
        line = data['line']             # The line of the document

    print('done')