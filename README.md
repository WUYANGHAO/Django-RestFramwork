#### 1.创建并启用虚拟环境
```cmd
py -m venv .venv
.venv\Script\activate
```
#### 2.安装依赖组件
```cmd
pip install django djangorestframework
```
#### 3.创建项目
```cmd
django-admin startproject Scene
```
#### 4.创建应用
```cmd
cd Scene
py manage.py startapp SiteSource
```
#### 5.添加应用到Scene/settings.py
```py
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # 添加rest_framework
    'Sitesource', # 添加应用名称
]
...
LANGUAGE_CODE = 'zh-hans' # 中文
TIME_ZONE = 'Asia/Shanghai' # 中国时间
···
#设置分页
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
···
```
#### 6.创建模型Sitesource/models.py
```py
from django.db import models

# Create your models here.
class Sitesource(models.Model):
    site_name = models.CharField(verbose_name='局点名称', max_length=200)
    site_region = models.CharField(
        verbose_name='国家/地区', max_length=200, default=None)
    site_type = models.CharField(
        verbose_name='所属区域', max_length=200, default=None)
    site_custom_info = models.CharField(
        verbose_name='客户信息', max_length=200, default=None)
    site_deploy_plan = models.CharField(verbose_name='部署方案', max_length=200)
    site_hardware_config = models.CharField(
        verbose_name='硬件配置', max_length=200, default=None)
    site_osdb_version = models.CharField(
        verbose_name='OS/DB版本', max_length=200, default=None)
    site_product_version = models.CharField(
        verbose_name='产品版本', max_length=200)
    site_component_info = models.CharField(verbose_name='组件信息', max_length=200)
    site_peripheral_docking = models.CharField(
        verbose_name='周边对接', max_length=200, default=None)

```
#### 7.模型迁移，同步数据库
```cmd
py manage.py makemigrations Sitesource
py manage.py migrate
```
#### 8.创建序列化器Sitesource/serializers.py
```py
from .models import Sitesource
from rest_framework import serializers

class SitesourceSerializer(serializers.ModelSerialize):
    class Meta:
        model = Sitesource
        fields = '__all__'
```
#### 9.创建视图集Sitesource/views.py
```py 
from .serializers import SitesourceSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Sitesource

class SitesourceViewSet(ModelViewSet):
    queryset = Sitesource.objects.all()
    serializer_class = SitesourceSerializer
```
#### 10.创建路由Sitesource/urls.py
```py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Sitesource import views

router = DefaultRouter()
router.register('sitesources',views.SitesourceViewSet)
urlpatterns = [
    path('',include('router.urls'))
]
```
