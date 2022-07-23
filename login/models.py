from django.db import models


# Create your models here.


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女")
    )

    name = models.CharField(max_length=128, unique=True, default='')
    password = models.CharField(max_length=128, default='')
    # 关系字段，与自己关联，lover也是用户，我想要关联名称，而名字正好是唯一的
    lover = models.OneToOneField('self', on_delete=models.SET_NULL,
                                 blank=True, null=True, related_name="lover_is", to_field="name")
    email = models.EmailField(default='')
    sex = models.CharField(max_length=32, choices=gender, default="女")
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create_time"]  # 定义用户按照创建时间的反序排列， 也就是最近的最先显示
        verbose_name = "用户"
        verbose_name_plural = "用户"
