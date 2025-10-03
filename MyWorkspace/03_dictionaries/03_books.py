book_authors = {"1984": "George Orwell",
                "Pride and Prejudice": "Jane Austen",
                "Moby Dick": "Herman Melville"}

print(book_authors.keys())
print(book_authors. values())

for book, author in book_authors.items():
    print(f"{book} by {author}")
