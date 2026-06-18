from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
app = FastAPI()
books=[]
class Book(BaseModel):
    id: int
    title: str = Field(..., min_length=1, description="Book title must be at least 1 character long")
    author: str = Field(..., min_length=1, description="Author name must be at least 1 character long")
    is_issued: bool = Field(default=False, description="Indicates if the book is issued or not")
@app.post("/books")
def add_book(book: Book):
    if not book.title.strip():
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book title cannot be empty")
    if not book.author.strip():
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Author name cannot be empty")
    books.append(book)
    return {
        "message": "Book added successfully",
        "book": book
    }
@app.get("/books")
def get_all_books():
    return {
        "message": "List of all books",
        "total_books": len(books),
        "all_books": books
    }
@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    for book in books:
        if book.id == book_id:
            return {
                "message": "Book found",
                "book": book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            if not updated_book.title.strip():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book title cannot be empty")
            if not updated_book.author.strip():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Author name cannot be empty")
            books[index] = updated_book
            return {
                "message": "Book updated successfully",
                "book": updated_book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(index)
            return {
                "message": "Book deleted successfully",
                "book": deleted_book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")