# celery
# pip install celery
# 在windows操作系统上，还要安装另外一个东西：eventlet
# pip install eventlet


# task：任务
# broker：中间人， 存储任务队列
# worker： 真正执行任务的工作者
# backend： 用来存储任务执行后的结果

#步骤：
#1.在终端  redis-server
#2.另一个终端中输入命令 celery -A tasks.celery worker --loglevel=info     进入监听模式
#       如果是windows celery -A  --pool=eventlet  tasks.celery worker --loglevel=info
#3.执行main.py



from celery import Celery
import time


celery = Celery("tasks", broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0")

@celery.task
def send_mail():
    print("邮件开始发送")
    time.sleep(2)
    print("邮件发送结束")


