from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

# idm title, slug, description, content, create_dt, modify_dt

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField(verbose_name='SLUG', unique=True, allow_unicode=True, help_text="one word for title alias.")
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text="simple description text.")
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
    
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()

"""    
# Quesiton과 Choice 구조와 같습니다.
class Comment(models.Model):
    # user
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    # date ...
"""