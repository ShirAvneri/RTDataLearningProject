import time
from time import sleep
from winsound import Beep


class Metronome:
    def __init__(self, bpm, bpb=(4, 4)):
        self.supported_bpb = [(2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)]
        self.bpm = bpm  # beats per minute
        self.bpb = bpb  # beats per bar
        self.is_running = False

    def start(self):
        self.is_running = True
        self.run()

    def stop(self):
        self.is_running = False

    def run(self):
        delay = 60.0 / self.bpm  # Will provide the delay, since bpm is beats per minute
        counter = 0
        while self.is_running:
            delta_time = time.time()  # Need to reduce the process time from the delay
            counter += 1
            if counter == self.bpb[0]:  # End of bar
                Beep(800, 100)
                counter = 0
            else:
                Beep(400, 100)
            sleep(delay - (time.time() - delta_time))
