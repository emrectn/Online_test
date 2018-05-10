import requests
from enum import Enum
from html.parser import HTMLParser
BASE_URL = 'http://localhost:5000/api/question'


CEVAPLAR = [0, 0, 1, 3, 3, 0, 1, 0, 0, 3, 4, 0, 1, 1, 1, 4, 4, 0, 0, 4, 2, 2, 0, 4, 2, 4, 2, 0, 4, 2, 2, 0, 2, 3, 0, 0, 4, 2, 2, 2, 3, 2, 2, 3, 3, 4, 3, 0, 3, 3, 2, 3, 3, 0, 2, 3, 1, 0, 2, 4, 0, 4, 2, 3, 2, 0, 0, 4, 3, 0, 3, 3, 2, 2, 1, 4, 2, 3, 0, 3, 4, 0, 1, 1, 4, 0, 2, 2, 0, 3, 2, 2, 2, 4, 4, 1, 0, 2, 2, 0, 3, 0, 2, 2, 2, 2, 0, 0, 3, 4, 4, 3, 3, 3, 0, 3, 0, 0, 4, 1, 0, 1, 1, 2, 0, 3, 4, 0, 1, 3, 1, 3, 3, 1, 1, 4, 2, 1, 4, 4, 0, 0, 2, 1, 0, 4, 0, 0, 1, 3]


def add_question(data, counter):

    print("Soru ekleme No: ", counter)
    r = requests.post(
        BASE_URL,
        json={'question': data['question'],
              'answer1': data['a'],
              'answer2': data['b'],
              'answer3': data['c'],
              'answer4': data['d'],
              'answer5': data['e'],
              'true_answer': CEVAPLAR[counter],
              'password': '123456'})

    print("{} \n".format(r.json()))
    return


class DataStatus(Enum):
    QUESTION = 1
    ANSWERA = 2
    ANSWERB = 3
    ANSWERC = 4
    ANSWERD = 5
    ANSWERE = 6
    TRUE = 7
    EMPTY = 0


class MyHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super(MyHTMLParser, self).__init__(*args, **kwargs)
        self.data_status = DataStatus.EMPTY
        self.data = []
    # Datanin metin, soru, cevap oldugunu belirlemize yarar.

    def handle_starttag(self, tag, attrs):
        if 'soru-' in tag:
            self.data_status = DataStatus.QUESTION
            # print('Bu bir metin {}'.format(DataStatus.TEXT.name))

        elif 'a-' in tag:
            self.data_status = DataStatus.ANSWERA

        elif 'b-' in tag:
            self.data_status = DataStatus.ANSWERB

        elif 'c-' in tag:
            self.data_status = DataStatus.ANSWERC

        elif 'd-' in tag:
            self.data_status = DataStatus.ANSWERD

        elif 'e-' in tag:
            self.data_status = DataStatus.ANSWERE

        else:
            print('Metin parcalanirken hata oluştu')

        # print("start tag:", tag.strip())

    def handle_data(self, data):
        # metinin basindaki ve sonunda '\n'den kurtuluyoruz.
        # data_content = data.strip()
        # re.sub('\n', '', data_content)
        data_content = data.replace('\n', ' ').strip()

        if self.data_status == DataStatus.QUESTION:
            self.data.append({'question': data_content})

        elif self.data_status == DataStatus.ANSWERA:
            self.data[-1]['a'] = data_content

        elif self.data_status == DataStatus.ANSWERB:
            self.data[-1]['b'] = data_content

        elif self.data_status == DataStatus.ANSWERC:
            self.data[-1]['c'] = data_content

        elif self.data_status == DataStatus.ANSWERD:
            self.data[-1]['d'] = data_content

        elif self.data_status == DataStatus.ANSWERE:
            self.data[-1]['e'] = data_content


if __name__ == '__main__':
    with open('sorular.txt') as f:
        metin = f.read()
    parser = MyHTMLParser()
    parser.feed(metin)
    data = parser.data

    counter = 0
    max_length = 0
    for i in data:
        add_question(i, counter)
        if max_length < len(i['question']):
            max_length = len(i['question'])
        counter += 1

    print('counter : ', counter)
    print(max_length)