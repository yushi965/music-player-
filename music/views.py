# 专门向浏览器返回一个html页面的
import random
from django.shortcuts import render
from django.views import View
from .models import Music

#搜索功能包
from django.db.models import Q
# 可以在此文件中编写网站的逻辑交互
# Create your views here.

'''
在django中 有两种编程模式
    函数式编程
        http get post 请求方法判断的话 比较麻烦
    
    基于类的编程
        自带了http方法 只要重写就可以
'''

# 显示网站首页
class Index(View):
    def get(self, request):
        # 如果你的页面上有动态数据[数据库中的数据] locals方法可以全部返回到页面上
        return render(request, 'music/index.html', locals())

    def post(self, request):
        pass

# 网站搜索功能
class Search(View):
    def get(self, request):
        # 1. 获取用户输入的关键字
        search_text = request.GET['search_text']
        print(search_text)

        if not search_text:
            return render(request, 'music/index.html', locals())

        reponse_list = Music.objects.filter(Q(name__icontains=search_text) | Q(singer__icontains=search_text))

        # 记录搜索数据
        with open('record.txt', 'a', encoding="utf-8") as f:
            if not reponse_list:
                f.write('\n' + search_text + '\t0')
            else:
                f.write('\n' + search_text + '\t1')

        return render(request, 'music/result.html', locals())

    def post(self, request):
        pass


class Good_luck(View):
    def get(self, request):
        with open('poison-soup.txt', 'r+', encoding='utf-8') as f:
            soup = f.readlines()
            poison = random.choice(soup)

            luck = Music.objects.order_by('?')[:6]
            print(luck)
            return render(request, 'music/lucky.html', {'poison': poison, 'reponse_list': luck})