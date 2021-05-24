from django.db import models
#每次修改管理的数据时1.修改models.py 2.对learning_logs 调用  makemigrations  Django迁移项目
# Create your models here.

class Topic(models.Model):
    text=models.CharField(max_length=200)  #存储少量文本  名称标题城市可用CharField  预留空间200个字符
    date_added=models.DateTimeField(auto_now_add=True)  #DateTimeField记录时间和日期的数据  True自动设置时间

    def __str__(self):
        return self.text
#添加新模型后就迁移数据库  python manage.py makemigrations learing_logs
#然后再  python manage.py migrate
class Entry(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)  #topic是ForeignKey 的一个实例 外键引用数据库另一条记录
    text=models.TextField()# text 是TextField的一个实例   不限制长度
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:  #嵌套类
        verbose_name_plural='entries'
    def __str__(self):
        return self.text[:50]+"..."
