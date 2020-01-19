from django.db import models
from django.db.models.fields import CharField, DurationField, BooleanField

SKILLS_QUALIFICATIONS = [
    (1, 'Operating Systems'),
    (2, 'Applications'),
    (3, 'Programming Languages'),
    (4, 'Platforms'),
    (5, 'Methodologies'),
    (6, 'Languages'),
    (7, 'Licenses and Certifications')
]

INTERESTS = [
    (1, 'Experience Abroad'),
    (2, 'Literature'),
    (3, 'Sports'),
    (4, 'Passions')
]


class LineItem(models.Model):
    name = CharField(max_length=100, blank=False, null=False)

    class Meta:
        abstract = True


class Skill(LineItem):
    type = CharField(max_length=100, choices=SKILLS_QUALIFICATIONS, blank=False, null=False)


class Interest(LineItem):
    type = CharField(max_length=100, choices=INTERESTS, blank=False, null=False)


class Information(models.Model):
    name = CharField(max_length=100, blank=False, null=False)
    city = CharField(max_length=100, blank=False, null=False)
    time = DurationField(blank=False, null=False)

    class Meta:
        abstract = True


class Association(Information):
    acronym = CharField(blank=False, null=False, max_length=10)


class Education(Information):
    university = CharField(max_length=100, blank=False, null=False)


class EducationNote(models.Model):
    education = models.ForeignKey(
        Education,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    item = CharField(max_length=100, blank=False, null=False)


class Project(Information):
    place = CharField(max_length=100, blank=True, null=False)
    personal = BooleanField(blank=False, null=False)


class ProjectNote(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    item = CharField(max_length=100, blank=False, null=False)


class Work(Information):
    company = CharField(max_length=100, blank=True, null=False)
    volunteer = BooleanField(blank=False, null=False)


class WorkNote(models.Model):
    work = models.ForeignKey(
        Work,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    item = CharField(max_length=100, blank=False, null=False)
