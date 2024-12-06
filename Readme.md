# Advent of code 2024

Notes on selected problems.

## Day 5

Note that the order for all possible pairs of pages is specified (i.e. the length of the order instructions 
is ($n$ choose 2) where $n$ is the number of unique pages in the updates). So we can use the order to build a comparator 
for sorting.


## Day 6

For part b, note that potential new obstacles must be on the original path found in part a (otherwise the guard would 
just travel the same route as in part a). This restricts the number of locations we need to check.
