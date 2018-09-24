#Regex

#basic cheatsheet

#Anchors
```
* ^ -> Start of line
* \A -> Start of string
* $ -> End of line
* \Z -> End of string
* \b -> Word boundary
* \B  -> Word not boundary
* \< Start of Word
* \> End of word
```

#Character classes
```
\c -> Control character
\s -> White space
\S -> Not white space

\d -> Digit
\D -> not digit
\w -> word
\W -> not word
\xhh -> Hexadecimal character
\Oxxx -> Octal Character
```

#Regex for exercises
Text 1:
* Words that start by wowel:
```
(\b[aeiou](\s\w*))
```
* Words that start by wovel and have a preposition 'a':
```
\b[aeiou] \w*
```
