import unittest

from arango_orm import Collection, Relation
from arango_orm.fields import String, DateTime, Integer, Url, Boolean, List, \
                              Float, Decimal, Float, Date, TimeDelta, Email, Number, UUID

from src import ArangoORMAutoFixture

class TestAutoFixture(unittest.TestCase):
    def test_creates_values_for_required(self):
        class MyModel(Collection):
            __collection__ = "MyCollection"

            _key = String()
            integer = Integer()
            datetime = DateTime()
            url = Url()
            bool_val = Boolean()
            str_list = List(String)
            floater = Float()
            date = Date()
            timedelta = TimeDelta()
            email = Email()
            number = Number()
            uuid = UUID()

        
        models = ArangoORMAutoFixture().generate(MyModel)
        
        for m in models:
            self.assertIsNotNone(m.number)
            self.assertIsNotNone(m.url)
            self.assertIsNotNone(m.bool_val)
            self.assertIsNotNone(m.integer)
            self.assertIsNotNone(m.datetime)
            self.assertIsNotNone(m.str_list)
            self.assertIsNotNone(m.floater)
            self.assertIsNotNone(m.date)
            self.assertIsNotNone(m.timedelta)
            self.assertIsNotNone(m.email)
            self.assertIsNotNone(m.uuid)

    def test_handles_none_gracefully(self):
        class MyModel(Collection):
            __collection__ = "MyCollection"

            _key = String(allow_none=True)
            integer = Integer(allow_none=True)
            datetime = DateTime(allow_none=True)
            url = Url(allow_none=True)
            bool_val = Boolean(allow_none=True)
            str_list = List(String, allow_none=True)
            floater = Float(allow_none=True)
            date = Date(allow_none=True)
            timedelta = TimeDelta(allow_none=True)
            email = Email(allow_none=True)
            number = Number(allow_none=True)
            uuid = UUID(allow_none=True)

        
        models = ArangoORMAutoFixture().generate(MyModel)
        
        for m in models:
            self.assertTrue(hasattr(m, 'number'))
            self.assertTrue(hasattr(m, 'url'))
            self.assertTrue(hasattr(m, 'bool_val'))
            self.assertTrue(hasattr(m, 'integer'))
            self.assertTrue(hasattr(m, 'datetime'))
            self.assertTrue(hasattr(m, 'str_list'))
            self.assertTrue(hasattr(m, 'floater'))
            self.assertTrue(hasattr(m, 'date'))
            self.assertTrue(hasattr(m, 'timedelta'))
            self.assertTrue(hasattr(m, 'email'))
            self.assertTrue(hasattr(m, 'uuid'))