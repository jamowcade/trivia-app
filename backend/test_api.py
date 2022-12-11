import os
import  json
import unittest

from flaskr import  create_app
from models import setup_db, Question, Category


class BookTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format("postgres", "12345", "localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "question": 'New question',
            "category": 1,
            "difficulty": 1,
            "answer": "answer one"
        }
    def tearDown(self):
        pass

    def test_get_paginated_questions(self):
        res = self.client.get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client.get('/questions/?page=200')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")









    # run the test
if __name__ == '__main__':
    unittest.main()