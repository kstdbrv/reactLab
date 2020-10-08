from django.db import models

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


class Order(models.Model):
    CATEGORY = (
        ('интернет-маркетинг', 'интернет-маркетинг'),
        ('веб-разработка', 'веб-разработка'),
    )

    INTERNET_CHOICES = (
        ('реклама готового продукта', 'реклама готового продукта'),
        ('оптимизация сайта и трафика', 'оптимизация сайта и трафика'),
        ('продвижение в социальных медиа', 'продвижение в социальных медиа'),
        ('креатив', 'креатив'),
        ('стратегия и аналитика', 'стратегия и аналитика'),
    )

    WEB_CHOICES = (
        ('брендинг', 'брендинг'),
        ('проектирование', 'проектирование'),
        ('дизайн', 'дизайн'),
        ('веб-разработка', 'веб-разработка'),
        ('адаптация сайта', 'адаптация сайта'),
        ('разработка мобильного приложения', 'разработка мобильного приложения'),
    )

    category = models.CharField(max_length=255, choices=CATEGORY)
