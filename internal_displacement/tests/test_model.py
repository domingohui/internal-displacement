import os
from datetime import datetime
from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from internal_displacement.model.model import Status, Session, Category, Article, Content, Country, CountryTerm

engine = create_engine(os.environ.get('DB_URL'))
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
        content = Content(article=article,
                          retrieval_date=datetime.now(),
                          content="La la la")
        disaster = Category.lookup(self.session, 'disaster')
        article.categories = [disaster]
        self.session.add(article)

    def test_country_term(self):
        mm = Country(code="mm")
        myanmar = CountryTerm(term="Myanmar", country=mm)
        burma = CountryTerm(term="Burma", country=mm)
        self.session.add(mm)
