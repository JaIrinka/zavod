import json

#LOCATIONS = {'L0': 0, 'L1': 1} #{ L0: 0, L1: 1, L2: 2, LM1: 3, LM2: 4, LM3: 5}
TRACK1 = (0, 1, 0, 2, 0, 3)
TRACK2 = (0, 1, 2, 0, 2, 3)

class Worker:

    def __init__(self, id, track):
        self.id = id
        self.track = track
        self.track_step = 0
        self.location = self.track[self.track_step]

    def __repr__(self):
        return '{id:'+str(self.id)+', location:'+str(self.location)+ '}'

    def step(self, point):
        self.track_step = self.track_step + 1 if self.track_step < len(self.track) - 1  else 0
        self.location = self.track[self.track_step]

class Simulator:

    def __init__(self, n, period):
        # n - количество рабочих
        # period - время в условных единицах

        self.Workers = []
        for i in range(n):
            track = TRACK1 if i % 2 == 0 else TRACK2
            self.Workers.append(Worker(i, track))
        self.period = period
        self.timer = 0
        self.log = []

    def run(self):
        for point in range(self.period):
            for w in self.Workers:
                self.contacts(point)
                print(repr(w))
                w.step(point)

        with open('logs.json', 'w', encoding='utf-8') as logs:
            print(json.dumps(self.log), file=logs)

    def contacts(self, point):
        for w1 in self.Workers:
            for w2 in self.Workers:
                if w1 != w2:
                    if w1.location == w2.location:
                        self.log.append({'time': point,'id1': w1.id, 'id2': w2.id, 'rssi': 1 })


s = Simulator(2, 10)
s.run()