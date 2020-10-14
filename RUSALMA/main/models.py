from django.db import models

from smart_selects.db_fields import ChainedForeignKey
from ckeditor.fields import RichTextField


class Author(models.Model):
    photo = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, verbose_name='Имя')
    position = models.CharField(max_length=255, null=True, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=255, null=True, verbose_name='Подзаголовок')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    content = RichTextField(null=True, blank=True, verbose_name='Текст публикации')
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL,)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_time_to_read(self):
        time_to_read = len(self.content) / 1500

        if time_to_read < 1:
            return '1 минута на прочтение'
        else:
            time_to_read = round(time_to_read)

            if 1 < time_to_read < 5:
                return '{} минуты на прочтение'.format(time_to_read)
            elif 5 <= time_to_read < 20:
                return '{} минут на прочтение'.format(time_to_read)
            else:
                return 'больше 20 минут на прочтение'


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Portfolio(models.Model):
    DIRECTION = (
        ('веб-разработка', 'веб-разработка'),
        ('интернет-маркетинг', 'интернет-маркетинг'),
    )
    direction = models.CharField(max_length=255, null=True, choices=DIRECTION)
    title = models.CharField(max_length=255, null=True, verbose_name='Название')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    link = models.CharField(max_length=255, null=True, verbose_name='Ссылка')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тег')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class Category(models.Model):
    category_name = models.CharField(max_length=255, null=True, verbose_name='Название категории')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=255, null=True, verbose_name='Название подкатегории')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Order(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(Subcategory, null=True, on_delete=models.CASCADE, verbose_name='Подкатегория')

    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True)

    def __str__(self):
        return 'Заказ № ' + str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'