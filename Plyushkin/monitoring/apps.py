from django.apps import AppConfig

# import schedule
# import time
# from datetime import datetime
# import bacumon

# def job():
#     print("Start job "+datetime.now().isoformat())
#     bacumon.check_all()

class MonitoringConfig(AppConfig):
    name = 'monitoring'
    verbose_name = "Monitoring"
    # def ready(self):
    # 	print "init jobs"
    # 	schedule.every(1).hours.do(job)
    # 	schedule.run_continuously()