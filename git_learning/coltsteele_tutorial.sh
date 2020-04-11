GIT TUTORIAL 

git log # can only be used in a git repo!

# git and github are completely separate things. git 
# is the tool for github

git init # to initialize git repo

ls # will see nothing
ls -a # will see .git

git status # to check status of repo

# make some changes to repo

# now two important steps
# first, stage file
git add "filename" # tracks the file, stages for commit

# now check status
git status # will say "changes to be commited"

# simplest way to commit, use -m flag
git commit -m "detail about the commit"

# then get the log: histroy of commits
git log


# to revert changes (new)
git checkout <commmit hash> # you get the hash from the command
# git log

# then you see a long message
# then you'll see that your code reverted

# have a crazy idea, make use of a branch, basically just 
# for yourself, don't wanna endanger master branch
# to list branch
git branch

# to create a new branch 
git branch "branchname"

# to go to that branch
git checkout "branchname"

# now make some drastic changes

git add . # adds everything
git commit -m "cool"

git log # now see the changes, now you can see commits back
# in master AND in curent branch
# but if you checkout to master, and git log, you can't see
# the changes in the new branch!

# so once you're happy with the changes you made in your
# new branch, you wanna MERGE!
# go to master branch and now,
git merge "branchname"

# then if you git log
git log # you see changes in both the new branch and master!!





