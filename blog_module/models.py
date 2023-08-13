from django.db import models
from account_module.models import User
from django.utils.text import slugify

# Create your models here.
class BlogCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name="نام دسته بندی")
    url_title = models.CharField(max_length=250, verbose_name="عنوان در url", unique=True)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی مقالات"


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان مقاله")
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name="دسته بندی")
    image = models.ImageField(upload_to="blog", verbose_name="عکس", null=True)
    short_description = models.CharField(max_length=250 ,verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name='متن')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    view = models.IntegerField(verbose_name="تعداد بازدید", blank=True, default=0)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='نویسنده', related_name='uesrs', editable=False)
    slug = models.SlugField(max_length=250, allow_unicode=True,  verbose_name="اسلاگ", db_index=True, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.id)
        super().save(*kwargs)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
