class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.isEmpty():
            print("Stack Kosong")
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def printAll(self):
        if self.isEmpty():
            print("Stack Kosong")
        else:
            print(*self.data, sep="-")


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
