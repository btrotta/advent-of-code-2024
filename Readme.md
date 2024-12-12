# Advent of code 2024

Notes on selected problems.

## Day 5

Note that the order for all possible pairs of pages is specified (i.e. the length of the order instructions 
is ($n$ choose 2) where $n$ is the number of unique pages in the updates). So we can use the order to build a comparator 
for sorting.


## Day 6

For part b, note that potential new obstacles must be on the original path found in part a (otherwise the guard would 
just travel the same route as in part a). This restricts the number of locations we need to check.

## Day 7

Use depth-first search to evaluate "paths" of operators. Since each operation increases the sum, we can stop checking 
a path if the current sum already exceeds the target.


## Day 9

The checksum can be calculated efficiently by using Gauss' method to sum a range of consecutive numbers. Calculate the
original checksum while parsing the original file layout, then update it as files move.

## Day 10

Use breadth-first search. In part a, we only need to find a single path from each trailhead, so we do not need to re-visit 
previously visited locations. In part b, we want to find all the paths, so we do re-visit previously visited locations.

## Day 11

For part a, we can calculate the list directly. For part b, this is no longer feasible. However, we can use dynamic programming
with caching. Note that for a number `n` whose length `k` is a power of 2, after  `log2(k)` blinks it will be transformed into a list of single-digit numbers.
Now, for numbers < 5, the output after 1 blink is either 1 (if the original number is 0), or a 4-digit number, 
and for numbers between 5 and 9, the output after 2 blinks is an 8-digit number. So, in either case, after a small number of blinks, 
the original number is transformed into a list of single-digit numbers. For numbers between 10 and 99, after a single blink we have a list of 2 single-digit numbers. This 
allows us to speed up our calculation by caching results for numbers < 100.
For each member of the original array, we recursively calculate the size of the array it generates after 75 blinks. During the calculation, 
we cache results for pairs `(number, num_blinks)` where `number < 100`.

## Day 12

Note that since different regions can have the same labels, we first simplify the array by relabelling distinct regions with distinct labels.
We can do this by considering it as a graph and finding the connected components. For part a, we can then find the perimeters by iterating 
over the array and, for each location, counting which of its neighbours have a different value.
For part b, iterate separately over rows and columns, considering the edges between subsequent pairs of rows/columns.
There will be a horizontal fence between 2 rows wherever the values are different across the rows (and similarly for the columns).
When travelling along a row, a new side of a region starts either at the beginning of a section of fence 
(i.e. where the current position has a horizontal fence above/below it, but the position to the left does not), 
or when the region changes (i.e. the current position has a horizontal fence above/below it, and the postion to the left 
belongs to a different region).
