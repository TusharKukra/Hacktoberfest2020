from bisect import bisect_left
def BinSearch(a, x):
   i = bisect_left(a, x)
   if i != len(a) and a[i] == x:
      return i
   else:
      return -1
a = [2, 3, 4, 4, 5, 8, 12, 36, 36, 36, 85, 89, 96]
x = int(4)
pos = BinSearch(a, x)
if pos == -1:
   print(x, "is absent")
else:
   print("First occurrence of", x, "is at position", pos)
