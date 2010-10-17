import cocos


class Font(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def Label(self, text, **kw):
        label = cocos.text.Label(text, font_name=self.name, font_size=self.size, **kw)
        return label

TNR_32 = Font('Times New Roman', 32)
