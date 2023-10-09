from pico2d import load_image


class IDLE:
    @staticmethod
    def do():
        print("Idle Doing")
        pass

    @staticmethod
    def enter():
        print("Idle Entry Action")
        pass

    @staticmethod
    def exit():
        print("Idle Exit Action")
        pass

    @staticmethod
    def draw():
        pass


class StateMachine:
    def __init__(self):
        self.cur_state = IDLE
        pass

    def start(self):
        self.cur_state.enter()
        pass

    def update(self):
        self.cur_state.do()
        pass

    def draw(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image("animation_sheet.png")
        self.state_machine = StateMachine()
        self.state_machine.start()

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(
            self.frame * 100, self.action * 100, 100, 100, self.x, self.y
        )
        self.state_machine.draw()
