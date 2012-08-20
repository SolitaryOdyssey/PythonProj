class InverseNumber:
    def MergeSort(self, arr):
        if len(arr) == 1:
            return [[arr[0], 0]]
        mid = (len(arr) - 1)//2
        firstHalf = self.MergeSort(arr[:mid+1])
        secondHalf = self.MergeSort(arr[mid+1:])
        result = self.Merge(firstHalf, secondHalf)
        return result

    def Merge(self, first, second):
        result = []
        fIndex = 0
        sIndex = 0
        for i in range(len(first)+len(second)):
            if first[fIndex][0] > second[sIndex][0]:
                first[fIndex][1] = first[fIndex][1] + len(second) - sIndex
                result.append(first[fIndex])
                fIndex = fIndex + 1
            else:
                result.append(second[sIndex])
                sIndex = sIndex + 1

            if fIndex == len(first):
                result = result + second[sIndex:]
                break
            elif sIndex == len(second):
                result = result + first[fIndex:]
                break
        return result

    def GetInverseNum(self,arr):
        self.invNum = 0
        self.final = self.MergeSort(arr)
        for num in self.final:
            self.invNum += num[1]
        return self.invNum

if __name__ =='__main__':
    inv = InverseNumber()
    print(inv.GetInverseNum([2,3,1]))
