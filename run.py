from app import app, logger
from app.models import db
from waitress import serve

from settings import DEV, PORT

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    if DEV:
        app.run(port=PORT, debug=True)
    else:
        logger.info("App starting...")
        serve(app, host="0.0.0.0", port=PORT)
