
## Solutions so far:

 * Day 1 Part 1 `day_1/part_1.py`
 * Day 1 Part 2 `day_1/part_2.py`
 * Day 2 Part 1 `day_2/part_1.py`
 * Day 2 Part 2 `day_2/part_2.py`
 * Day 2 Part 2 `day_1/part_1.py`
 
 ## How to run

 Make sure you have Python3 installed.  You can use `python aoc2021.py --help` to get the following:

 ```
 usage: aoc2021.py [-h] [--debug] [--sub] [--all] day part

positional arguments:
  day         The Day we want to process
  part        Which part we're using

optional arguments:
  -h, --help  show this help message and exit
  --debug     Will add some extra output to add to the confusion
  --sub       Prints the sub
  --all       Runs all of the solutions! You still need to set the day and part, because I haven't worked out how to make these args optional
  ```

Examples:
 * `python aoc2021.py 1 1` - runs Day 1 Part 1
 * `python aoc2021.py 1 1 --all` - runs all solutions
 * `python aoc2021.py 1 1 --debug` - shows extra debug info (and possible limits the number of loops depending on the solution)
 