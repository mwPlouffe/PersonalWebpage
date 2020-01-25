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

    def __str__(self):
        return f"Name: {self.name}\n"


class Skill(LineItem):
    type = CharField(max_length=100, choices=SKILLS_QUALIFICATIONS, blank=False, null=False)

    def __str__(self):
        return f"{super(LineItem, self).__str__()} type: {self.type}\n"


class Interest(LineItem):
    type = CharField(max_length=100, choices=INTERESTS, blank=False, null=False)

    def __str__(self):
        return f"{super(Interest, self).__str__()} type: {self.type}\n"


class Information(LineItem):
    city = CharField(max_length=100, blank=False, null=False, default="")
    start = DateField(blank=False, null=False, default=timezone.now)
    end = DateField(blank=False, null=False, default=timezone.now)
    current = BooleanField(blank=False, null=False, default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{super(Information, self).__str__()} city: {self.city}\nstart: {self.start}\nend: {self.end}\n"


class Education(Information):
    university = CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{super(Education, self).__str__()} university: {self.university}\n"


class Note(models.Model):
    item = CharField(max_length=150, blank=False, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"note: {self.item}\n"


class EducationNote(Note):
    education = models.ForeignKey(
        Education,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    def __str__(self):
        return f"{super(EducationNote, self).__str__()} education: {self.education}\n"


class Association(Information):
    university = CharField(max_length=100, blank=False, null=False, default="")
    acronym = CharField(blank=False, null=False, max_length=10, default="")
    type = CharField(blank=False, null=False, choices=TYPES, max_length=11, default=TYPES[0][1])

    def __str__(self):
        return f"{super(Association, self).__str__()} acronym: {self.acronym}\ntype: {self.type}\n " + \
            f"university: {self.university}\n"


class Project(Information):
    place = CharField(max_length=100, blank=True, null=False)
    personal = BooleanField(blank=False, null=False)

    def __str__(self):
        return f"{super(Project, self).__str__()} place: {self.place}\npersonal: {self.personal}\n"


class ProjectNote(Note):
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    def __str__(self):
        return f"{super(ProjectNote, self).__str__()} project: {self.project}\n"


class Work(Information):
    company = CharField(max_length=100, blank=True, null=False)
    volunteer = BooleanField(blank=False, null=False)

    def __str__(self):
        return f"{super(Work, self).__str__()} company: {self.company}\nvolunteer: {self.volunteer}\n"


class WorkNote(Note):
    work = models.ForeignKey(
        Work,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    def __str__(self):
        return f"{super(WorkNote, self).__str__()} work: {self.work}\n"
