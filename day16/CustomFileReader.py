class FileReaderIterator:
    def __init__(self, filename, chunk_size=3):
        self.file = open(filename, "r")
        self.chunk_size = chunk_size
        self.lines = []

    def __iter__(self):
        return self

    def __next__(self):
        self.lines = []

        for _ in range(self.chunk_size):
            line = self.file.readline()
            if not line:
                break
            self.lines.append(line.strip())

        if not self.lines:  # No more lines
            self.file.close()
            raise StopIteration

        return self.lines


# Create a sample file (for testing)
with open("sample.txt", "w") as file:
    file.write(
        "Line 1\nLine 2\nLine 3\nLine 4\n"
        "Line 5\nLine 6\nLine 7\nLine 8\n"
    )


# Using the iterator
reader = FileReaderIterator("sample.txt", chunk_size=2)

print(next(reader))  # ['Line 1', 'Line 2']
print(next(reader))  # ['Line 3', 'Line 4']
print(next(reader))  # ['Line 5', 'Line 6']
print(next(reader))  # ['Line 7', 'Line 8']
