# [Programming Exercises](http://www.dimagi.com/about/careers/exercises/)

These optional programming exercises give you a chance to show off your skills and creativity, and give us a chance to get a feel for how you go about solving problems. If you decide to give any of them a try, please submit your code (no need for extensive documentation or careful structure) along with the solution.

We’ve provided exercises in two categories, one covering general software development and one tailored to web development. You are welcome to attempt as many of these as you’d like, although if you submit more than one please include a single one you’d like us to review most closely. Understanding that you are probably quite busy, each category has a some quick exercises that we expect should take no more than 30 minutes; we’ve also included a more challenging exercise if you have more time.

## General

### Numeric Converter

Write a function that converts a (non-negative) integer into its spoken-language form.

    3 => "three"
    12 => "twelve"
    355 => "three hundred fifty five"

output language and maximum number supported are up to you

### String Rotation

Write a function that takes a string and returns a rot13 version of that string with every other word reversed. If the function is f, f(f(x)) should return x.  Remember to take non-alphanumeric non-alphanumeric characters into account.

    Example Input: “Hello world!”
    Example Output:”byyrU jbeyq!”

### Number Counting

Write a function that takes in a number N and counts how many numbers between 1 and N (inclusive) do not contain any digits which are ’7′.

### Set Combination (Challenging)

You’re given several lists of words. For example:

       * apple, banana, pear
       * car, truck
       * zambia, malawi, kenya

Print out all possible combinations of words, where one word is taken from each list, in the same order the lists are given. For example:

       * apple car zambia
       * apple truck kenya
       * pear car malawi
       * pear car kenya
    …

but not:

       * car zambia apple   (‘apple’ is in the first list; it should be the first word)
       * apple banana kenya   (two words taken from same list)
       * apple car   (one word must be taken from each list)

Each list will contain one or more words.
The total number of lists may vary; there will be at least one list.
Print each combination only once.
Write a function that accepts the word lists as a parameter, and either prints out or returns the word combinations. Write the solution in the language of your choice.

## Web Development
### Math Engine

Write a web based math engine. It should take the form of a running web service that takes in a single parameter GET or POST* called “values”, which is a JSON-formatted list of numbers.
The response should be a JSON dictionary with two values, the “sum” and the “product”.

    Example input: “values” = [1, 4, 7, -2] (will be either a url param for a GET or a post param for POST)
    Example output: {“sum”: 10, “product”: -56}

`* POST is optional

### (Challenge)

Write an additional endpoint to query the history with a second parameter asking how far back you want to go.

Should return a list of JSON objects formatted like the following:


    [{"ip": "127.0.0.1", "timestamp": 2011-06-09T17:46:21, "values": [1, 4, 7, -2], "sum": 10, "product": -56},
     {"ip": "127.0.0.1", "timestamp": 2011-06-09T17:25:23, "values": [1, 4, 7, -2], "sum": 10, "product": -56},
     {"ip": ...}, 
     {"ip": ...}, ...]
