import osfrom pygame import *import blocksimport monstersfrom settings import MOVE_SPEED, MOVE_EXTRA_SPEED, PLATFORM_WIDTH, PLAYER_HEIGHT, PLATFORM_COLOR, POWER_JUMP, \    POWER_EXTRA_JUMP, GRAVITY, ANIMATION_DELAY, ANIMATION_SUPER_SPEED_DELAY,ICON_DIR, ANIMATION_LEFT, ANIMATION_RIGHT, \    ANIMATION_JUMP, ANIMATION_JUMP_LEFT, ANIMATION_JUMP_RIGHT, ANIMATION_STAYclass Player(sprite.Sprite):    def __init__(self):        # sprite.Sprite.__init__(self)        super.__init__(self)    def update(self, left, right, up, run, platform):        if up:            pass        if left:            pass        if right:            pass    def collide(self, x_value, y_value, platform):        pass    def teleporting(self, go_x, go_y):        self.rect.x = go_x        self.rect.y = go_y    def die(self):        time.wait(500)        self.teleport(self.start_x, self.start_y)