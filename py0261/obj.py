class CleanCom(object):
    __zhang_ben = 5

    def clean_city(self):
        """清理城市街道"""
        pass

    def __salary(self):
        pass


class ChildCleanCom(CleanCom):
    pass


xuyang = CleanCom()
xuyang.clean_city()
print(dir(xuyang))
print(help(xuyang.clean_city))

