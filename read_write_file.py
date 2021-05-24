
filename = 'data/inputData.txt'

# READING THE FILE
with open('data/inputData.txt') as input_data:
    contents = input_data.read()
    print(contents)
print(contents)
print('Reading a inputData.txt file completed')


with open('data/inputData.txt') as input_data:
    counter = 1
    print('Reading line by line:')
    for line in input_data:
        print('line:',counter,line)
        counter += 1


# WRITING THE FILE ( with 'a' we append the lines,
# with 'w' we override the content)
with open (filename, 'a') as input_data:
    input_data.write("I love programming!\n")
    input_data.write("I love  everything about programming!\n")




