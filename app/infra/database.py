import os
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


def get_db_url() -> str:
    return 'mysql+pymysql://%s:%s@%s:%s/%s' % (
        os.getenv('DB_USER', 'root'),
        os.getenv('DB_PASSWORD', 'password'),
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_PORT', '3306'),
        os.getenv('DB_NAME', 'post_app'),
    )


engine = create_engine(get_db_url(), pool_size=500, max_overflow=0, pool_pre_ping=True)


metadata = MetaData()


SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def session_manager() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    yield from session_manager()


def get_db() -> Generator[Session, None, None]:
    yield from session_manager()
