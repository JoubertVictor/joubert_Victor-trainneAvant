import pygame
import sys
import json
from pygame.locals import *

# Inicialização do pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fontes
font = pygame.font.Font(None, 36)

# Função para desenhar o texto na tela
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Classe para gerenciar usuários
class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.filename, 'w') as file:
            json.dump(self.users, file)

    def register_user(self, username):
        if not username:
            print("Nome de usuário não pode estar vazio!")
            return False
        if username in self.users:
            print(f"Usuário {username} já existe!")
            return False
        self.users[username] = {"high_score": 0}
        self.save_users()
        print(f"Usuário {username} registrado com sucesso!")
        return True

    def update_high_score(self, username, score):
        if username in self.users and score > self.users[username]["high_score"]:
            self.users[username]["high_score"] = score
            self.save_users()

# Classe para o jogador
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 50)
        self.speed = 10

    def move(self, mouse_x):
        self.rect.centerx = mouse_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)

# Classe para o jogo
class Game:
    def __init__(self, username, user_manager):
        self.username = username
        self.user_manager = user_manager
        self.player = Player()
        self.bullets = []
        self.enemies = [pygame.Rect(x * 60, 50, 40, 40) for x in range(10)]
        self.clock = pygame.time.Clock()
        self.score = 0
        self.level = 1

    def run(self):
        while True:
            screen.fill(BLACK)
            draw_text(f'Score: {self.score}  Level: {self.level}', font, WHITE, screen, 10, 10)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    self.bullets.append(pygame.Rect(self.player.rect.centerx - 2, self.player.rect.y - 10, 5, 10))

            mouse_x, _ = pygame.mouse.get_pos()
            self.player.move(mouse_x)

            for bullet in self.bullets[:]:
                bullet.move_ip(0, -5)
                if bullet.bottom < 0:
                    self.bullets.remove(bullet)

            for enemy in self.enemies[:]:
                enemy.move_ip(0, self.level)
                if enemy.bottom > HEIGHT:
                    print("Game Over!")
                    self.user_manager.update_high_score(self.username, self.score)
                    pygame.time.delay(2000)  # Adicionar um delay de 2 segundos
                    return

            for bullet in self.bullets[:]:
                for enemy in self.enemies[:]:
                    if bullet.colliderect(enemy):
                        self.bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        self.score += 10

            if not self.enemies:
                self.level += 1
                self.enemies = [pygame.Rect(x * 60, 50, 40, 40) for x in range(10)]

            self.player.draw(screen)
            for bullet in self.bullets:
                pygame.draw.rect(screen, RED, bullet)
            for enemy in self.enemies:
                pygame.draw.rect(screen, GREEN, enemy)

            pygame.display.flip()
            self.clock.tick(60)

# Classe para o menu principal
class MainMenu:
    def __init__(self):
        self.user_manager = UserManager()

    def display(self):
        while True:
            screen.fill(BLACK)
            draw_text('Space Invaders', font, WHITE, screen, 300, 100)
            draw_text('1. Jogar', font, WHITE, screen, 300, 200)
            draw_text('2. Registrar Usuário', font, WHITE, screen, 300, 250)
            draw_text('3. Sair', font, WHITE, screen, 300, 300)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        username = self.select_user()
                        if username:
                            game = Game(username, self.user_manager)
                            game.run()
                    elif event.key == K_2:
                        self.register_user()
                    elif event.key == K_3:
                        pygame.quit()
                        sys.exit()

    def register_user(self):
        input_active = False
        username = ""

        while True:
            screen.fill(BLACK)
            draw_text('Registrar Usuário', font, WHITE, screen, 300, 100)
            draw_text('Digite o nome e pressione Enter:', font, WHITE, screen, 300, 200)

            box_color = BLUE if input_active else WHITE
            pygame.draw.rect(screen, box_color, (300, 250, 200, 40), 2)
            draw_text(username, font, WHITE, screen, 310, 260)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if 300 <= event.pos[0] <= 500 and 250 <= event.pos[1] <= 290:
                        input_active = True
                    else:
                        input_active = False
                if event.type == KEYDOWN:
                    if input_active:
                        if event.key == K_RETURN:
                            if self.user_manager.register_user(username):
                                return
                        elif event.key == K_BACKSPACE:
                            username = username[:-1]
                        else:
                            username += event.unicode

    def select_user(self):
        users = list(self.user_manager.users.keys())
        selected_user = None
        while not selected_user:
            screen.fill(BLACK)
            draw_text('Selecione um Usuário', font, WHITE, screen, 300, 100)
            for i, user in enumerate(users):
                draw_text(f'{i + 1}. {user}', font, WHITE, screen, 300, 150 + i * 40)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    try:
                        selected_user = users[int(event.unicode) - 1]
                    except (ValueError, IndexError):
                        pass
        return selected_user

# Executar o menu principal
if __name__ == "__main__":
    menu = MainMenu()
    menu.display()