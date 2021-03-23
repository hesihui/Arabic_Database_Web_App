from django.db import models

FORMS = [
    ('F1', 'Form 1'),
    ('F2', 'Form 2')
]  # 体裁
LANGUAGES = [
    ('EN', 'English'),
    ('DE', 'German')
]
REGIONS = [
    ('R1', 'Region 1'),
    ('R2', 'Region 2')
]


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    authors = models.CharField(max_length=200)  # TODO: see if there's a better way for list
    year = models.IntegerField()
    form = models.TextField(choices=FORMS)
    language = models.TextField(choices=LANGUAGES)
    region = models.TextField(choices=REGIONS)
    tags = models.TextField()

    def __str__(self):
        return self.title
