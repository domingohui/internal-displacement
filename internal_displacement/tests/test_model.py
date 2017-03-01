from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from internal_displacement.model.model import Status, Session, Category, Article

engine = create_engine(
    'postgresql://aneel:xxx@internal-displacement.cf1y5y4ffeey.us-west-2.rds.amazonaws.com/internal_displacement')
Session.configure(bind=engine)

class TestModel(TestCase):

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.rollback()

    def test_statuses(self):
        statuses = self.session.query(Status)
        descriptions = {s.description for s in statuses}
        self.assertEqual(descriptions, {'new', 'fetching', 'processing', 'processed', 'fetching failed', 'processing failed'})

    def test_categories(self):
        categories = self.session.query(Category)
        descriptions = {c.description for c in categories}
        self.assertEquals(descriptions, {'other', 'disaster', 'conflict'})

    def test_article(self):
        new = Status.lookup(self.session, 'new')
        article = Article(url='http://example.com',
                          domain='example.com',
                          status=new)
        self.session.add(article)
        self.session.commit()
