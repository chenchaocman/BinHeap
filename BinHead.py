# -*- coding: utf-8 -*-

class BinHeap:

    def __init__(self):
        self.heapList = [0]
        self.N = 0

#上浮
    def swim(self,i):
        while (i>1)and(self.heapList[i]>self.heapList[i//2]):
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
                i = i//2
#下沉
    def sink(self,i):
        while i<self.N:
            j = i*2

            if j>self.N:
                break

            if self.heapList[j]<self.heapList[j+1]:
                j+=1
            if self.heapList[i]<self.heapList[j]:
                self.heapList[i],self.heapList[j]=self.heapList[j],self.heapList[i]
            i = j

#插入元素
    def insert(self,n):
        self.heapList.append(n)
        self.N =self.N+1
        self.swim(self.N)
#删除元素
    def delteMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.N]
        self.N = self.N - 1
        self.heapList.pop()
        self.sink(1)

    def BuildHeap(self,alist):
        self.N = len(alist)
        self.heapList = [0] + alist





if __name__ == '__main__':
    print("1111")
    bh = BinHeap()
    bh.BuildHeap([9, 6, 3,2, 1])
    bh.insert(100)
    bh.insert(-100)
    bh.insert(300)
    bh.delteMax()
    print(bh.heapList[1])





















