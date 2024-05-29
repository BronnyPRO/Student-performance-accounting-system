from django.db import models


class Students(models.Model):
    """
    A model of a students.

    id - primary key.
    """

    surname = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    patronymic = models.CharField(max_length=100, null=False)
    group = models.CharField(max_length=10, null=False)

    @property
    def fio(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def __str__(self):
        return f'{self.fio} ({self.group})'

    def __repr__(self):
        return f'Student(surname="{self.surname}", name="{self.name}", patronymic="{self.patronymic}")'


class Scores(models.Model):
    """
    A model of a scores by students.

    id - primary key.
    student - foreign key.
    """
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.CharField(
        max_length=50,
        choices=(
            ("math", "Math"),
            ("physics", "Physics"),
            ("music", "Music")
        ),
        null=False
    )
    value = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{self.student.__str__()}: {self.subject} -> {self.value:.2f}'

    def __repr__(self):
        return f'Student(student="{self.student}", subject="{self.subject}", value="{self.value}")'