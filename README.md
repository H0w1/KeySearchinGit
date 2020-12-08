# requirements document 
## summary
1. scripts for pick out commit logs for our provided keywords
2. updating scripts for pick out the new commit logs we need to study.

Input:
- commits we have studied
- our keywords and cross-keywords list
- the Linux version we want to study
    - (dir to the Linux git repo we want)

## details of functionality 
1. it can automatically search for all the commit-ids and 
    - save the results for all keywords and cross-keywords.
    - make soft-links for each target keyword, show the log numbers of them  
2. when the git base is updated, it can automatically 
    - pick up the new added commit-ids for each target keyword.
    - save the new results for all keywords and cross-keywords in the 'update/commits' dir and wait us to update it.


## desigh
Two kinds of keywords and our target keywords:
- direct keywords
  - short name & Regular Expression
  - short name as the filename of results
- cross keywords
  - short name list
  - search input in files by the short name
- target keywords
    - a list of the keywords/corss-keywords we need to study.
