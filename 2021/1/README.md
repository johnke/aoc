# Day 1 Commentary

Part 2 of this called for a `three-measurement sliding window`, which they illustrated like this:

```
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
```

Now, I'm not sure if you've spotted this about me, but I'm not actually a trained programmer, so the words "sliding window" don't really mean much to me. So my first instinct was to try and recreate the illustration exactly (i.e. assign `199` to `A` and `200` to `A` and `B` etc.) and figure it out from there.

My final code could be a _lot_ better but I don't mind, I'm just happy with how held off on my first instinct here.
