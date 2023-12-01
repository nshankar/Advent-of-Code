#!/usr/bin/env python3
with open("test") as f:
   data = f.readlines()
   print(data)

   # solution is to build the tree O(N)
   # Accumulate the size of the branches O(N)
   # Sum entries < 10^5 O(N)
   # Will do later on
