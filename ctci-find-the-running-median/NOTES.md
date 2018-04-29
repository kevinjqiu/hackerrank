naive approach
==============

Just take medium point if len(a) is odd and take average of a[medium-1] and a[medium] if len(a) is even

However this did not take into account that the median should be the middle point of the sorted array

Use a heap
==========

Use a heap to always keep the list sorted. 

Take the median is approximately O(n/2), and with n input numbers, it's O(n^2)

Obviously this is still too slow for large sets

