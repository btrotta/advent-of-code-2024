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

Since different regions can have the same labels, we first simplify the array by relabelling distinct regions with distinct labels.
We can do this by considering it as a graph and finding the connected components. For part a, we can then find the perimeters by iterating 
over the array and, for each location, counting which of its neighbours have a different value.
For part b, iterate separately over rows and columns, considering the edges between subsequent pairs of rows/columns.
There will be a horizontal fence between 2 rows wherever the values are different across the rows (and similarly for the columns).
When travelling along a row, a new side of a region starts either at the beginning of a section of fence 
(i.e. where the current position has a horizontal fence above/below it, but the position to the left does not), 
or when the region changes (i.e. the current position has a horizontal fence above/below it, and the position to the left 
belongs to a different region).

## Day 13

This requires solving a system of 2 linear equations. The only complications are that we need to check that the solution 
is positive and integer-valued, and for part b, because the solutions can be very large we need to use 64-bit integers.

## Day 14

For part b, plotting a hundred or so examples shows that in some cases the robots are not evenly distributed but mostly in 
one half of the plot vertically or horizontally. Therefore I guessed that the Christmas tree must appear in one of these cases. 
I plotted the cases where the distribution was significantly different in the 2 vertical or horizontal halves, and checked them 
manually.

## Day 15

For part b, we need to treat horizontal and vertical moves differently. A horizontal move still can move only a single row
of boxes, but a vertical move can move a block of boxes, not just a single column, since boxes in adjacent rows can have 
overlapping horizontal dimension. So for each potential vertical move, we need to check that all boxes in the leading edge of the moving block
have a space to move into.

## Day 16
For part a, we can use Dijkstra's algorithm to find a shortest path. Since changing direction has a cost, we consider a "node" of 
the graph to be a pair `(location, direction)`. For part b, we need to modify the algorithm to find all paths.

## Day 17
For part b, I don't think there's a general algorithmic solution. I solved it by figuring out by hand the operation 
of the program and writing it as a simple function, which allowed me to automate the search for the answer. But my solution 
depends a lot on specifics of the program (e.g. that it only ever jumps from the end to the start), so I don't know how
generalisable this is.

## Day 18
Use breadth-first search to find shortest paths. For part b, after adding a block, if the block does not lie on the current shortest 
path we do not need to run the path-finding algorithm again since the current path will still work.

## Day 19
For part a, use depth-first search. For part b, use dynamic programming to recursively calculate the number of ways of 
making the first `n` colours of the design.
