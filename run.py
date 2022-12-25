from app import app, logger
from app.models import db
from waitress import serve

from settings import DEV

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    if DEV:
        app.run(port=6571, debug=True)
    else:
        logger.info("")
        serve(app, host="0.0.0.0", port=6571)
