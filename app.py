from doc_storage import app, db
from doc_storage.models import Document


if __name__ == '__main__':
    with db:
        db.create_tables([Document])
    app.run()
