# usage
`vim <filename>`

* no mouse need for vim :p

## to exit vim
`:q`: quit
`:wq`: save and then quit
`:q!`: to quit without saving

## to move cursor around
`k`: go up
`j`: go down
`l`: go right
`h`: go left

* you can hold the keys down
* by default you are in **command** mode!

## to get into insert mode
`i`

## to get back to command mode
`Esc`

## to go all the way down
`G`

## to go back up 
`g`

## to skip blocks of code
### to go down a block
`}`
### to go up a block
`{`

## cool tip: specify iterations (number) before letter!
`10l`: go down 10 lines

## to delete a line
escape out first and then `dd`

## to undo
`u`: unravel each undo

## to redo
`^r`

## to redo the same action
`.`

## to copy and paste lines of code
`y`: to copy
`p`: to paste

## to select multiple lines (recommended when deleting something because you can visually see what's selected before deleting them)
`^v`, and then move cursor (`hjkl`)

## to add new line and puts you in insert mode
`o`
`O`: adds a line ABOVE your cursor

# now some horizontal movements
## to move word by word (use capitalized w and b to ignore punctuations!)
`w`: forward
`b`: backward

## to go to a specific line
`:20` go to line 20

## to go to a certain point in a line
`0`: takes you to the very beginning of the line
`^`: takes you to the first word of the line
`$`: go to the end of the line
`f!`: go to `!` in the line, can specify what you want
`%`: if you're on the left parenthesis, will go to the right parenthesis!

* `d` is for deleting
* `c` is for changing

## to delete the rest of the line
`D`: deletes everything to the right of the cursor

## to change something
`cw`: change word, gets rid of word and goes into insert mode

## to change up to a certain thing
`ct}`: deletes everything up to the curly brace! same goes to deleting
`dt}`: deletes everything up to the curly brace!

## to find all the same words 
`*`

## to go to the next instance of the same letter
`;`: say you wanna go to a letter but there are multiple letters in the same line, will go to the next letter if the same! (use of t or f)

## miscellaneous 
### to capitalize
`~`: swap the case
### to capitalize multiple
`5~`: swap the case of the next 5 letters

### the period command
`.`: redo the last action you did. say you renamed something to bob, it will rename things to bob wherever your cursor is and you press `.`

# Review use of `t` and `f` (unsure of their usage, seems powerful)


















