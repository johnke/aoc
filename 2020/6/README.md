```
$ time python 1.py
Sum of questions answered: 6596

________________________________________________________
Executed in   28.04 millis    fish           external 
   usr time   19.49 millis  153.00 micros   19.33 millis 
   sys time    6.35 millis  422.00 micros    5.93 millis
```

```
$ time python 2.py
Sum of counts: 3219

________________________________________________________
Executed in   31.64 millis    fish           external 
   usr time   23.02 millis  163.00 micros   22.85 millis 
   sys time    6.87 millis  419.00 micros    6.45 millis
```

---

Part 2 works and gives the right answer but it's the AOC challenge that I'm actually kind of embarrassed about. I've got a nest that goes `for` -> `if` -> `for` -> `for` -> `if` and I hates it. I'm reluctantly uploading it here as a cautionary tale for any other AOCers.
