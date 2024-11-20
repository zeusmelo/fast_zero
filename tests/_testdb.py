from sqlalchemy import select

from fast_zero.models import User


def test_create_user_db(session):
    user = User(username='zeus', email='zeus@example.com', password='123456')
    session.add(user)
    session.commit()
    session.scalar(select(User).where(User.email == 'zeus@example.com'))

    assert user.username == 'aaa@example.com'
