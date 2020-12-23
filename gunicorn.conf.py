"""
    @File  : gunicorn.conf.py.py
    @Author: GaoZizhong
    @Date  : 2020/4/2 21:13
    @Desc  : 
"""
import multiprocessing

workers = multiprocessing.cpu_count()    # 定义同时开启的处理请求的进程数量，根据网站流量适当调整
# worker_class = "gevent"   # 采用gevent库，支持异步处理请求，提高吞吐量
bind = "0.0.0.0:6106"
timeout = 120
