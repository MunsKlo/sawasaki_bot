class User:

    def __init__(self, _id, _name, _mention, _msg_cursor=''):
        self.id = _id
        self.name = _name
        self.status = ""
        self.role = ""
        self.msg_cursor = _msg_cursor
        self.mention = _mention

    def msg_cursor_next(self, next_cat):
        if len(self.msg_cursor):
            self.msg_cursor += '/' + next_cat
        else:
            self.msg_cursor += next_cat

    def msg_cursor_back(self):
        if not len(self.msg_cursor):
            return

        next_backslash = False
        i = len(self.msg_cursor) - 1

        while not next_backslash:
            if self.msg_cursor[i] == '/' or i == 0:
                break

            i -= 1
        self.msg_cursor = self.msg_cursor[0:i]

    def set_cursor_to_start(self):
        self.msg_cursor = ''
