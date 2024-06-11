from lib.models.database import SessionLocal
from lib.models.hymns import Hymn, Author, Key

def get_all_hymns():
    session = SessionLocal
    hymns = session.query(Hymn).all()
    session.close()
    return hymns