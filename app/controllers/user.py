from app.models import DBSession, User
from sqlalchemy.exc import IntegrityError


def create_user(email):
    data = get_user(email)
    if not data:
        print('Yeni kullanıcı eklendi')
        db = DBSession()
        user = User(email=email)
        db.add(user)

        try:
            db.commit()
        except IntegrityError:
            print('Veritabanı commit esnasında hata oluştu')
            db.rollback()
            user = None
        data = user.to_dict() if user else None
        db.close()
    return data


def get_user(email):
    db = DBSession()
    user = db.query(User).filter(User.email == email).first()

    if user:
        data = user.to_dict()
    else:
        data = None
    db.close()
    return data


def update_best_point(email, point):
    db = DBSession()
    user = db.query(User).filter(User.email == email).first()

    if user:
        user.point = point
        try:
            db.commit()
            user.update_best_point()
            db.commit()
        except IntegrityError:
            print('Veritabanı commit işlemi sırasında hata oluştu')
            db.rollback()

        data = user.to_dict()
        db.close()
        return data



