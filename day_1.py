"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
sample_data: list[str] = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]

with(open("day_1_input.txt")) as f:
    data = f.readlines()

output: list[int] = []
for row in data:
    start = None
    end = 0
    for i in row:
        if i.isdigit():
            if start is None:
                start = i
            end = i

    value = int(f"{start}{end}")
    output.append(value)
print(sum(output))

"""
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""
sample_data: list[str] = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]

number_strings: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

number_mapping: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
statics: dict[str, int] = {
    "one": 900,
    "two": 900,
    "three": 900,
    "four": 900,
    "five": 900,
    "six": 900,
    "seven": 900,
    "eight": 900,
    "nine": 900
}

max_statics: dict[str, int] = {
    "one": -1,
    "two": -1,
    "three": -1,
    "four": -1,
    "five": -1,
    "six": -1,
    "seven": -1,
    "eight": -1,
    "nine": -1
}
with(open("day_1_input.txt")) as f:
    data = f.readlines()

output = 0
for row in data:
    indexes: dict[int, int|None] = {i:900 for i in range(10)}
    indexes.update(statics)

    # Handle integers
    for i in range(10):
        try:
            indexes[i] = row.index(str(i))
        except ValueError:
            pass
    
    # Handle strings
    for string in number_strings:
        try: 
            indexes[string] = row.index(string)
        except ValueError:
            pass
    found_values = {k: v for k, v in indexes.items() if v != 900}

    minval = min(found_values.values())
    start = [k for k, v in indexes.items() if v==minval][0]

    # Handle maximum values.
    max_indexes: dict[int, int|None] = {i:-1 for i in range(10)}
    max_indexes.update(max_statics)

    # Handle integers
    for i in range(10):
        try:
            max_indexes[i] = row.rindex(str(i))
        except ValueError:
            pass
    
    # Handle strings
    for string in number_strings:
        try: 
            max_indexes[string] = row.rindex(string)
        except ValueError:
            pass


    found_values = {k: v for k, v in max_indexes.items() if v != -1}
    print(found_values)
    maxval = max(found_values.values())
    end = [k for k, v in max_indexes.items() if v==maxval][0]

    try:
        start_mapped = number_mapping[start]
    except:
        start_mapped = start
    try:
        end_mapped = number_mapping[end]
    except:
        end_mapped = end
    value = int(f"{start_mapped}{end_mapped}")
    print(value)
    output += value

print(output)