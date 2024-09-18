from celery import shared_task
from datetime import timezone, datetime
from datetime import timedelta

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from NewsPaper import settings
from news.models import Post, Category


@shared_task
def send_email_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscribers_email = []
    for category in categories:
        subscribers_users = category.subscribers.all()
        for sub_users in subscribers_users:
            subscribers_email.append(sub_users.email)
    html_content = render_to_string(
        'post_created_email.html',
        {'text': f'{post.name_post}',
         'link': f'{settings.SITE_URL}/news/{pk}',
         }
    )

    msg = EmailMultiAlternatives(
        subject='Новости за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_email
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekly_send_mail_task():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    news = Post.objects.filter(time_post__gte=last_week)
    categories = set(news.values_list('category__name_category', flat=True))
    subscribers = set(Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'news': news,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Новости за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,

    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
