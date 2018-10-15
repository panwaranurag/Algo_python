import unittest
class MergeSort(object):
    def merge_sort(self, arr, l, r):

        if l < r:
            # Same as (l+r)/2, but avoids overflow for
            # large l and h
            m = (l + (r - 1)) // 2

            # Sort first and second halves
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m + 1, r)
            self.merge(arr, l, m, r)
        return arr

    def merge(self, arr, l, m, r):
        n1 = m-l+1
        n2 = r-m


        L = [0]*(n1)
        R = [0]*(n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i, j, k =0,0,l
        while i < n1 and j < n2:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

c = MergeSort()

class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], c.merge_sort([4, 6, 1, 3, 5, 2], 0, 5))
        self.assertEqual([1, 2, 3, 4, 5, 6], c.merge_sort([6, 4, 3, 1, 2, 5], 0, 5))
        self.assertEqual([1, 2, 3, 4, 5, 6], c.merge_sort([6, 5, 4, 3, 2, 1], 0, 5))

