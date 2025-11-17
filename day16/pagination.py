class PaginationIterator:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration  # End of pages

        start = self.index
        end = min(self.index + self.page_size, len(self.items))
        self.index = end  # Move to next page
        return self.items[start:end]

    def prev(self):
        # Go back exactly one page
        self.index = max(0, self.index - self.page_size * 2)
        return next(self)


# Sample data
products = ["Laptop", "Mouse", "Keyboard",
            "Monitor", "Printer", "Webcam",
            "Headset", "Speaker"]

page_size = 3

# Using the iterator
pager = PaginationIterator(products, page_size)

print(next(pager))   # ['Laptop', 'Mouse', 'Keyboard']
print(next(pager))   # ['Monitor', 'Printer', 'Webcam']
print(pager.prev())  # ['Laptop', 'Mouse', 'Keyboard']
