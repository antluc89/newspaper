import os

from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from .models import PostCategory, Post
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from .tasks import send_email_task, weekly_send_mail_task
from NewsPaper.NewsPaper import settings


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if not kwargs['action'] == 'post_add':
        return

#    emails = User.objects.filter(
#        subscriptions__category__in=instance.category.all()
#    ).values_list('email', flat=True)
#
#    subject = f'Пост в категории {", ".join([str(cat) for cat in instance.category.all()])}'
#
#    text_content = (
#        f'Название: {instance.name_post}\n'
#        f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
#    )
#    html_content = (
#        f'Название: {instance.name_post}<br>'
#        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#        f'Ссылка на пост</a>'
#    )
#    for email in emails:
#        msg = EmailMultiAlternatives(subject, text_content, None, [email])
#        msg.attach_alternative(html_content, "text/html")
#        msg.send()

    send_email_task.delay(instance.id)

