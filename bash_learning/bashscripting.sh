# based on an article
# https://itnext.io/bash-scripting-everything-you-need-to-know-about-bash-shell-programming-cd08595f2fba
# focus on programming spec and not how different
# UNIX command works

# Bash aka Bourne Again Shell
# an interpreter that process shell commands
# a shell interpreter takes commands in plain 
# text format and calls OS services to do something
# e.g.
ls # commands lists the files and folders in a dir

# Bash is the IMPROVED version of Sh (Bourne Shell)

# What is shell scripting?
# writing a program for the shell to execute

# What is a shell script?
# a file or program that shell wille execute

# a shebang or hashbang at the top of a file enables
# us to direcrtly execute it like a binary (this declares
# the interpreter)

# the shebang
#!/usr/bin/env bash OR #!/usr/bin/bash
# DIFFERENCE BETWEEN THE TWO! so for /usr/bin/env,
# 1) Running a command in this way has the benefit
# of looking whatever the DEFAULT version of the program
# is in your CURRENT env
# 2) Downside to /usr/bin/env is you can't pass more  
# than one argument!
# 3) Another downside: since you aren't calling an 
# EXPLICIT EXECUTABLE, it has potential for mistakes
# 4) if security is the focus, latter is preferred (limits)
# code injection possibilities

# Bash DOES NOT have a type system
# only saves STRING values

# echo command adds a space AUTOMATICALLY between
# two adjacent args in the output by default

# to print a declared variable: put $ as prefix to var

# to write multiple commands on a single line, use
# ";" as the command sep

# to concat two strings together, can use +- operator

# Bash supports both single-quotes and double quotes to
# define a string BUT
# only double quotes support string interpolation
# i.e. ${"some string"}
# STRING INTERPOLATION: process of evaluating a string
# literal containing one or more placeholders, giving 
# a result in which placeholders are REPLACED with their
# corresponding values

args # prints the number of arguments passed to the var
# e.g.
NAME="John Doe Jr"
args $NAME # should give 3 # not working on Git Bash 
# even after installation KIV

# remember, wrapping a var in DOUBLE QUOTES helps 
# solve problems like printing var which contains
# strings with special characters like *

# can use "\" to escape
# e.g. having double quotes within double quotes
# \ BEFORE whatever you wanna escape
echo "I am 'John' and I am \"AWESOME\"."

# ARITHMETIC OPERATIONS
# possible even though Bash doesn't support NUMBER data
# type
# using the let command
let RESULT=1+1
echo $RESULT # gives 2
# BUT if you do 1 + 1, + will be a command. so be SAFE 
# and write it in quotes!!
let RESULT="1 + 1"
echo $RESULT 
# let: evaluates the expression in a string


