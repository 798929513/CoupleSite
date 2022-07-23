from django.db import models
from login.models import User


class LikeAndComplain(models.Model):
    # 选择框的标签，二元元组，第一个元素是存在数据库中真实的值，第二个标识在页面上显示的具体内容
    SCORE = (
        (-5, "-5"),
        (-4, "-4"),
        (-3, "-3"),
        (-2, "-2"),
        (-1, "-1"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    author = models.ForeignKey(User, to_field="name", on_delete=models.CASCADE
                               , related_name="like_and_complains", verbose_name="作者")
    title = models.CharField(max_length=32, verbose_name="标题")
    content = models.CharField(max_length=128, verbose_name="内容")
    data_time = models.DateField(verbose_name="日期")
    score = models.IntegerField(choices=SCORE, verbose_name="分数")

    def __str__(self):
        return "{0}: {1}, {2}分".format(self.data_time, self.content, self.score)

    class Meta:
        verbose_name = "吐槽牢骚"
        verbose_name_plural = "吐槽牢骚"
        ordering = ['-data_time']

