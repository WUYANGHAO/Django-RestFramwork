from django.db import models

# Create your models here.
class Sitesource(models.Model):
    site_name = models.CharField(verbose_name='局点名称', max_length=200)
    site_region = models.CharField(
        verbose_name='所属区域', max_length=200, default=None)
    site_type = models.CharField(
        verbose_name='局点类型', max_length=200, default=None)
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