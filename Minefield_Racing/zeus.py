import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zeuz")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/zeus.png").convert(),(40,65))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		self.stun = False
		self.stun_counter = True
		self.start_time = 0
		self.thunder_counter = True
		self.start_time2 = 0
		self.tunder = False
		self.start_time3 = 0
		self.mine_counter = True
		self.min = False
	
	def thunder(self):
		pass


class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT * 1//3
		
		
	def update(self):
		now = pygame.time.get_ticks()
		if self.stun_counter:
			if self.stun:
				self.stun = False
				self.stun_counter = False
				self.start_time = pygame.time.get_ticks()
		if not self.stun_counter:
			if now - self.start_time >= 3000:
				self.stun_counter = True
		if self.thunder_counter:
			if self.tunder:
				self.tunder = False
				self.thunder_counter = False
				self.start_time2 = pygame.time.get_ticks()
		if not self.thunder_counter:
			if now - self.start_time2 >= 6000:
				self.thunder_counter = True
		if self.mine_counter:
			if self.min:
				self.min = False
				self.mine_counter = False
				self.start_time3 = pygame.time.get_ticks()
		if not self.mine_counter:
			if now - self.start_time3 >= 12000:
				self.mine_counter = True

		self.hp += 1/70
		self.mana += 1/180
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if not self.stun:
			if keystate[pygame.K_a]:
				self.speed_x = -5
			if keystate[pygame.K_d]:
				self.speed_x = 5
			self.rect.x += self.speed_x
			if keystate[pygame.K_w]:
				self.speed_y = -5
			if keystate[pygame.K_s]:
				self.speed_y = 5
			self.rect.y += self.speed_y
		if self.rect.right > WIDTH + self.rect.x:
			self.rect.right = WIDTH + self.rect.x
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 10:
			self.rect.top = 10
		if self.rect.bottom > 700:
			self.rect.bottom = 700

	def mine(self):
		if self.mana >= 30:
			self.mana -= 30
			self.min = True
			mine = Mine1()
			mine.rect.x, mine.rect.y = self.rect.bottomleft
			mine3_list.add(mine)
			all_sprites.add(mine)

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT * 2//3
		
		
	def update(self):
		now = pygame.time.get_ticks()
		if self.stun_counter:
			if self.stun:
				self.stun = False
				self.stun_counter = False
				self.start_time = pygame.time.get_ticks()
		if not self.stun_counter:
			if now - self.start_time >= 3000:
				self.stun_counter = True
		if self.thunder_counter:
			if self.tunder:
				self.tunder = False
				self.thunder_counter = False
				self.start_time2 = pygame.time.get_ticks()
		if not self.thunder_counter:
			if now - self.start_time2 >= 6000:
				self.thunder_counter = True
		if self.mine_counter:
			if self.min:
				self.min = False
				self.mine_counter = False
				self.start_time3 = pygame.time.get_ticks()
		if not self.mine_counter:
			if now - self.start_time3 >= 12000:
				self.mine_counter = True

		self.hp += 1/70
		self.mana += 1/180
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if not self.stun:
			if keystate[pygame.K_LEFT]:
				self.speed_x = -5
			if keystate[pygame.K_RIGHT]:
				self.speed_x = 5
			self.rect.x += self.speed_x
			if keystate[pygame.K_UP]:
				self.speed_y = -5
			if keystate[pygame.K_DOWN]:
				self.speed_y = 5
			self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH + self.rect.x:
			self.rect.right = WIDTH + self.rect.x
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 10:
			self.rect.top = 10
		if self.rect.bottom > 700:
			self.rect.bottom = 700

	def mine(self):
		if self.mana >= 30:
			self.mana -= 30
			self.min = True
			mine = Mine1()
			mine.rect.x, mine.rect.y = self.rect.bottomleft
			mine4_list.add(mine)
			all_sprites.add(mine)

class Mine1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/mine1.png").convert(),(30,30))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(100, WIDTH-100)
		self.ngo_list = [110, 240, 370, 500]
		self.rect.y = random.randrange(10, HEIGHT-50)
		self.num = 0
		
    
	def update(self):
		if self.num == 1:
			self.image = pygame.transform.scale(pygame.image.load("img/mine1.png").convert(),(30,30))
		else:
			self.image = pygame.image.load("img/fond.png").convert()

class Mine2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/mine22.png").convert(),(30,30))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(100, WIDTH-100)
		self.ngo_list = [110, 240, 370, 500]
		self.rect.y = random.randrange(10 , HEIGHT-50)
		self.num = 0
		
	def update(self):
		if self.num == 1:
			self.image = pygame.transform.scale(pygame.image.load("img/mine22.png").convert(),(30,30))
		else:
			self.image = pygame.image.load("img/fond.png").convert()


def show_go_screen():
	
	screen.fill(BLACK)
	draw_text1(screen, "Mines", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "llega a la meta", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False


game_over = True
running = True
thunder_time = 0
while running:
	if game_over:

		show_go_screen()
		screen.fill(WHITE)
		game_over = False
		
		all_sprites = pygame.sprite.Group()
		mine1_list = pygame.sprite.Group()
		mine2_list = pygame.sprite.Group()
		mine3_list = pygame.sprite.Group()
		mine4_list = pygame.sprite.Group()
		p1_list = pygame.sprite.Group()
		p2_list = pygame.sprite.Group()
		players = pygame.sprite.Group()
		player1 = Player1()
		player2 = Player2()
		all_sprites.add(player1, player2)
		players.add(player1, player2)
		p1_list.add(player1)
		p2_list.add(player2)
		counter1 = False
		counter2 = False
		counter11 = True
		counter22 = True
		mine_counter = True

		for i in range(100):
			mine1 = Mine1()
			all_sprites.add(mine1)
			mine1_list.add(mine1)
		
		for i in range(15):
			mine2 = Mine2()
			all_sprites.add(mine2)
			mine2_list.add(mine2)
	
		score = 0
		

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_f:
				if player1.thunder_counter:
					player1.thunder()
					player1.tunder = True
					for m in mine1_list:
						m.num = 1
					for m in mine2_list:
						m.num = 1

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				if player2.thunder_counter:
					player2.thunder()
					player2.tunder = True
					for m in mine1_list:
						m.num = 1
					for m in mine2_list:
						m.num = 1

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_g:
				if player1.mine_counter:
					player1.mine()
					player1.min = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_o:
				if player2.mine_counter:
					player2.mine()
					player2.min = True
			

	now = pygame.time.get_ticks()

	if mine_counter:
		for m in mine1_list:
			if m.num == 1:
				mine_counter = False
				start_time = pygame.time.get_ticks()
	if not mine_counter:
		if now - start_time >= 1300:
			for m in mine1_list:
				m.num = 0
			for m in mine2_list:
				m.num = 0
			mine_counter = True
	if counter11:
		if len(p1_list) == 0:
			p1now = pygame.time.get_ticks()
			counter1 = True
			counter11 = False
	if counter1:
		if now - p1now >= 6000:
			player1 = Player1()
			all_sprites.add(player1)
			p1_list.add(player1)
			counter1 = False
	if counter22:
		if len(p2_list) == 0:
			p2now = pygame.time.get_ticks()
			counter2 = True
			counter22 = False
	if counter2:
		if now - p2now >= 6000:
			player2 = Player2()
			all_sprites.add(player2)
			p2_list.add(player2)
			counter2 = False
			
	if player1.rect.centerx > WIDTH:
		game_over = True
	if player2.rect.centerx > WIDTH:
		game_over = True
	
	all_sprites.update()

	for m in mine1_list:
		for p in players:
			if pygame.sprite.collide_rect(m,p):
				m.kill()
				p.hp -= 40

	for m in mine2_list:
		for p in players:
			if pygame.sprite.collide_rect(m,p):
				p.stun = True
				m.kill()	

	for m in mine3_list:
		if pygame.sprite.collide_rect(m, player2):
			m.kill()
			player2.hp -= 40

	for m in mine4_list:
		if pygame.sprite.collide_rect(m, player1):
			m.kill()
			player2.hp -= 40

	screen.fill(WHITE)

	all_sprites.draw(screen)
	
	# hp - mana bars.
	if player1.hp > 0:
		draw_hp_bar(screen, 5, 5, player1.hp)
		draw_text2(screen, str(int(player1.hp)) + "/100", 10, 25, 6)
		draw_hp_bar(screen, player1.rect.x, player1.rect.y - 5, player1.hp)
		draw_mana_bar(screen, 5, 15, player1.mana)
		draw_text1(screen, str(int(player1.mana))+ "/100", 10, 25, 16)
	if player2.hp > 0:
		draw_hp_bar(screen, 600, 5, player2.hp)
		draw_text2(screen, str(int(player2.hp))+ "/100", 10, 625, 6)
		draw_hp_bar(screen, player2.rect.x, player2.rect.y - 5, player2.hp)
		draw_mana_bar(screen, 600, 15, player2.mana)
		draw_text1(screen, str(int(player2.mana))+ "/100", 10, 625, 16)

	pygame.display.flip()