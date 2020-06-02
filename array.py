class myArray: 
    def __init__(self):
        self.length = 0
        self.data = {}
        
    def __str__(self):
        return str(self.__dict__)

    def get(self,index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length+=1
        return self.length

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastItem

    def delete(self,index):
        item = self.data[index]
        self.shiftItems(index)
    
    def shiftItems(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length-=1


newArray = myArray()
# print(newArray.get(0))
newArray.push(1)
newArray.push(2)
newArray.push(3)
newArray.push("shit")
newArray.pop()
newArray.delete(1)
newArray.delete(1)
# newArray.pop()
# newArray.pop()
print(newArray)
# print(newArray.get(2))
