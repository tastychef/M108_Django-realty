from django.db import models


class Zhk(models.Model):
    '''Данные о проекте'''
    name_project = models.CharField('Название проекта', blank=False, null=False, max_length=100)
    name_developer = models.CharField('Название застройщика', blank=False, null=False, max_length=100)
    get_id = models.CharField('ID проекта', blank=False, null=False, max_length=3)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.name_project}, {self.name_developer}, {self.get_id}'


# class Connect(models.Model):
#     '''Подключение'''
#     token = models.TextField(blank=False, null=False, max_length=100)
#     name = models.CharField(blank=False, null=False, max_length=100)
#     login = models.CharField(blank=False, null=False, max_length=100)
#     zhk = models.ForeignKey(Zhk, verbose_name='Подключение', on_delete=models.CASCADE)
