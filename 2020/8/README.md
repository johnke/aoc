## Day 8

I struggled a lot with part 2 here. Spent a lot of time trying to be smart and do a backward lookup of failing instructions, but in the end just a plain brute-force crack was the most straightforward. Shows in the time, too - first one that's gone above 80ms. Bah.

```
$ time python 1.py
Accumulator is: 1501

________________________________________________________
Executed in   28.78 millis    fish           external 
   usr time   19.70 millis  137.00 micros   19.56 millis 
   sys time    7.09 millis  369.00 micros    6.72 millis 
```

```
$ time python 2.py
509

________________________________________________________
Executed in   80.84 millis    fish           external 
   usr time   71.66 millis  170.00 micros   71.49 millis 
   sys time    7.01 millis  405.00 micros    6.61 millis 
```
