# Must-know VIM commands!

## Movement
* `hjkl`
* `H`: puts cursor at top of screen
* `M`: puts cursor in the middle of screen
* `L`: puts cursor at the bottom of screen
* `w`: puts cursor at start of next word
* `b`: puts cursor at start of prev word
* `e`: puts cursor at end of word
* `0`: puts cursor at beginning of line
* `$`: puts cursor at end of line
* `)`: takes you to start of next sentence
* `(`: takes you to start of prev sentence
* `}`: takes you to start of next paragraph or text block
* `{`: takes you to start of prev paragraph or text block
* `^f`: takes you one page forward
* `^b`: takes you one page back
* `gg`: puts cursor at start of file
* `G`: puts cursor at end of file
* `#`: where `#` is the line number, this will take you to the line specified (relative to current position of cursor)

## Editing
* `yy`: copies a line
* `yw`: copies a word
* `y$`: copies from cursor to end of line
* `v`: highlights one character at a time using arrow buttons or `hjkl` (enters **VISUAL** mode)
* `V`: highlights **one line**, and movement keys can allow you to highlight additional lines
* `p`: paste whatever has been copied
* `d`: deletes highlighted text
* `dd`: deletes a line of text
* `dw`: deletes a word
* `D`: deletes everything from cursor to end of line
* `d0`: deletes everything from cursor to start of line
* `dgg`: deletes everything from cursor to start of file
* `dG`: deletes everything from cursor to end of file
* `x`: deletes a character (after cursor i think)
* `u`: undo last operation
* `^r`: redo last undo
* `.`: repeats last action

## Searching! 
* `/<keyword>`: searches whatever `keyword` is
* `n`: searches text again in forward direction
* `N`: searches text again in opposite direction
* `:%s/[pattern]/[replacement]/g`: replaces all occurrences of `pattern` **without confirming**