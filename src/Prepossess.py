import regular as R

class Preposses:
    def showLine(self, filename):
        with open(filename,'r') as F:
            i = 5
            for lines in F.readlines():
                print(lines)
                print('\n')
                i -= 1
                if i < 0:
                    break

    def writeSome(self, filein, fileout):
        with open(filein, 'r') as fin:
            with file(fileout, 'w') as fout:
                i = 2000
                for lines in fin.readlines():
                    tp = lines.split('\t', 22)

                    # new_tp = tp[:6] + tp[17:]
                    new_tp = str(tp[2:3]) + '\n'
                    # new_line = '\t'.join(new_tp)
                    fout.writelines(new_tp)
                    i -= 1
                    if i < 0:
                        break

    def file2Dict(self, filein):
        d = {}
        with open(filein,'r') as fin:
            for lines in fin.readlines():
                sublist = lines.split('\t',22)
                if d.get(sublist[1]) == None:
                    d[sublist[1]] = sublist[2:] 
                else:
                    d[sublist[1]].append(sublist[2:])
        return d

    def writeUsefulline(self, filein, fileout):
        with open(filein, 'r') as fin:
            with file(fileout, 'w') as fout:
                # i = 200000
                for lines in fin:
                    # print lines.count('\t')
                    tp = lines.split('\t', 22)

                    problem_name = tp[3] if tp[3] else 'null'
                    KC_traced_skill = tp[19] if tp[19] else 'null' 
                    KC_rules = tp[20] if tp[20] else 'null' 



                    fout.writelines(problem_name + '||' + KC_traced_skill + '||' + KC_rules + '\n')


    def handle_problem_name(self, file_path_in, file_path_out):
        s = set()
        sh = set()

        fout = open(file_path_out, 'w')

        with open(file_path_in, 'r') as f:
            for line in f:
                tp = line.split('||')
                problem_name = tp[0]

                if problem_name == 'null':
                    print 'aaaaaaaaaaaaaaaaaaaaa'
                    break
                else:
                    if R.iswhole(problem_name):
                       new_problem_name = R.handle_whole(problem_name)
                       fout.write(new_problem_name + '\n')
                    else:
                        # print problem_name
                        tp = problem_name.split(' ', 1)
                        left, right = tp[0], tp[1]
                        new_left = R.handle_whole(left)
                
                        new_right = R.handle_right(right)

                        fout.write(new_left + new_right + '\n')
                        # if right not in sh:
                        #     print right
                        #     sh.add(right)

                        # if new_right not in s:
                        #     print new_right
                        #     s.add(new_right)

                    # new_problem_name = R.split_eng_num(problem_name)
                    # R.replaceOP(new_problem_name)

        

if __name__ == '__main__':
    pre = Preposses()
    # pre.showLine('dateset/algebra_2008_2009_train.txt') 
    pre.writeUsefulline('../dataset/a89_part.txt','../dataset/a89_useful.txt')
    # dataset = pre.file2Dict('../dataset/0809train.txt')
    pre.handle_problem_name('../dataset/a89_useful.txt', '../dataset/a89_problem_name.txt')
