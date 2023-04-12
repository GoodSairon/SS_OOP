from string import punctuation as punct

class Text_processor:

    def __init__(self, string):
        self.string = string
        self.__ind = None

    def is_punktiantian(self, char):
        self.__ind = True if char in punct else False
        return self.__ind

    def get_clean_string(self):
        for char in self.string:
            if self.is_punktiantian(char) == True:
                self.string = self.string.replace(char, ' ')
            else:
                pass
        return self.string

class Text_loader:

    def __init__(self, string):
        self.__text_processor = Text_processor(string)
        self.__clean_string = None

    @property
    def clean_string(self):
        """Clean string"""
        return self.__clean_string

    @clean_string.setter
    def set_claen_text(self):
        self.__clean_string = self.__text_processor.get_clean_string()
        return self.__clean_string

    @clean_string.deleter
    def del_clean_string(self):
        del self.__clean_string

class Data_interface:

    def __init__(self, string):
        self.__text_loader = Text_loader(string)



a = Text_loader('hello,')

#a.set_claen_text()
#a.print_self()
