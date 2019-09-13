#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I


```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

a) This one is O(n) because as the input grows, the runtime of the loop grows at ( or about) the same rate each time.
    for example n = 2, 2 iterations of the loop
    n = 3, 3 iterations of the loop
    n = 4, 4 iterations


b) This one is O()


c) 

## Exercise II


