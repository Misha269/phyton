from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

window.title = "3D Parkour - Custom Background & 3 Min Timer"
window.fps_counter.enabled = True

# --- ДОБАВЛЕНИЕ СВОЕГО ФОНА ---
# Убедитесь, что ваша картинка называется background.png (или background.jpg)
# и лежит в одной папке с этим скриптом!
try:
    Sky(texture='background', color=color.white)
except:
    # Запасной вариант, если картинка не найдена, чтобы игра не вылетала с ошибкой
    Sky(color=color.rgb(10, 10, 20))
    print("Внимание: Картинка background не найдена в папке! Убедитесь, что файл называется background.png")


# --- ПЕРСОНАЖ И ФИЗИКА ---

class ParkourPlayer(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.normal_speed = 10
        self.run_speed = 15
        self.speed = self.normal_speed

        # Настройка прыжка
        self.jump_height = 4
        self.jump_up_duration = 0.38

        self.has_double_jumped = False

    def update(self):
        super().update()

        # Бег на Shift
        if held_keys['left shift']:
            self.speed = self.run_speed
        else:
            self.speed = self.normal_speed

        if self.grounded:
            self.has_double_jumped = False

        # Возврат на старт при падении
        if self.y < -35:
            self.x = 0
            self.z = 0
            self.y = 8
            print_on_screen("YOU FELL! Try again!", position=(-0.15, 0), scale=2, color=color.red)

    def jump(self):
        if self.grounded:
            super().jump()
            self.has_double_jumped = False
        elif not self.has_double_jumped:
            self.y += 0.4
            self.air_time = 0
            self.animate_y(self.y + self.jump_height * 1.3, duration=self.jump_up_duration, curve=curve.out_expo)
            self.has_double_jumped = True

            spark = Entity(model='sphere', scale=0.4, color=color.cyan, position=self.position)
            destroy(spark, delay=0.2)


player = ParkourPlayer(
    model='capsule',
    z=0, x=0, y=5,
    color=color.cyan,
    origin_y=-0.5,
    collider='box'
)

mouse.sensitivity = Vec2(40, 40)

# --- СТАРТОВАЯ ПЛАТФОРМА И UI ТАЙМЕРА ---

start_platform = Entity(
    model='cube',
    scale=(10, 1, 10),
    position=(0, 0, 0),
    color=color.rgb(30, 30, 30),
    texture='white_cube',
    collider='box'
)
Entity(parent=start_platform, model='wireframe_cube', scale=1.01, color=color.green)

# Подсказка на экране
Text(text="PARKOUR:\nWASD - Move | SHIFT - Run\nSPACE - Jump (Double Jump!)",
     position=(-0.85, 0.45), scale=1.3, color=color.white)

# Текст таймера (3 минуты = 180 секунд)
game_time = 180.0
timer_text = Text(text="Time: 03:00", position=(0.55, 0.45), scale=2, color=color.yellow)
game_won = False
game_over = False

# --- ГЕНЕРАЦИЯ ПЛАТФОРМ ---

platforms = []
textures_list = ['white_cube', 'brick', 'grass', 'radial_gradient']
colors_list = [
    color.rgb(255, 50, 100),
    color.rgb(0, 200, 255),
    color.rgb(255, 140, 0),
    color.rgb(180, 50, 255),
    color.rgb(0, 255, 120),
    color.rgb(255, 230, 0)
]

last_pos = Vec3(0, 0, 0)

for i in range(50):
    offset_x = random.randint(-9, 9)
    offset_y = random.randint(1, 4)
    offset_z = random.randint(8, 14)

    last_pos += Vec3(offset_x, offset_y, offset_z)
    p_scale = (random.randint(4, 7), 1, random.randint(4, 7))

    block = Entity(
        model='cube',
        scale=p_scale,
        position=last_pos,
        color=random.choice(colors_list),
        texture=random.choice(textures_list),
        collider='box'
    )
    platforms.append(block)
    Entity(parent=block, model='wireframe_cube', scale=1.01, color=color.white)

# Финиш
finish_platform = Entity(
    model='cube',
    scale=(12, 1, 12),
    position=last_pos + Vec3(0, 2, 12),
    color=color.gold,
    texture='white_cube',
    collider='box'
)
Text(text="FINISH!", position=(0, 0.3), origin=(0, 0), scale=3, color=color.black, parent=finish_platform)


# --- ЛОГИКА ТАЙМЕРА И ПОБЕДЫ ---

def update():
    global game_time, game_won, game_over

    if game_won or game_over:
        return

    # Уменьшаем таймер каждую секунду
    game_time -= time.dt

    if game_time <= 0:
        game_time = 0
        game_over = True
        timer_text.text = "Time: 00:00"
        print_on_screen("TIME IS UP! YOU LOSE", position=(-0.2, 0), scale=3, color=color.red)
        application.pause()
        return

    # Форматирование времени в минуты и секунды (MM:SS)
    minutes = int(game_time // 60)
    seconds = int(game_time % 60)
    timer_text.text = f"Time: {minutes:02d}:{seconds:02d}"

    # Проверка победы (если дошли до финиша)
    if distance(player.position, finish_platform.position) < 6 and player.y >= finish_platform.y:
        game_won = True
        print_on_screen("VICTORY! YOU WIN!", position=(-0.2, 0.1), scale=3, color=color.gold)
        application.pause()


app.run()