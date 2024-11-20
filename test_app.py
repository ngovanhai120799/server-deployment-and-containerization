import unittest

from Tools.scripts.gprof2html import header


class TestApp(unittest.TestCase):
    def setUp(self):
        from app import create_app
        self.app = create_app()
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_ctxt.pop()
        self.app = None
        self.app_ctxt = None

    def test_auth(self):
        response = self.client.get('/auth', json={
            "email": "testuser1@gmail.com",
            "password":"Abcd@1234"
        })
        self.assertEqual(response.status_code, 200)
    def test_content(self):
        response = self.client.get('/auth', json={
            "email": "testuser1@gmail.com",
            "password":"Abcd@1234"
        })
        token = response.json
        content = self.client.get('/contents', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(content.status_code, 200)
        user = content.json.get("email")
        self.assertEqual(user, "testuser1@gmail.com")