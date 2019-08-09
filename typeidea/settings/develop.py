#  @Author : Vector
#  @Email  : vectorztt@163.com
#  @Time   : 2019/8/9 9:19
# -----------------------------------------
from .base import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
