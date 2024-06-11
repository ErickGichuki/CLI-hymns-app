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

@cli.command()
@click.argument('hymn_id', type=int)
@click.option('__title', type=str, help='New title for the hymn')
@click.option('__lyrics', type=str, help='New lyrics for the hymn')
@click.option('__author_name', type=str, help='New author for the hymn')
@click.option('__key_name', type=str, help='New key for the hymn')
def update_hymn(hymn_id, title, lyrics, author_name, key_name):
    """Update an existing hymn."""
    session =SessionLocal()
    hymn = session.query(Hymn).filter_by(id=hymn_id).first()
    if hymn:
        if title:
            hymn.title = title
        if lyrics:
            hymn.lyrics = lyrics
        if author_name:
            author = session.query(Author).filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                session.add(author)
                session.commit()
            hymn.author_id = author.id
            if key_name:
                key = session.query(Key).filter_by(name=key_name).first()
                if not key:
                    key = Key(name=key_name)
                    session.add(key)
                    session.commit()
                hymn.key_id = key.id
            session.commit()
            click.echo(f"Hymn '{hymn_id}' has been updated successfully!")
        else:
            click.echo("Sorry!The hymn you want to update is not found!")
            session.close()