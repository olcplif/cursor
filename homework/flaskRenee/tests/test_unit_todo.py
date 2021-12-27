import unittest
from .conftest import client
from app import app


class TestTodo(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config["Unit_test_todo"] = True

    def test_get_todos(self):
        response = self.client.get('/api/v1/todos')
        self.assertEqual(response.status_code, 200)

    def test_show_todo_editor(self):
        response = self.client.get('/todo-editor')
        self.assertEqual(response.status_code, 200)

    def test_add_new_todo(self):
        todo_1 = {"title": "Task_1", "text": "Text for Task_1"}
        response = self.client.post('/api/v1/todos', json=todo_1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]["title"], "Task_1")
        self.assertEqual(response.json[0], todo_1)

    def test_update_todo(self):
        response_len_start = len(self.client.get('/api/v1/todos').json)
        todo_1_upd = {"title": "Task_1_upd", "text": "Text for Task_1_upd"}
        response = self.client.patch('/api/v1/todos/0', json=todo_1_upd)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]["title"], todo_1_upd["title"])
        self.assertEqual(len(response.json), response_len_start)

    def test_delete_todo(self):
        response_len_start = len(self.client.get('/api/v1/todos').json)
        todo_2 = {"title": "Task_2", "text": "Text for Task_2"}
        self.client.post('/api/v1/todos', json=todo_2)
        response = self.client.delete('/api/v1/todos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), response_len_start)
