import faker

from marshmallow.fields import *
from marshmallow import missing

# TODO: Nested
# TODO: Validators

fake = faker.Faker()

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
            Email: self.fake_email
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

    def fake_string(self):
        return fake.paragraph()

    def fake_uuid(self):
        return fake.uuid4()

    def fake_number(self):
        return fake.random_number()

    def fake_integer(self):
        return fake.pyint()

    def fake_decimal(self):
        return fake.pydecimal()

    def fake_boolean(self):
        return fake.pybool()

    def fake_float(self):
        return fake.pyfloat()

    def fake_datetime(self):
        return fake.date_time()

    def fake_naivedatetime(self):
        return fake.date_time()

    def fake_awaredatetime(self):
        return fake.date_time(tzinfo=fake.pytimezone())

    def fake_time(self):
        return fake.time_object()

    def fake_date(self):
        return fake.date_object()

    def fake_timedelta(self):
        return fake.time_delta()

    def fake_url(self):
        return fake.url()

    def fake_email(self):
        return fake.email()

    def generate_fake_object(self, object):
        fields = object.schema().fields
        data = {}
        for field_key in fields.keys():
            if field_key == '_key':
                data['_key'] = f'{self.fake_integer()}'
                continue
            field = fields[field_key]
            if (not field.required and field.allow_none) and fake.boolean(fake.random_int(0, 100)):
                continue
            if not type(field.default) == type(missing) and fake.boolean(fake.random_int(0, 100)):
                return field.default
            field_type = str()
            data[field_key] = self.field_to_faker[type(field)]()
        return object(**data)

    def generate(self, object, n=1):
        return [self.generate_fake_object(object) for x in range(n)]
