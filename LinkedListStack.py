from SLLNC import SLLNC

class Stack:
    def __init__(self):
        self.data = SLLNC()

    def __len__(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0

    def push(self, data):
         self.data.addElementTail(data)
    
    def pop(self):
        if self.isEmpty():
            print("Stack Kosong")
        else:
            hapus = self.data._tail._element
            self.data.deleteLast()
            return hapus
    
    def top(self):
        if self.isEmpty():
            print("Stack Kosong")
        else:
            return self.data._tail._element
    
    def printAll(self):
        if self.isEmpty():
            print("Stack Kosong")
        else:
            helper = self.data._head
            output = ""
            for _ in range(len(self.data)):
                output += " "+ str(helper._element)
                helper = helper._next
            print(" - ".join(output.split()))


if __name__ == "__main__":
    st = Stack()
    st.push(12)
    st.push(23)
    st.push(34)
    st.push(45)
    st.push(56)
    st.push("12")
    st.pop()
    st.pop()
    st.push(55)
    st.push(88)
    st.pop()
    st.push("23")
    st.push("97")
    print("Data teratas: ", st.top())
    print("Panjangnya: ", len(st))
    st.printAll()
