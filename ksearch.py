import sys,os
import json
import getopt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

this_dir, this_file = os.path.split(os.path.abspath(__file__))
DEBUG = True

def parse_config():
    with open("config.json",'r') as configFile:
        configDict = json.load(configFile)
    return configDict

def parse_keywords():
    with open("keywords.json",'r') as keywordFile:
        keywordList = json.load(keywordFile)
    return keywordList

def grep_keywords(keywordList,RepoDir):
    keywordDict = keywordList[0]
    crossDict = keywordList[1]
    targetDict = keywordList[2]

    # search all the keywords and cross_keywords in the git repo(from config)
    # save results for all keywords and cross-keywords.
        # git log --grep $$ -E > commits/$$.commits
    for key,value in keywordDict.items():
        key = key.replace(' ','')
        # print(key)
        command = "cd " + RepoDir + "&&" + "git log --grep '" + value + "' -E | grep '^commit' > " + this_dir + "/commits/" + key + ".commits"
        print(command[command.find("&&")+2:])
        if not DEBUG:
            os.system(command)

    # cross part
    for key,value in crossDict.items():
        key = key.replace(' ','')
        value[0]= value[0].replace(' ','')
        value[1]= value[1].replace(' ','')
        inputDir1 = 'commits/' + value[0] + '.commits'
        inputDir2 = 'commits/' + value[1] + '.commits'
        outputDir = 'commits/' + key + '.commits'
        with open (inputDir1, 'r') as f1:
            list1 = f1.readlines()
        with open (inputDir2, 'r') as f2:
            list2 = f2.readlines()

        crossPart = list(set(list1)&set(list2))
        if not DEBUG:
            with open (outputDir, 'w') as f:
                f.writelines(crossPart)
        else:
            print(key, " : ", len(crossPart))
    
    # make soft-links for each target keyword,
        # ln -s commits/$$.commits target-commits/$$.commits
    if not DEBUG:
        for key,value in targetDict.items():
            targetList = value
        # print(targetList)
        for target in targetList:
            target = target.replace(' ','')
            command = 'ln -sf commits/' + target + '.commits target-commits/' + target + '.commits'
            os.system(command)

    print('oldRepos commits collected')


def print_res_of_target_keyword(targetList):
    logNub = {}
    for target in targetList:
        target = target.replace(' ','')
        fileDir = "commits/" + target + '.commits'
        with open(fileDir , 'r') as f:
            List = f.readlines()
            logNub[target] = len(List)
    if not DEBUG:
        with open("commits/logNub.json" , 'w') as f:
            json.dump(logNub,f,indent=1)
    print('oldcount:',logNub)
    return logNub
    

def update(keywordList,newRepoDir): 
    # search all the keywords and cross_keywords in the git repo(from config)
    # save results for all keywords and cross-keywords in 'update/commits'.
    # make soft-links for each target keyword in 'update/target-commits'
    # compute the new added commits logs for each target keyword
    # saved the new added commits logs in 'update/'
    # show the new added commits logs number for each target keyword
    keywordDict = keywordList[0]
    crossDict = keywordList[1]
    targetDict = keywordList[2]

    RepoDir = newRepoDir

    # search all the keywords and cross_keywords in the git repo(from config)
    # save results for all keywords and cross-keywords.
    for key,value in keywordDict.items():
        key = key.replace(' ','')
        # print(key)
        command = "cd " + RepoDir + "&&" + "git log --grep '" + value + "' -E | grep '^commit' > " + this_dir + "/commits/" + key + ".commits"
        print(command[command.find("&&")+2:])
        if not DEBUG:
            os.system(command)

    # cross part
    for key,value in crossDict.items():
        key = key.replace(' ','')
        value[0]= value[0].replace(' ','')
        value[1]= value[1].replace(' ','')
        inputDir1 = 'update/commits/' + value[0] + '.commits'
        inputDir2 = 'update/commits/' + value[1] + '.commits'
        outputDir = 'update/commits/' + key + '.commits'
        with open (inputDir1, 'r') as f1:
            list1 = f1.readlines()
        with open (inputDir2, 'r') as f2:
            list2 = f2.readlines()

        crossPart = list(set(list1)&set(list2))

        if not DEBUG:
            with open (outputDir, 'w') as f:
                f.writelines(crossPart)
        else:
            print(key, " : ", len(crossPart))
    
    # make soft-links for each target keyword,
    # ln -s commits/$$.commits target-commits/$$.commits
    for key,value in targetDict.items():
        targetList = value
        # print(targetList)
    if not DEBUG:
        for target in targetList:
            target = target.replace(' ','')
            command = 'ln -sf update/commits/' + target + '.commits update/target-commits/' + target + '.commits'
            os.system(command)

    new_commit_count(targetList)
    print('newRepos commits collected')

def new_commit_count(targetList):
    
    difcount ={}
    allcount = {}
    for target in targetList:
        target = target.replace(' ','')
        newlist = []
        oldlist = []
        newDir = "update/commits/" + target + '.commits'
        oldDir = "commits/" + target + '.commits'
        outputDir = "update/newcommits/" + target + '.commits'
        with open (newDir, 'r') as newf:
            newlist = newf.readlines()
        with open (oldDir, 'r') as oldf:
            oldlist = oldf.readlines()
        deflist = list(set(newlist)-set(oldlist))
        # store new commits
        if not DEBUG:
            with open (outputDir,'w') as f:
                f.writelines(deflist)
        difcount[target] = len(newlist) - len(oldlist)
        allcount[target] = len(newlist)
    # store the count for new commmits
    if not DEBUG:
        with open ("update/newcommits/difcount.json",'w') as f:
            json.dump(difcount,f,indent=1)
        # store all nubs of commits in new repo
        with open ("update/commits/allcount.json",'w') as f:
            json.dump(allcount,f,indent=1)
    print('newcount:',allcount)
    print('difcount:',difcount)


    

def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, conflict_handler='resolve')
    parser.add_argument('--newRepo', default = '/home/seclab/xujianhao/linux-stable' , help='dir of new repo')
    args = parser.parse_args()

    configDict = parse_config()
    keywordList = parse_keywords()

    oldRepos = configDict['RepoDir']
    newRepos = args.newRepo
    print('oldRepos:',oldRepos)
    print('newRepos:',newRepos)

    grep_keywords(keywordList,oldRepos)

    update(keywordList,newRepos)

    # collect targetkeywords and count them
    targetDict = keywordList[2]
    for key,value in targetDict.items():
        targetList = value
    # oldrepo commits count
    print_res_of_target_keyword(targetList)
    # collect new commits and count nub
    new_commit_count(targetList)

if __name__ == "__main__":
    main()