import unittest
from app import app, db
from models import Plant

class TestPlant(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_can_be_serialized(self):
        '''can create records with a to_dict() method for serialization.'''
        with app.app_context():
            p = Plant(name="Douglas Fir", image=None, price=0.0)
            db.session.add(p)
            db.session.commit()
            serialized = p.to_dict()
            self.assertEqual(serialized['name'], "Douglas Fir")
            self.assertEqual(serialized['image'], None)
            self.assertEqual(serialized['price'], 0.0)

if __name__ == '__main__':
    unittest.main()
