from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone


class Article(models.Model):
    RATE_CHOICES = (
        ('1.0', _('1 - Very Poor')),
        ('2.0', _('2 - Below Average')),
        ('3.0', _('3 - Average')),
        ('4.0', _('4 - Good')),
        ('5.0', _('5 - Excellent')),
    )

    completed = models.BooleanField(verbose_name=_('Completed'), blank=False, default=False)
    creator = models.ForeignKey(User, verbose_name=_('Creator'), on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(verbose_name=_('Title'), max_length=90, db_index=True)
    body = models.TextField(verbose_name=_('Body'), blank=True)
    authors = models.ManyToManyField(User, verbose_name=_('Authors'), related_name='authors')
    rate = models.CharField(_('Rate'), max_length=3, choices=RATE_CHOICES, default='3.0', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), default=timezone.now)
    update_date = models.DateTimeField(verbose_name=_('Update Date'), auto_now_add=True)
    liked = models.ManyToManyField(User, verbose_name=_('Liked by Users'), related_name='user_liked', default=list, blank=True)
    views = models.PositiveIntegerField(verbose_name=_('Views'), default=0)
    favorited = models.ManyToManyField(User, verbose_name=_('Favorited by Users'), related_name='user_favorited', default=list, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
