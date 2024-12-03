from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname        # Имя пользователя
        self.password = hash(password)  # Пароль в хешированном виде, число
        self.age = age                  # Возраст

    def __str__(self):
        return f'{self.nickname}'

class Video:

    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):

        self.title = title           # Заголовок, строка
        self.duration = duration     # Продолжительность, секунды
        self.time_now = time_now     # Секунда остановки (изначально 0)
        self.adult_mode = adult_mode # Ограничение по возрасту, bool (False по умолчанию)

class UrTube:

    def __init__(self):
        self.users = []             # Cписок объектов User
        self.videos = []            # Текущий пользователь, User
        self.current_user = None    # Текущий пользователь, User



    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User (nickname,password,age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован и вошел в систему')

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def log_out(self):
        self.current_user = None
        print('Вы вышли из системы')

    def add(self, *args):
        for movie in args:
            if movie.title not in (video.title for video in self.videos):
                self.videos.append(movie)

    def get_videos(self, word):
        list_videos = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                list_videos.append(video.title)
        return list_videos


    def watch_video(self, title):
        if not self.current_user:
            print('Для просмотра видео войдите в аккаунт')
            return

        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, просмотр данного видео запрещен')

                else:
                    print(f'Просмотр видео {title}')
                    video.time_now = 1
                    while video.time_now <= video.duration:
                        print(video.time_now, end=' ')
                        sleep(1)
                        video.time_now += 1

                    print('\nКонец видео')
                    video.time_now = 0
                    return
        print(f'Видео {title} не существует')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 2, adult_mode=True)

    #Добавление видео
    ur.add(v1, v2)


    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    ur.log_out()

