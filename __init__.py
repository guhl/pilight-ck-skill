from mycroft import MycroftSkill, intent_file_handler


class PilightCk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ck.pilight.intent')
    def handle_ck_pilight(self, message):
        self.speak_dialog('ck.pilight')


def create_skill():
    return PilightCk()

