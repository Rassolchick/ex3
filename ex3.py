import os

def new_list(directory):
    file_list = os.listdir(directory)
    new_list = []

    for file in file_list:
        with open(directory + "/" + file) as cur_file:
            new_list.append([file, 0, []])
            for line in cur_file:
                new_list[-1][2].append(line.strip())
                new_list[-1][1] += 1

    return sorted(new_list, key=lambda x: x[2], reverse=True)

def create_new_text(directory, filename):
    with open(filename + '.txt', 'w+') as newtext:
        for file in new_list(directory):
            newtext.write(f'File name: {file[0]}\n')
            newtext.write(f'Length: {file[1]} string(s)\n')
            for string in file[2]:
                newtext.write(string + '\n')
            newtext.write('     ***     \n')


create_new_text('text', 'mytext')