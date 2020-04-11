# shell scripting tutorial by Derek Banas

# VIM
# to save vim file
:w
# to save vim file and then quite
:wq
# to quit and discard any changes
:q!

# while not in insert mode
# to move cursor down
w
# to move cursor up
b
# to move start of line
0
# to the end of line 
$
# to the beginning of the last line
G
# to get into insert mode, gets you to the end of the line too
A
# once in insert mode, can move around with arrow keys

# get out of insert mode
# to number each line 
:set number 
# to turn syntax highlightin on
:syntax on
# can decide how many spaces with a tab
:set tabstop=2
# set autoindent
:set autoindent

# to delete multiple lines in vim
V 
# then highlight any line below using the down button
# when done highlighting the lines you wanna delete
d

# to enter insert mode
i 

# always begin script with
#!/bin/bash
# means you're telling the system you wanna use bash

# use # for comments

# to execute 
./ # file name

# let's definite variables
myname="Derek"
# remember, no white spaces on either side of the equal sign

# variable names start with letter or underscore

# to declare a constant
declare -r NUM1=5

num2=4

# to do arithmetic, you need dollar sign
# also the double parentheses
num3=$((NUM1+num2))

# to copy that whole line
V
# to copy
y
# to past, remember do this NOT in insert mode
P

# to print
echo 

# for exponents
**
# for modules 
%

# assignment operators
i += 2 # same as i = i + 2
# also
-=
*=
/=
%= # maybe exists

# to increment and decrement
# to do: understand ++ and -- 03/26/2020















