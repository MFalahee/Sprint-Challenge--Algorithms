#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This one is O(n) because as the input grows, the runtime of the loop grows at ( or about) the same rate each time.
    for example n = 2, 2 iterations of the loop
    n = 3, 3 iterations of the loop
    n = 4, 4 iterations

b) This one is O(n^c) because there are two loops, and for each item in the first loop it iterates through the entire input in the second loop. This function will get out of hand with the number of operations really fast in comparison to the first example.

c) This one, even though it's recursive, is still O(n) because it only increases by one recursive call for each corresponding increase in input.

## Exercise II

I'd approach this problem like a Binary Search.

Start at the middle floor, len(n//2) and check if an egg breaks. 

  If it doesn't, check if an egg breaks on (f+1).
    if it does break, your highest floor is F.
    if not, toss the floors to the left out, and do it again with the array to the right.
  
  If it does, check if an egg breaks on (f-1) 
    if not, Your highest floor is F.
    if so, toss the floors to the right of F out, and run it again.

Keep going until the second condition is met with breaking or not breaking. That's the threshold for the floor you want.

This problem would be complexity O(log(n)) because we are dividing N in half every time we recursively call the search again. This makes it slightly more efficient than O(n) or an iterative search.