import json

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase


class QuestionAnswersAPITest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test',
            'test@test.com',
            'test',
        )
        self.dummy_questions = [
            {
                'posted_user': self.user.pk,
                'questions': 'Test questions1',
                'book_mark': 0
            }, {
                'posted_user': self.user.pk,
                'questions': 'Test questions2',
                'book_mark': 1
            }
        ]
        self.dummy_answers = [
            {
                'answered_user': self.user.pk,
                'question': 1,
                'answers': 'This is answer about question11',
                'book_mark': 0
            }, {
                'answered_user': self.user.pk,
                'question': 1,
                'answers': 'This is answer about question12',
                'book_mark': 0
            }, {
                'answered_user': self.user.pk,
                'question': 2,
                'answers': 'This is answer about question21',
                'book_mark': 1
            }
        ]
        self.questions_url = reverse('questions_list')
        self.answers_url = reverse('answers_list')

    def test_questions_post(self):
        response = self.client.post(self.questions_url, data=json.dumps(
            self.dummy_questions), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.json())

    def test_questions_list(self):
        self.test_questions_post()

        response = self.client.get(self.questions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

        pk = str(response.json()[0]['id'])
        response = self.client.get(self.questions_url + pk + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json())

    def test_answers_post(self):
        self.test_questions_post()

        response = self.client.post(self.answers_url, data=json.dumps(
            self.dummy_answers), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.json())

    def test_answers_list(self):
        self.test_answers_post()

        response = self.client.get(self.answers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)

        response = self.client.get(self.questions_url)
        pk = str(response.json()[0]['id'])
        response = self.client.get(self.questions_url + pk + '/answers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json())
        self.assertEqual(len(response.json()), 2)
