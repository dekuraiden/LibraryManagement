from sql import crud
from sql.models import Book, Anime
from sqlalchemy.orm import Session


def list_book(db: Session):
    return crud.get_all_books(db)



def get_book_by_id(db: Session, book_id: int):
    return crud.get_book_by_id(db, book_id)


def create_book(db: Session, data: dict):
    book = Book(**data)
    book = crud.create_book(db, book)
    return book



def update_book(db: Session, book_id: int, update: dict):
    return crud.update_book_by_id(db, book_id, update)


def delete_book(db: Session, book_id: int):
    book = crud.get_book_by_id(db, book_id)

    if not book:
        return None

    crud.delete_book(db, book)
    return True


