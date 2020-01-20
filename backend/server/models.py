from django.db import models
from django.db.models.fields import CharField, DateField, BooleanField
from django.utils import timezone

SKILLS_QUALIFICATIONS = [
    ('Operating Systems', 0),
    ('Applications', 1),
    ('Programming Languages', 2),
    ('Platforms', 3),
    ('Methodologies', 4),
    ('Languages', 5),
    ('Licenses and Certifications', 6)
]

INTERESTS = [
    ('Experience Abroad', 0),
    ('Literature', 1),
    ('Sports', 2),
    ('Passions', 3)
]
TYPES = [
    ('Association', 0),
    ('Society', 1)
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
    start = DateField(blank=False, null=False, default=timezone.now)
    end = DateField(blank=False, null=False, default=timezone.now)

    class Meta:
        abstract = True


class Education(Information):
    university = CharField(max_length=100, blank=False, null=False)


class EducationNote(models.Model):
    education = models.ForeignKey(
        Education,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    item = CharField(max_length=150, blank=False, null=False)


class Association(Education):
    acronym = CharField(blank=False, null=False, max_length=10)
    type = CharField(blank=False, null=False, choices=TYPES, max_length=11)


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
    item = CharField(max_length=150, blank=False, null=False)


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
    item = CharField(max_length=150, blank=False, null=False)
