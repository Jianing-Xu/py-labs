from django.db import models

class Topic(models.Model):
    """用户学习的主题"""
    
    # 存储少量的文本，如名称、城市等，使用 CharField
    text = models.CharField(max_length=200)
    
    # auto_now_add=True 让 Django 自动将这个属性设置为当前日期和时间
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    
    # ForeignKey 是一个外键，用于建立数据库中两项数据之间的联系
    # 这里将一个条目(Entry)与一个特定的主题(Topic)相关联
    # on_delete=models.CASCADE 意味着如果删除了主题，此主题下所有的条目也会被级联删除
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    # TextField 不需要长度限制，适合记录比较长的一大段笔记文本
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """用于管理模型的额外信息"""
        # verbose_name_plural 告诉 Django 在需要显示多个条目时使用什么词（默认它是加一个s变成 entrys，不符合英语语法）
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """返回模型的字符串表示"""
        # 如果条目内容更长，只显示前 50 个字符，并加上省略号
        if len(self.text) > 50:
             return f"{self.text[:50]}..."
        else:
             return self.text
