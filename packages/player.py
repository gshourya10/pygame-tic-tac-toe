class Player:
    def __init__(self, avatar, avatar_img, name='Player'):
        self.avatar = avatar
        self.score = 0
        self.avatar_img = avatar_img
        if name == 'Player':
            self.name = name + ' ' + avatar
        else:
            self.name = name

    def get_name(self):
        return f'{self.name}'

    def get_avatar(self):
        return f'Avatar: {self.avatar}'

    def get_score(self):
        return f'Score: {self.score}'
