from faker import Faker
from django.contrib.auth import get_user_model

from .models import Posts
import factory
import datetime

User = get_user_model()
fake = Faker()
eml = "@gmail.com"


class PostFactory:
    class Meta:
        model = Posts

    # title = fake.sentence(ext_word_count=2)
    title = factory.Faker("sentence", nb_words=4)
    slug = fake.slug(title)
    # content = fake.paragraphs(nb=2, ext_sentence=True)
    content = factory.Faker("sentence", nb_words=4)
    author = User.objects.create_user(
        email=fake.user_name() + eml,
        name=fake.user_name(),
        tc=True,
        password=fake.password(),
    )
    # date_created = fake.date_time()
    date_created = factory.LazyFunction(datetime)
    # date_updated = fake.date_time(date_created)


post = PostFactory()
print(post.title)  # Access any generated field
# post.save()  # Save the post to the database
