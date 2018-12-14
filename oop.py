class Andela35:
    language = 'Python'

    def __init__(self, attendees, month, facilitators, duration=2):
        self.attendees = attendees
        self.month = month
        self.facilitators = facilitators
        self.duration = duration


class BootCamp(Andela35):
    def __init__(self, attendees, month, facilitators, duration=2):
        super().__init__(attendees, month, facilitators)

    # def change_facilitator(self):
        self.facilitators = self.attendees // 5

    # def Learner:
    #     backer = Learner()
    def add_learners(self, new_learners):
        self.attendees += new_learners


andela35dec = Andela35(70, 'Dec', 5, )
andela35nov = Andela35(70, 'Nov', 4, )
# andela35dec.add_learners(5)
btjan = BootCamp(70, 'jan', 5,)

# print(f'Andela35{andela35nov.month} has {andela35nov.attendees} attendees')
# print(f'Andela35{andela35dec.month} has {andela35dec.attendees} attendees')
# print(andela35dec.attendees, 'attendees')

# print(f'BootCamp{btjan.month} has {btjan.attendees}attendees')
