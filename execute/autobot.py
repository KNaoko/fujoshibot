import schedule
import time
import subprocess

path = "./fujoshibot.py"

def job():
	subprocess.call("python %s" % path)

schedule.every(5).to(10).hours.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
