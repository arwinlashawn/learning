# leaning how to use git stash

git branch add # create a new branch

git checkout add # go into the new branch

git diff # see difference

# say for whatever reason, you need to urgently go into
# your master branch
# use stash!
git stash save "worked on add function"

# if you do
git diff # no diff seen

git status # all good

#but
git stash list # you will then see  the message " worked on 
# add function"

# if you wanna work on the stash
git stash apply "whatever you see on the stash list"

git stash list # you'll see the stash still there

git checkout -- . # just resets to where we were

# now let's do pop
git stash pop # grab the very first stash
# it applies the changes AND drops the stash unlike git stash
# apply, which doesn't drop the stash

# say we made a lot of changes to the calc function
git stash save "calc functions"
git stash list # make sure it's stashed

# make another small change
git diff # you'll see that change now

git stash save "added small change"

git stash list # now you can see another stash formed!
# cuz you didn't stash pop previously

# WHAT IF someone said they don't want the small change?
git stash drop "name of the staash related to small change"

git stash list # now we see only the big change stash

# say if you hate your stash, not needed
git stash clear # deletes all stash(es)







