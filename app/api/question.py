from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from app.controllers.question import get_question, add_question

bp = Blueprint('question_api', __name__)
api = Api(bp)


class Question(Resource):
    def get(self):
        question_id = request.args.get("id")
        if question_id:
            try:
                data = get_question(int(question_id))
                if data:
                    # Dogru cevap Log
                    for i in data['options']:
                        if i['is_correct']:
                            print('Cevap : ', i['text'])
                    # Dogru cevap Log
                    return data

                print('Bu question_id veritabanında bulunamadi')
                abort(403)
            except ValueError:
                print('question_id int değil')
                print(question_id, ' type: ', type(question_id))
                abort(404)
        abort(400)

    def post(self):
        question = request.json.get("question")
        answer1 = request.json.get("answer1")
        answer2 = request.json.get("answer2")
        answer3 = request.json.get("answer3")
        answer4 = request.json.get("answer4")
        answer5 = request.json.get("answer5")
        true_answer = request.json.get("true_answer")
        password = request.json.get("password")

        if password == '123456':
            data = add_question(question, answer1, answer2, answer3, answer4,
                                answer5, true_answer)

            if data:
                return {'status': 'OK',
                        'data': data}
            abort(400)
        abort(403)

api.add_resource(Question, '/api/question')
