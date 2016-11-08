# -*- coding: utf-8 -*- 

def cut(file_path_in, file_path_out, number):

    id_set = set()
    count = 0
    with open(file_path_out, 'w') as fout:
        with open(file_path_in, 'r') as fin:
            for line in fin:
                id = line.split('\t', 2)[1]

                if id not in id_set and count < number:
                    id_set.add(id)
                    fout.write(line)
                    count += 1
                elif id not in id_set and count == number:
                    break
                else:
                    fout.write(line)

def train_test_split(file_path_in):

    train = []
    test = []
    
    with open(file_path_in, 'r') as f:
        f.readline()
        line = f.readline()
        next_line = f.readline()
        assert line.split('\t', 3)[2] == next_line.split('\t', 3)[2]

        while next_line:
            unit = line.split('\t', 3)[2].split(',', 1)[0]
            next_unit = next_line.split('\t', 3)[2].split(',', 1)[0]
            if unit == next_unit:
                train.append(line)
                line = next_line
                next_line = f.readline()
            elif unit != next_unit:
                test.append(line)
                line = next_line
                next_line = f.readline()
        test.append(line)
    return train, test
            

def main():
    # 1
    # file_path_in = '../dataset/algebra_2008_2009_train.txt'
    # file_path_out = '../dataset/a89_part.txt'
    # cut(file_path_in, file_path_out, 100)

    # 2
    pass

main()
train, test = train_test_split('../dataset/a89_part.txt')