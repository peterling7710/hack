import sqlalchemy from create_engine
import sqlalchemy.orm import scoped_session, sessionmaker
import os

def main:
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        main()


db = SQLAlchemy()





    #print(database_exists(engine.url))
    #engine = create_engine(os.getenv("DATABASE_URL"))
    #db = scoped_session(sessionmaker(bind=engine))
