#Defining function swapFileData
def swapFileData():

   #Taking input from user ad storing it in the file variable
    file1 = input(" Enter a file name ")
    file2 = input(" Enter another file name ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)

swapFileData()