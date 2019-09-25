from celery import Celery

app = Celery('emailTasker', broker= 'redis://Devavijju@Deva:6379/' )
# app.conf.broker_url = 'redis://localhost:6379/0'

@app.task
def add(x,y):
    return x*y;