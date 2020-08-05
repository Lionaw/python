from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)                  #需要存储少量的文本，如名称、标题或城市时，可使用CharField
    date_added = models.DateTimeField(auto_now_add=True)     #DateTimeField ——记录日期和时间的数据

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text