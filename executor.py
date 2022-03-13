import time

from cronGirlfriend import Girlfriend


class Executor:
    def __init__(self,cron_list):
        self.cron_list = cron_list

    def run(self):
        for cron in self.cron_list:
            if cron.can_run():
                now = time.strftime('%H', time.localtime())
                if cron.time() == int(now):
                    cron.run()

Executor(cron_list=[Girlfriend()]).run()