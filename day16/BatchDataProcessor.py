

class BatchDataIterator:
    def __init__(self, filename, batch_size=3):
        self.file = open(filename, "r")
        self.batch_size = batch_size

    def __iter__(self):
        return self

    def __next__(self):
        batch = []

       
        for _ in range(self.batch_size):
            line = self.file.readline()
            if not line:
                break
            batch.append(line.strip())

       
        if not batch:
            self.file.close()
            raise StopIteration

        return batch


with open("students.txt", "w") as file:
    file.write(
        "Alice 85\n"
        "Bob 90\n"
        "Charlie 78\n"
        "David 92\n"
        "Emma 88\n"
        "Frank 76\n"
        "Grace 91\n"
    )



processor = BatchDataIterator("students.txt", batch_size=2)

print(next(processor))   
print(next(processor))  
print(next(processor))   
print(next(processor))   
