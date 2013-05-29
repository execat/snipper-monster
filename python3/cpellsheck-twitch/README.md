# Problem

Write a program that reads a large list of English words (e.g. from /usr/share/dict/words on a unix system) into memory, and then reads words from stdin, and prints either the best spelling suggestion, or "NO SUGGESTION" if no suggestion can be found. The program should print ">" as a prompt before reading each word, and should loop until killed.

Your solution should be faster than O(n) per word checked, where n is the length of the dictionary. That is to say, you can't scan the dictionary every time you want to spellcheck a word.

For example:

    > sheeeeep
    sheep
    > peepple
    people
    > sheeple
    NO SUGGESTION

The class of spelling mistakes to be corrected is as follows:

* Case (upper/lower) errors: "inSIDE" => "inside"
* Repeated letters: "jjoobbb" => "job"
* Incorrect vowels: "weke" => "wake"
* Any combination of the above types of error in a single word should be corrected (e.g. "CUNsperrICY" => "conspiracy").

If there are many possible corrections of an input word, your program can choose one in any way you like. It just has to be an English word that is a spelling correction of the input by the above rules.

Final step: Write a second program that *generates* words with spelling mistakes of the above form, starting with correctly spelled English words. Pipe its output into the first program and verify that there are no occurrences of "NO SUGGESTION" in the output.

# Execution

The script has been written in Python 3 (doesn't run on Python 2).

The cpellerror script creates error-words for 500 randomly selected words from words-5k file. It prints the original word (that has been modified) to STDERR, and the modified word to STDOUT.

The cpellsheck script checks the input-words for infinitely long sequence until "quit" is typed by the user. Can also accept inputs from the cpellerror script, and print the output.

This entire process has been automated in execute.sh. Just ./execute.sh with proper utilities installed.
