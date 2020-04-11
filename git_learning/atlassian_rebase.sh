# git rebase tutorial

# got rebase is one of two git utilities that specializes in 
# integrating changes from one branch onto another
# the other change integration? merge.

# merge is always a forward moving change record
# alternatively, rebase has powerful history rewriting features

# rebase has 2 main modes
# manual and interactive

# what is git rebase?
# the process of moving or combining a sequence of commits 
# to a new base commit
# from a content perspective, rebasing is changing the
# base of your branch from one commit to another,
# making it appear as if you'd created your branch from 
# a different commit

# two options for integrating your feature into the
# master branch:
# 1. merging directly
# 2. rebasing and then merging

# Option 1 results in a 3-way merge and a merge commit
# Option 2 results in a fast-forward merge and a 
# perfectly linear history

git rebase <base>
# git rebase in standard mode will automatically take the commits
# in your current working branch and apply them to 
# the head of the passed branch

# this automatically rebases the current branch onto
# <base>, which can be any kind of commit reference

