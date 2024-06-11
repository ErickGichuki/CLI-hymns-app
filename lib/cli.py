import os
import sys
import click

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.database import SessionLocal
from lib.models.hymns import Hymn, Key, Author

@click.group()
def cli():
    """Welcome to Eric's CLI hymns management"""

@cli.command()
@click.argument('number', type=int)
@click.argument('title', type=str)
@click.argument('lyrics', type=str)
@click.argument('author_name', type=str)
@click.argument('key_name', type=str)
def create_hymn(number, title, lyrics, author_name, key_name):
    """Create a new hymn"""
    session = SessionLocal()
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    key = session.query(Key).filter_by(name=key_name).first()
    if not key:
        key = Key(name=key_name)
        session.add(key)
        session.commit()

    hymn = Hymn(number=number, title=title, lyrics=lyrics, author_id=author.id, key_id = key.id)
    session.add(hymn)
    session.commit()
    session.close()
    click.echo(f"Hymn '{title} has been added successfully.'")
    