from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField(max_length=3000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return f'{self.id}) {self.question}'

class Choice(models.Model):
    article = models.ForeignKey(
        'questionnare_app.Poll',
        on_delete=models.CASCADE,
        related_name='choices',
        verbose_name='Опрос',
        null=False,
        blank=False
    )
    choice = models.TextField(max_length=3000, verbose_name='Ответ', null=False, blank=False)

    class Meta:
        db_table = 'choices'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    
    def __str__(self):
        return f'{self.id}) {self.choice}'