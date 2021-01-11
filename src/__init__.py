import math
import random
import faker

from marshmallow.fields import *
from marshmallow import missing

# TODO: Nested
# TODO: Validators

fake = faker.Faker()
random.seed()
class ArangoORMAutoFixture():
    def __init__(self):
        self.field_to_faker = {
            String: self.fake_string,
            UUID: self.fake_uuid,
            Number: self.fake_number,
            Integer: self.fake_integer,
            Decimal: self.fake_decimal,
            Boolean: self.fake_boolean,
            Float: self.fake_float,
            DateTime: self.fake_datetime,
            NaiveDateTime: self.fake_naivedatetime,
            AwareDateTime: self.fake_awaredatetime,
            Time: self.fake_time,
            Date: self.fake_date,
            TimeDelta: self.fake_timedelta,
            Url: self.fake_url,
            Email: self.fake_email,
            List: self.fake_list,
            Dict: self.fake_dict,
        }

        validators = {
            'ContainsNoneOf': '',
            'ContainsOnly': '',
            'Email': '',
            'Equal': '',
            'Length': '',
            'NoneOf': '',
            'OneOf': '',
            'Predicate': '',
            'Range': '',
            'Regexp': '',
            'URL': ''
        }

    def fake_string(self, *args, **kwargs):
        return fake.paragraph()

    def fake_uuid(self, *args, **kwargs):
        return fake.uuid4()

    def fake_number(self, *args, **kwargs):
        return fake.random_number()

    def fake_integer(self, *args, **kwargs):
        return fake.pyint()

    def fake_decimal(self, *args, **kwargs):
        return fake.pydecimal()

    def fake_boolean(self, *args, **kwargs):
        return fake.pybool()

    def fake_float(self, *args, **kwargs):
        return fake.pyfloat()

    def fake_datetime(self, *args, **kwargs):
        return fake.date_time()

    def fake_naivedatetime(self, *args, **kwargs):
        return fake.date_time()

    def fake_awaredatetime(self, *args, **kwargs):
        return fake.date_time(tzinfo=fake.pytimezone())

    def fake_time(self, *args, **kwargs):
        return fake.time_object()

    def fake_date(self, *args, **kwargs):
        return fake.date_object()

    def fake_timedelta(self, *args, **kwargs):
        return fake.time_delta()

    def fake_url(self, *args, **kwargs):
        return fake.url()

    def fake_email(self, *args, **kwargs):
        return fake.email()

    def fake_list(self, *args, **kwargs):
        field = kwargs['field']
        inner = field.inner
        fake_func = self.field_to_faker[type(inner)]
        MAX_LIST_SIZE = 50
        list_size = random.randint(1, MAX_LIST_SIZE)
        l = [fake_func()]
        return l

    def fake_dict(self, *args, **kwargs):
        MAX_KEYS = 10
        num_keys = random.randint(1, MAX_KEYS)
        mapping_items = self.field_to_faker.items()
        d = {}
        for _ in range(num_keys):
            key = fake.pystr()
            value = fake.pystr()
            d[key] = value

        return d

    def generate_fake_object(self, object, key=1):
        fields = object.schema().fields
        data = {}
        for field_key in fields.keys():
            if field_key == '_key':
                data['_key'] = str(key)
                continue
            field = fields[field_key]
            if (not field.required and field.allow_none) and fake.boolean(fake.random_int(0, 100)):
                continue
            if not type(field.default) == type(missing) and fake.boolean(fake.random_int(0, 100)):
                data[field_key] = field.default
                continue
            field_type = str()
            data[field_key] = self.field_to_faker[type(field)](field=field)
        return object(**data)

    def generate(self, object, n=1):
        return [self.generate_fake_object(object, x) for x in range(n)]
