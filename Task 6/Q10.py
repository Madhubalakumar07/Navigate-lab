from datetime import datetime

class Experiment:
    def start(self):
        self.start_time = datetime.now()

    def end(self):
        self.end_time = datetime.now()
