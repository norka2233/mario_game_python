import osfrom pygame import *import blockimport monsterfrom settings import MOVE_SPEED, MOVE_EXTRA_SPEED, PLAYER_COLOR, PLAYER_WIDTH, PLAYER_HEIGHT, POWER_EXTRA_JUMP, POWER_JUMP, ICON_DIR, ANIMATION_JUMP, ANIMATION_RIGHT, ANIMATION_LEFT, ANIMATION_JUMP_LEFT, ANIMATION_STAY, ANIMATION_JUMP_RIGHT, ANIMATION_RIGHT, ANIMATION_SUPER_SPEED_DELAY, ANIMATion_DELAY,class Player(sprite.Sprite):    def __init__(self):        # sprite.Sprite.__init__(self)        super.__init__(self)    def update(self, left, right, up, run, platform):        if up:            pass        if left:            pass        if right:            pass    def collide(self, x_value, y_value, platform):        pass    def teleport(self, go_x, go_y):        self.rect.x = go_x        self.rect.y = go_y    def die(self):        time.wait(500)        self.teleport(self.start_x, start_y)