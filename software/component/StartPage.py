from software.component.Buttons import Button
class StartPage:
    def __init__(self):
        self.start_button = Button("start")

    def show(self, screen):
        self.start_button.show(screen)

    def set_event(self, event):
        self.start_button.set_event(event)
