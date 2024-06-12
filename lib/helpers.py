import click
from models.database import SessionLocal
from models.hymns import Hymn, Author, Key

def exit_program():
    print('Goodbye! see you next time')
    exit()

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
def delete_hymn(hymn_id):
    """Delete a hymn"""
    session = SessionLocal()
    hymn = session.query(Hymn).filter_by(id=hymn_id).first()
    if hymn:
        session.delete(hymn)
        session.commit()
        click.echo(f"We're sorry to see that Hymn '{hymn_id}' has been deleted successfully!")
    else:
        click.echo('The hymn is not found!')
    session.close()

def list_hymns():
    """List all hymns."""
    session = SessionLocal()
    hymns = session.query(Hymn).all()
    if hymns:
        for hymn in hymns:
            click.echo(f"{hymn.id}: {hymn.title} by {hymn.author.name} in {hymn.key.name}")
    else:
        click.echo("We're sorry we don't have hymns yet.")
    session.close()