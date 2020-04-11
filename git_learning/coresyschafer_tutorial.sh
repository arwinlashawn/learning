# video title
# git tutorial for beginners: command_line fundamentals

# git is a distributed version control system (vcs), not a central
# vcs
# every contributor has a copy of the repo

# to set config values
git config --global user.name "name"
git config --global user.email "email address"

git config --list # to check the configuration values, mainly
# your name and email address

# to get help for config
git help config
# or 
git config --help
# other e.g.
git add --help # opens a tab for help lol
git add -h # opens help in the terminal

# to begin tracking the codes in a directory
# cd into the dir, then
git init
# you will see a .git directory, meaning that it's being
# tracked

# if you every wanna stop tracking the repo
rm -rf .git

# to see untracked files, tells you which branch you're on too
git status

# you sometimes wanna ignore certain files
# do this, this creates .gitignore file!
# it's a simple text file that contains files that you want
# git to ignore
touch .gitignore
# in the .gitignore file, you can put in extensions/wildcards
# e.g. .project, *.pyc

# to add files to staging area
git add -A # to add everything to staging area
# all of the files now in staging area
git status

# if you wanna remove files from the staging area
git reset "file" # this file will then be in untracked

# to remove every file from staging area
git reset

# to commit files
# message is important! give details of changes
git commit -m "message"

# after committing
git status # and you should see "nothing to commit, working
# directory clean"

# to see log
git log # you will see author and time commit was made


# CLONING A REMOTE REPO
git clone <url> <where to clone>

# after cloning the remote repo
# to view some info about it
git remote -v # gives branch and corresponding location
git branch -a # lists all branches in repo both locally and remotely

# to push changes
# make a change to your code
# FIRST, commit the changes locally
git diff # shows changes you've made to the code
git status # will show the status "modified"
git add -A
git status # will show changes to be committed
git commit -m "message"

# now you wanna push the changes to the remote repo
# 2 things you wanna do
# YOU NEED TO PULL FIRST (important) and then push
# pull gets any changes made since the last time we pulled
# from the repo
git pull origin master # it will say already up to date,
# then good to go
git push origin master # pushes the changes!

# now let's have a look at common workflow
# you wanna work in a different branch
# first create a branch for desired feature
git branch "new branch" # no quotes needed!
git branch # gonna list all your local branches
# you'll see master branch, has an asterisk
git checkout "new branch" # will switch to the branch specified in
# name
git status
git add -A
git commit -m "message"
# this results in no effect on local master branch
# also no effect on remote repo
# only affects local branch specified

# after commit, PUSH BRANCH TO REMOTE
git push -u origin "new branch" # pushes new branch to remote repo
git branch -a # to see all your branches
# you'll see you remotes/origin pointing to your new branch
# usually unittests are done on non-master branch
# after passing tests, then merge to master branch!
git checkout master
git pull origin master # if says up to date
git branch --merged # lists the branches that we've merged in so far
# see that new branch doesn't pop up yet
# we wanna merge new branch with master
git merge "new branch"
# now push changes to master branch!
git push origin master

# to check if everything was successfully merged
git branch --merged
# sees new branch, that's good
# now delete that new branch, cuz we don't need it anymore
git branch -d "new branch" # deletes the new branch locally
# BUT we still have the new branch on the remote repo
git branch -a # see that the new branch is still on remote repo
git push origin --delete "new branch"
git branch -a # will see that we just have the local
# and remote master branch

# FASTER EXAMPLE
git branch subtract
git checkout subtract # working on subtract branch
git status
# make a change to code
git add -A
git commit -m "made some changes"
git push -u origin subtract
git checkout master
# now ready to merge with master branch
git pull origin master # pull all the changes
# nowMERGE
git merge subtract
git push origin master
# now delete the new branches in both remote and local















