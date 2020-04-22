# Why Vim
* ubiquitous
* scalable
* powerful

# Verbs
Basically actions we can take, that can be perfomed on nouns
* `d`: delete
* `c`: change
* `y`: yank (copy)
* `v`: visually select (V for line vs. character)

# Modifiers 
Used before nouns to describe the way in which you're going to do something
* `i`: inside
* `a`: around
* `NUM`: any number
* `t`: searches for something and stops **before** it
* `f`: searches for that thing and lands **on** it
* `/`: find a string (literal or regex)

# Nouns
Basically objects you do something to!
* `w`: word 
* `s` or `)`: sentence
* `p` or `}`: paragraph
* `t`: tag (think HTML/XML)
* `b`: block (think programming)

# Some *good* examples to get you going
## to delete two words
`d2w`

## to copy the paragraph you're in 
`yip`: y to copy, p to paste

## to change text till first open bracket
`ct<`: deletes text till first open bracket and puts you in insert mode

# Working with your file
`:q!`: to quit vim without saving file
`saveas ~/some/path/`: to save file to a specific location
`ZZ`: faster way to do `:wq` lmao

# Searching your text (very powerful)
## Searching by string
Basically what `Ctrl` + `f` does outside Vim. Do this:
`/<something>` then hit `Enter`   

Then,
`n`: to go to next instance of result
`N`: to go to previous instance of result  

## Jumping to certain characters
### To jump forward and land **on** "<" character (find)
`f<`

### To jump forward and land **right before** the "<" character (to)
`c<`

## A search reference
* `*` search for other instances of the word under your cursor
* `;`: go to next instance when you've jumped to a character. `,` goes the opposite direction!

# Moving around text
## Basic shit
Know your `hjkl`. `k` goes up.

## Moving **within** same line
* `0`: go to beginning
* `$`: go to end
* `^`: move to first non-blank character

## Moving by word (yes)
* `w`: move forward one word (think about how you move forward in fps games)
* `b`: move back one word
* `e`: move to the **end** of your word (i guess this is useful for **very long** words)
* `W`: ignore delimeters while moving forward one word
* `B`: ignore delimeters while moving back one word

## Moving sentence or paragraph
`)`: move forward one sentence
`}`: move forward one paragraph

## Moving within screen
`H`: move to top
`M`: move to middle
`L`: move to bottom
`gg`: go to topp of file
`G`: go to bottom of file
`^U`: move up half a screen
`^D`: move down half a screen
`^F`: page down
`^B`: page up

## Jumping back and forth
* `^I`: jump to your previous navigation location
* `^O`: jump back to where you are

# Changing text

## Basic change/insert options
* `i`: insert before cursor
* `a`: append after cursor
* `I`: insert at beginning of line
* `A`: append at the end of line
* `o`: open a new line below the current one
* `r`: replace the one charater under your cursor
* `R`: replace the character under your cursor, but just keep trying afterwards

# Delete text

## Basic deletion options
`x`: exterminate (delete) the character after the cursor
`X`: exterminate (delete) the character before the cursor
`dd`: delete current line
`dt.`: delete from where you are to the period
`D`: delete to the end of the line

# Copy and Pasting

## Copying text
`y`: copy (yank) whatever's selected
`yy`: copies current line

## Pasting text
`p`: to paste after cursor
`P`: to paste before cursor




