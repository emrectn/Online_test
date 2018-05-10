from config import DB_URI
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    point = Column(Integer, default=0)
    best_point = Column(Integer, default=0)

    def __repr__(self):
        return '<User(id: {}, email: \'{}\'>'.format(self.id, self.email)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'point': self.point,
            'best_point': self.best_point,
        }

    def update_best_point(self):
        if self.point > self.best_point:
            self.best_point = self.point
        self.point = 0
        return self.best_point

    def increment_point(self):
        point = self.point + 1
        self.point = point
        return self.point


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String(300), nullable=False)
    answer1 = Column(String(100), nullable=False)
    answer2 = Column(String(100), nullable=False)
    answer3 = Column(String(100), nullable=False)
    answer4 = Column(String(100), nullable=False)
    answer5 = Column(String(100), nullable=False)
    true_answer = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Question(id: {}>'.format(self.question)

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer1': self.answer1,
            'answer2': self.answer2,
            'answer3': self.answer3,
            'answer4': self.answer4,
            'answer5': self.answer5,
            'true_answer': self.true_answer,
        }

    def to_frontend(self):
        return {
            'text': self.question,
            'options': [
                        {'text': self.answer1, 'is_correct': False},
                        {'text': self.answer2, 'is_correct': False},
                        {'text': self.answer3, 'is_correct': False},
                        {'text': self.answer4, 'is_correct': False},
                        {'text': self.answer5, 'is_correct': False},
                        ]
        }


# local veritabanı
engine = create_engine(DB_URI)

# tablolar veritabanına kaydedildi.
Base.metadata.create_all(engine)

# Database session oluşturucu oluşturuldu
DBSession = sessionmaker(engine)
