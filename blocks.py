import osfrom  pygame import *from settings import PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_COLOR, ICON_DIRclass Platform(sprite.Sprite):    def __init__(self, x, y):        # sprite.Sprite.__init__(self)        super().__init__()        passclass BlockDie(Platform):    def __init__(self, x, y):        passclass BlockTeleport(Platform):    def __int__(self, x, y):        pass    def update(self):        passclass Princess(Platform):    def __init__(self, x, y):        pass    def update(self):        pass