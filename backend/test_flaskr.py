import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "postgres", "12345", "localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # self.new_question = {
        #     "question": 'New question',
        #     "answer": "new asnwer",
        #     "category": 1,
        #     "difficulty": 1
        # }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # def test_get_paginated_questions(self):
    #     res = self.client().get('/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(len(data['categories']))
    
    # def test_404_sent_requesting_questions_beyond_valid_page(self):
    #     res = self.client().get('/questions/?page=100000', json={"difficulty":1})
    #     data = json.loads(res.data)
        
     
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_get_categories(self):
    #     res= self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['categories'])

    # def test_404_non_existing_category(self):
    #     res = self.client().get('categories/9999')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "resource not found")


    # def test_delete_question(self):
    #     question = Question(question="question new", answer="new answer",
    #     difficulty=1, category=2
    #     )
    #     question.insert()
    #     question_id = question.id
    #     res = self.client().delete(f'/questions/{question_id}')
    #     data = json.loads(res.data)

    #     question = Question.query.filter(
    #         Question.id == question.id).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], question_id)
    #     self.assertEqual(question, None)

    # def test_422_non_existing_questions(self):
    #     res = self.client().delete('/questions/500')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'],"unprocessable")
    # def test_add_question(self):
    #     total_questions_before = len(Question.query.all())
    #     res = self.client().post('/questions', json=self.new_question)
    #     data = json.loads(res.data)

    #     total_questons_after = len(Question.query.all())

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(total_questons_after, total_questions_before +1)

    def test_422_add_question(self):
        new_question = {
            'question': 'new_question',
            'answer': 'new_answer',
            'category': 1
        }


        res = self.client().post('/questions', json=new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

    # def test_search_question(self):
    #     new_search = {'searchTerm': "3"}

    #     res = self.client().post('/questions/search', json=new_search)
    #     data = json.loads(res.data)

        
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['total_questions'])

    # def test_404_search_question(self):
    #     new_search = {'searchTerm': ""}

    #     res = self.client().post('/questions/search', json=new_search)
    #     data = json.loads(res.data)

        
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "resource not found")

    # def test_get_questions_per_category(self):
    #     res = self.client().get('/categories/1/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(data['current_category'])
    
    # def test_404_get_questions_per_category(self):
    #     res = self.client().get('/categories/a/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "resource not found")

   




    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()