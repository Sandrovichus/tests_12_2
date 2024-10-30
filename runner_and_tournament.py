class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1

        while self.participants:
            speeds = []
            for i in self.participants:
                speeds.append(i.speed)
            max_speed = max(speeds)  # выявляем самого быстрого по скорости участника
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance and participant.speed == max_speed:  # включаем доп.
                    # условие для исключения случаев, когда самый медленный бегун оказывается пробежавшим быстрее
                    # при дистанции равной или меньше удвоенного значения скорости самого медленного бегуна
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
