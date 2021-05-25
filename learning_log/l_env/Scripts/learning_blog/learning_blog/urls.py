#告诉Django应创建哪些网页来相应浏览器请求
#url与函数的对应关系  路由系统  根据url不同 返回不同的内容  url与函数的对应关系
"""learning_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect
import pymysql
import  json
import time

import time
class SqlHelper():

    # def __init__(self):
    #     self.connect()
    #也可以把那个链接的内容写成配置文件（活的）
    #只要一建立对象，就直接链接上

    def connect(self):
        self.conn=pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise',charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self,sql,args):
        self.cursor.execute(sql,args)
        result=self.cursor.fetchall()
        return(result)

    def get_one(self,sql,args):
        self.cursor.execute(sql,args)
        result = self.cursor.fetchone()
        return (result)

    def modify(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()

    def multiple_modify(self,sql,args):
        #self.cursor.executemany('insert into ba(id,name)'value(%s,%s),[(1,'abv'),(2,'ffff')])
        self.cursor.executemany(sql,args)
        self.conn.commit()

    def add_create(self,sql,args):
        self.cursor.execute(sql,args)
        self.conn.commit()
        return self.cursor.lastrowid  #获取最后的一个id并且返回

    def close(self):
        self.cursor.close()
        # 关闭连接
        self.conn.close()








def login(request):  #用户提交的数据都在request里面放着   至少一个参数
     #pass
   #  return HttpResponse('hello')  #后面只加字符串
    # return
     if request.method=='GET':  #请求的方法
         return render(request, 'login.html')  #render去找的话根据配置文件去找 DIRS
     else:
         print(request.POST)  #这个post对应html里面的post,request.POST相当于一个字典
         #return HttpResponse('ok')#返回字符串
         # u=request.POST['username']
         # p=request.POST['password']
         u=request.POST.get('username')#通过get从字典里面取值 没有就返回none不会报错
         p=request.POST.get('password')
         if u=='root' and p=='123123':
             #登录成功
             #return redirect('https://www.oldboyedu.com/')#跳转界面
             return redirect('/aaa/')   #跳转到自己的网址
         else:
             return render(request, 'login.html', {'abc':'用户名或者密码错误'}) #替换html里面的字符(模板引擎的渲染)

diccc=[   #可以从数据库取
                        {'id': '1',  'name': 'akagi', 'age': '11'},
                        {'id': '2', 'name': 'bkagi', 'age': '22'},
                        {'id': '3', 'name': 'ckagi', 'age': '33'}
                                                ]

def gab(request):
    return render(request, 'ts/gab.html',
                  {
                      'name':'gab',
                        'oo':['李元芳', '狄仁杰'],          #{{oo.0}}   在 html里面拿某个位置的
                    'zidian':{'a1':'七天','a2':'大圣'},
                    'u_list_dict':diccc
                      # [   #可以从数据库取
                    #     {'id':'1',  'name': 'akagi', 'age': '11'},
                    #     {'id': '2', 'name': 'bkagi', 'age': '22'},
                    #     {'id': '3', 'name': 'ckagi', 'age': '33'}
                    #                             ]
                  }   #{{zidian.a1}}
                  )   #目录下面目录要加路径ts/

    #return HttpResponse('ok')#返回字符串

def delll(request):
    print(request.GET)

    # n=0
    # for a in diccc:
    #     n+=1
    #     if a['id']==request.GET.get('nid'):
    if len(diccc)>1:
        del diccc[int(request.GET.get('nid'))-1]
        return render(request, 'ts/gab.html',
                  {
                      'name': 'gab',
                      'oo': ['李元芳', '狄仁杰'],  # {{oo.0}}   在 html里面拿某个位置的
                      'zidian': {'a1': '七天', 'a2': '大圣'},
                      'u_list_dict': diccc
                      # [   #可以从数据库取
                      #     {'id':'1',  'name': 'akagi', 'age': '11'},
                      #     {'id': '2', 'name': 'bkagi', 'age': '22'},
                      #     {'id': '3', 'name': 'ckagi', 'age': '33'}
                      #                             ]
                  }  # {{zidian.a1}}
                  )  # 目录下面目录要加路径ts/



    else:

            return render(request, 'ts/gab.html',
                                  {
                                      'name': 'gab',
                                      'oo': ['李元芳', '狄仁杰'],  # {{oo.0}}   在 html里面拿某个位置的
                                      'zidian': {'a1': '七天', 'a2': '大圣'},
                                      #'u_list_dict': diccc
                                      # [   #可以从数据库取
                                      #     {'id':'1',  'name': 'akagi', 'age': '11'},
                                      #     {'id': '2', 'name': 'bkagi', 'age': '22'},
                                      #     {'id': '3', 'name': 'ckagi', 'age': '33'}
                                      #                             ]
                                  }  # {{zidian.a1}}
                                  )  # 目录下面目录要加路径ts/



    #return HttpResponse('ok')  # 返回字符串


def classes(request):


    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise',charset='utf8')
    #print("888888888888888",conn)
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #print("******************", cursor)
    # 执行SQL，并返回收影响行数
    cursor.execute("select  id,title  from  class")
    class_list=cursor.fetchall()
    #print("hahhahaha------------")
    #print(class_list)
    # 执行SQL，并返回受影响行数
    # effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

    # 执行SQL，并返回受影响行数
    # effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

    # 提交，不然无法保存新建或者修改的数据
   # conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return render(request, 'ts/link_shujuku.html', {'class_list': class_list})

def add_class(request):
    if request.method=="GET":
        #1.跳转到一个添加界面（新的html），造一个输入框和确定按钮
        #收到get请求（做1）和post请求（拿到数据，存到数据库，更新画面）做不同处理
        return render(request, 'ts/addclass.html')
        #return HttpResponse('你好')\
    else:
         v=request.POST.get('tpdata')
         #print("----------",v)
         if len(v)>0:
             conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
            # print("888888888888888", conn)
             # 创建游标
             cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
             #print("******************", cursor)
             # 执行SQL，并返回收影响行数
             cursor.execute("insert into class(title) values(%s)", [v,] ) #%s是一个占位符（c语言）
             #class_list = cursor.fetchall()
             conn.commit()   # 提交，不然无法保存新建或者修改的数据
             cursor.close()  # 关闭游标
             conn.close()# 关闭连接
             return redirect('/123/')
         else:
            return render(request,'ts/addclass.html',{'错误提示':'班级名称不能为空，请重新输入'})

def del_class(request):
    nid = request.GET.get('nid')
    print("***************",request.GET)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
    # print("888888888888888", conn)
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # print("******************", cursor)
    # 执行SQL，并返回收影响行数
    cursor.execute("delete from class where id=%s", [nid, ])  # %s是一个占位符（c语言）
    # class_list = cursor.fetchall()
    conn.commit()  # 提交，不然无法保存新建或者修改的数据
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return redirect('/123/')  #直接跳转回去就好啦    一次请求一次相应

def change(request):
    if request.method=="GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id=%s", [nid, ])  # 从数据库查数据
        # class_list = cursor.fetchall()
        #conn.commit()  # 这里不用提交了，是要数据
        result=cursor.fetchone()  #是个字典
        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接
        return render(request, 'ts/change_class.html', {'result':result} )
    else:
        print("***************",request.POST)  # 在请求体中
        #即使是post请求，数据也可以放到url里面  使用get来取    nid=request.GET.get('id')
        nid=request.POST.get('id')
        title=request.POST.get('ch_data')

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s  where id=%s", [title, nid])  # 从数据库查数据
        # class_list = cursor.fetchall()
        conn.commit()  #
        result = cursor.fetchone()  # 是个字典
        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接

        return redirect('/123/')

def student(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select student.`name`,student.`id`,student.`class_id`,class.title from student LEFT JOIN class on student.class_id=class.id")  # 从数据库查数据
    # class_list = cursor.fetchall()
    # conn.commit()  # 这里不用提交了，是要数据
    student_list= cursor.fetchall()  # 是个字典  与fetchon什么区别
    #print(student_list)
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接

    return render (request, 'ts/student.html',{'student_list':student_list})

def add_student(request):
    if request.method=="GET":
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(
            "select id,title from class")  # 从数据库查数据
        class_list = cursor.fetchall()
        # conn.commit()  # 这里不用提交了，是要数据
        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接
        return render(request, 'ts/add_student.html', {'class_list':class_list})
    else:
        print(".....................",request.POST)
        name=request.POST.get('xname')
        class_id=request.POST.get('class_id')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(
            "insert into student(name,class_id) values(%s,%s)", [name,class_id,])  # 从数据库查数据
        #class_list = cursor.fetchall()
        conn.commit()  # 这里不用提交了，是要数据
        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接
        return redirect('/student/')


def get_all(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(
        sql, args)  # 从数据库查数据
    class_list = cursor.fetchall()
    # conn.commit()  # 这里不用提交了，是要数据
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return class_list

def modify(sql,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(
        sql,args)  # 从数据库查数据
    #class_list = cursor.fetchall()
    conn.commit()  # 这里不用提交了，是要数据
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接



def edit_student(request):
    if request.method=="GET":
        name=request.GET.get('name')
        cid=int(request.GET.get('nid'))  #为何不能url中获取多个值,起始可以的 刷新一下最先的url就行
        sid=int(request.GET.get('sid'))

        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='94188', db='exercise', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute(
        #     "select id,title from class")  # 从数据库查数据
        # class_list = cursor.fetchall()
        # # conn.commit()  # 这里不用提交了，是要数据
        # cursor.close()  # 关闭游标
        # conn.close()  # 关闭连接
        class_list=get_all("select id,title from class")

        return render(request, 'ts/edit_student.html',{'haha':name,'class_list':class_list,'yes':cid,'sid':sid})
    else:
        name=request.POST.get('xname')
        id= request.GET.get('iid')   #url 里面的要用get
        class_id=request.POST.get('class_id')
        #print("******",id,class_id,name)
        modify("update student set name=%s,class_id=%s where id=%s",[name, class_id, id,])#改一张表  其他的因为主键改变二改变
        return redirect('/student/')
#----------模态对话框------------------
def   modal_add_class(request):
    title=request.POST.get('title')
    if len(title) > 0:
        modify("insert into class(title) values(%s)", [title, ])  # 往数据库增加
        return HttpResponse('ok')  #返回的数据  前端看不到  Ajax偷偷传数据
    else:
        return HttpResponse('班级不能为空')

    #return redirect('/123/')  Ajax这里不能跳转，只能在html中 它里面判断语句（对服务器返回的数据判断）进行是否跳转

    # else:
    #     pass

def  modal_de_class(request):
    title = request.POST.get('title')

    modify("delete from class where id= % s", [title, ])  # 删除

    print(title)
    return HttpResponse('ok')

def modal_edit_class(request):
    ret={'status':True,'message':None}
    try:
        nid = request.POST.get('nid')
        content = request.POST.get('content')
        modify("update class set title=%s where id=%s", [content, nid])
        #print(nid, content)
    except Exception as e:
        ret['status']=False
        ret['message']="处理异常"  #异常对象的内容以字符串格式拿到

    return HttpResponse(json.dumps(ret))


def modal_add_stu_cla(request):
    ret = {'status': True, 'message': None}
    try:
        name=request.POST.get('name')
        classId=request.POST.get('classId')
        print(name, classId)
        modify("insert into student(name,class_id)  values(%s,%s)", [name, classId])

    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)  # 异常对象的内容以字符串格式拿到


    return HttpResponse(json.dumps(ret))


def modal_edit_stu_cla(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        classId  = request.POST.get('classId')
        id = request.POST.get('id')
        print(name, classId, id)
        modify("update student set name=%s,class_id=%s where id=%s", [name, classId, id])

    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)  # 异常对象的内容以字符串格式拿到
   # json.dumps(ret)  python对象转成json对象，为字符串
    # JSON.parse() 方法将数据转换为 JavaScript 对象。
    return HttpResponse(json.dumps(ret))

def teacher_and_class(request):


    class_list=get_all('''SELECT teacher.id AS tid,teacher.`name`,class.title ,GROUP_CONCAT(title) AS titles FROM teacher
                          LEFT JOIN   teacher2class ON teacher.id=teacher2class.teacher_id
                          LEFT JOIN class ON  teacher2class.class_id=class.id
                          GROUP BY teacher.id;''',[])

    class_list1=get_all('''SELECT teacher.id AS tid,teacher.`name`,class.title  FROM teacher
                LEFT JOIN   teacher2class ON teacher.id=teacher2class.teacher_id
                LEFT JOIN class ON  teacher2class.class_id=class.id;''',[])
    class_list2= get_all('select * from class', [])
    result={}
    for row in class_list1:
        tid=row['tid']
        if tid in result:
            result[tid]['titles'].append(row['title'])
        else:
            result[tid]={'tid':row['tid'],'name':row['name'],'titles':[row['title']]}

    #result.values()   #用字典列表方式取出来他的values[作为一个列表]
    #class_list    #mysql group by  直接分组
    return render(request, 'ts/teacher_and_class.html',{'class_list':result.values(),'class_list2':class_list2})
    # return HttpResponse(json.dumps(ret))
    # return redirect('/student/')

def add_teacher_class(request):
    if request.method == "GET":
          class_list = get_all('select * from class', [])
          return render(request, 'ts/add_teacher_class.html',{'class_list':class_list})
    else:
        print(request.POST)
        name=request.POST.get('xname')
        class_ids = request.POST.getlist('class_id')
        obj = SqlHelper()
        obj.connect()
        if   obj.get_one("select id from teacher  where `name`=%s",[name,]):
            #return render(request, 'ts/add_teacher_class.html',{'qqqq':"555"}) #select里面会没有值
            # time.sleep(1)
            obj.close()
            return HttpResponse('名重复，请核实')
        else:

            # list(request.POST.get('class_id'))
            print(name, class_ids)
            teacher_id=obj.add_create("insert into teacher(`name`) values(%s)", [name,])
            #add_create 返回最后一个id的值int
            #obj.modify("insert into teacher(`name`) values(%s)", [name,])
            #teacher_id=obj.get_one("select id from teacher  where `name`=%s",[name,])
            #cursor.lastrowid
            #print(teacher_id[0]['id'])
            print(teacher_id)
            for i in class_ids:
                #data_list=[(),(),()]
                # for i in class_ids:
                #     temp=(teacher_id,i)
                #     data_list.append(temp)
                #obj.multiple_modify('',[(),(),()])  来添加多次，一次提交
                obj.modify("insert into teacher2class(teacher_id,class_id) value(%s,%s)", [teacher_id,i])
            obj.close()
            return redirect('/teacher_and_class/')

def edit_teacher_class(request):
    obj = SqlHelper()
    obj.connect()
    #nid = request.GET.get('nid')
    if request.method == "GET":
        nid = request.GET.get('nid')
        #nid=request.GET.get('nid')
        #print('it is:',request.GET.get('nid'))
        name=obj.get_one("select name from teacher  where `id`=%s", [nid,])['name']
        class_list=obj.get_list('select * from class',[])
        teacher_list = obj.get_list('select class_id from  teacher2class where teacher_id=%s', [nid,])

        #print(teacher_list)
        t_list=[]
        for i in teacher_list:
            t_list.append(i['class_id'])
        # if 2 in t_list:
        #      print('2 在里面',t_list)
        obj.close()
        return render(request, 'ts/edit_teacher_class.html',{'name':name,'class_list':class_list,'t_list':t_list,'nid':nid})
    else:
        #先删除再增加
        t_name=request.POST.get('xname')
        class_ids = request.POST.getlist('class_id')
        nid=request.GET.get('nid')
        obj.modify('update teacher set name=%s WHERE id=%s', [t_name,nid, ])
        obj.modify('DELETE FROM teacher2class WHERE teacher_id=%s',[nid,])
        print(nid)
        # for i in class_ids:
        #     obj.add_create('insert into teacher2class(teacher_id,class_id) values(%s,%s)',[nid,i])
        #data1=[(nid,i) for i in class_ids]  这个也可以替代 data_list
        data_list=[]
        for i in class_ids:
            temp=(nid,i)
            data_list.append(temp)
        print(data_list)
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) values(%s,%s)',data_list)

        obj.close()
        return redirect('/teacher_and_class/')

def modal_add_tea_cla(request):
    name=request.POST.get('name')
    class_id=request.POST.getlist('classId')
    print(name,json.loads(class_id))
   # print(name,class_id)
    return  HttpResponse(1)

def A_get_sql_data(request):
    time.sleep(5)
    obj = SqlHelper()
    obj.connect()
    class_list2=obj.get_list('select id,title from class',[])
    obj.close()
    return HttpResponse(json.dumps(class_list2))  #dunmps python对象转json字符串  序列化一下

urlpatterns = [
     path('admin/', admin.site.urls),
     path('qqq/', login), #不同url调用不同的函数  get请求
     path('aaa/', gab),
     path('del/', delll),
     path('123/', classes),
     path('addclass/', add_class),
     path('del_class/', del_class ),
     path('change/', change) ,   #change后面加/  所有用的后面都要加/
     path('student/', student),
     path('add_student/',add_student),
     path('edit_student/',edit_student),
    #----------模态对话框------------------
     path('modal_add_class/',modal_add_class),
     path('modal_de_class/',modal_de_class),
     path('modal_edit_class/',modal_edit_class),
     path('modal_add_stu_cla/',modal_add_stu_cla),
     path('modal_edit_stu_cla/',modal_edit_stu_cla),
     path('teacher_and_class/' ,teacher_and_class),
     path('add_teacher_class/',add_teacher_class),
     path('edit_teacher_class/',edit_teacher_class),
     path('modal_add_tea_cla/',modal_add_tea_cla),
     path('A_get_sql_data/',A_get_sql_data)
]

