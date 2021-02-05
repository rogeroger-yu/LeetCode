# solution 1
class Solution:
    def quick_sort(self, lists, l, r):
        if l < r:
            q = self.partition(lists, l, r)
            self.quick_sort(lists, l, q-1)
            self.quick_sort(lists, q+1, l)
        return lists

    def partition(self, lists, l, r):
        x = lists[r]
        i = l - 1
        for j in range(l, r):
            if lists[j] <= x:
                i += 1
                if i != j:
                    lists[i], lists[j] = lists[j], lists[i]
        lists[i+1], lists[r] = lists[r], lists[i+1]
        return i + 1

# solution 2
def quick_sort(lists,i,j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists


if __name__=="__main__":
    lists=[30,24,5,58,18,36,12,42,39]
    for i in lists:
        print(i,end =" ")
    for i in quick_sort(lists,0,len(lists)-1):
        print(i,end=" ")
