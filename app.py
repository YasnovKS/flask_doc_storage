from doc_storage import app, db, views  # noqa
from doc_storage.models import Document, Version

if __name__ == '__main__':
    with db:
        db.create_tables([Document, Version])
    app.run()
