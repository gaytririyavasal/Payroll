PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Bowling is the world's number one participation sport! It is the only sport that takes place on all seven continents, including McMurdo Station in Antarctica!

As a way of making bowling leagues more fun for beginners, bowlers are often assigned a handicap so that beginning bowlers may compete more evenly with experienced bowlers. The handicap is calculated based on the bowler's average; the higher the average, the lower the handicap. For example, a bowler with an average of 100 may have a handicap of 80, and a bowler with an average of 150 may only have a handicap of 40. When the two bowlers compete against each other, their handicaps are added to their respective scores to determine the winner. The higher bowler still has an advantage (if they both bowl their averages exactly, the 150 + 40 = 190 will beat the 100 + 80 = 180) but the match is clearly much closer. If the 150 bowler bowls exactly 150, the 100 bowler need only bowl a 111 to win instead of a 151.

Algorithm

Every bowling league may define the way handicap is calculated with their own methodology. However, most typical leagues use a formula such as the following:

       handicap = (200 - average) * 80%
   
Here the bowler's average (a floating-point number) is truncated to an integer, and the handicap is also truncated to an integer.

Note that this previously said "truncated to the next lowest integer," but that's not quite right. That's what the floor() function does. But apparently, they just throw away the non-integer part. For negative numbers, that's not the next lowest integer, it's the next highest integer. Use the int() function rather than the floor() function and it will do the right thing.

For example: if a bowler in the above league had a 147.8 average, you would calculate her handicap as follows:

       average = 147 (147.8 truncated)
       handicap = (200 - average) * 80%
                = (200 - 147) * 80%
                = 53 * 80% = 42.4
   
which is then truncated to 42.

Assignment and Expected Output:

Write a complete Python program that calculates a bowler's average and handicap after three games. Using input statements, prompt for the user's first name and the scores of three bowling games (integers between zero and 300 inclusive) one at a time. Then calculate the bowler's average and handicap using the formula above. Print out a nicely formatted report of the bowler's average and handicap, truncated to integers. The function int() will truncate a float to an int. For a positive number it rounds down; for a negative number it rounds up (toward zero). See the examples below for the format.

The sample below shows three runs of the program. (Your code only has to handle one bowler, not three!) Format your output so that, if you were to use the same inputs, your output would match the following exactly. Notice that the handicap may be low and could even be negative. There should be one space after each colon (where something follows on the line) and a single blank line above and below the output in addition to the blank lines internal to the report. There are two spaces at the start of the average and handicap lines.

> python Handicap.py

Enter bowler's name: Bernard
Enter Game 1: 200
Enter Game 2: 184
Enter Game 3: 210

Handicap report for Bernard:
  Bernard's average is: 198
  Bernard's handicap is: 1

It's time to Bowl!

> python Handicap.py

Enter bowler's name: Cindy Lou
Enter Game 1: 50
Enter Game 2: 82
Enter Game 3: 75

Handicap report for Cindy Lou:
  Cindy Lou's average is: 69
  Cindy Lou's handicap is: 104

It's time to Bowl!

> python Handicap.py

Enter bowler's name: Tom Daugherty
Enter Game 1: 300
Enter Game 2: 295
Enter Game 3: 287

Handicap report for Tom Daugherty:
  Tom Daugherty's average is: 294
  Tom Daugherty's handicap is: -75

It's time to Bowl!

> 
