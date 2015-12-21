from celery import Celery
import subprocess


#app = Celery('tasks', broker='redis://redis.trawi.org:6379/0')

app = Celery()

@app.task
def add(x, y):
    return x + y

    
@app.task
def fetch_url(url, oid):
    subprocess.run("curl -L %s  -o /data/tmp/%s"%(url, oid), shell=True, check=True)
    return "Got %s %s"%(url, oid)

@app.task
def process_image(oid):
    cmd = "vips im_vips2tiff --vips-progress --vips-concurrency=4  /data/tmp/%s /data/public/%s.tif:deflate,tile:256x256,pyramid"%(oid,oid)
    print ("Execute",cmd)
    subprocess.run(cmd, shell=True, check=True)
    return "Processed %s"%(cmd)
    
@app.task
def fetch_image(url, oid):
    fetch_url(url, oid)
    process_image(oid)
    return "Processed %s %s"%(url, oid)
    
    
