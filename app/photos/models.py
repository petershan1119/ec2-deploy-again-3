from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)


# Photo모델이 삭제되는 시점의 signal을 이용해서
# 인스턴스가 삭제될 때, file필드의 파일도 삭제하도록 구현
@receiver(pre_delete, sender=Photo)
def file_delete(sender, instance, **kwargs):
    instance.file.delete()