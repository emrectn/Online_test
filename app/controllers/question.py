from app.models import DBSession, Question
from sqlalchemy.exc import IntegrityError


def get_question(question_id):
    db = DBSession()
    question = db.query(Question).get(question_id)

    if question:
        true_id = question.to_dict()['true_answer']
        data = question.to_frontend()
        data['options'][true_id]['is_correct'] = True

    else:
        data = None
    db.close()
    return data


def add_question(question, answer1, answer2, answer3, answer4, answer5,
                 true_answer):

    db = DBSession()
    question = Question(question=question,
                        answer1=answer1,
                        answer2=answer2,
                        answer3=answer3,
                        answer4=answer4,
                        answer5=answer5,
                        true_answer=true_answer)
    db.add(question)
    try:
        db.commit()
    except IntegrityError:
        print('Veritabanı commit esnasında hata oluştu')
        db.rollback()
        question = None
    data = question.to_dict() if question else None
    db.close()
    return data