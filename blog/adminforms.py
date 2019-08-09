#  @Author : Vector
#  @Email  : vectorztt@163.com
#  @Time   : 2019/8/9 13:53
# -----------------------------------------
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)