from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def crossPart(dir1,dir2,output):
    list1 = []
    list2 = []
    outputList = []
    with open(dir1,'r') as f:
        list1 = f.readlines()
    with open(dir2,'r') as f:
        list2 = f.readlines()
    outputList = list(set(list1)&set(list2))
    with open(output,'w') as f:
        f.writelines(outputList)

def sub(dir1,dir2,output):
    list1 = []
    list2 = []
    outputList = []
    with open(dir1,'r') as f:
        list1 = f.readlines()
    with open(dir2,'r') as f:
        list2 = f.readlines()
    outputList = list(set(list1)-set(list2))
    with open(output,'w') as f:
        f.writelines(outputList)

def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, conflict_handler='resolve')
    parser.add_argument('--commitDir1', help='dir of 1st commit')
    parser.add_argument('--commitDir2', help='dir of 2nd commit')
    parser.add_argument('--outputDir', help='dir of 2nd commit')
    args = parser.parse_args()

    Dir1 = args.commitDir1
    Dir2 = args.commitDir2
    output = args.outputDir

    # crossPart(Dir1,Dir2,output)
    sub(Dir1,Dir2,output)

if __name__ == "__main__":
    main()