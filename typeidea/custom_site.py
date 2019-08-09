#  @Author : Vector
#  @Email  : vectorztt@163.com
#  @Time   : 2019/8/9 14:09
# -----------------------------------------
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea 管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')