import random
import pygame
import os

pygame.init()
font = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((800, 600))
prompt_text = 'CHECK BET OR FOLD?'
user_text = ''
bet = 0
clock = pygame.time.Clock()


def load_background_image():
    background = pygame.image.load("/Users/dev_patel16/Documents/Pokergame/poker.png")
    return pygame.transform.scale(background, (800, 600))




def load_images():
    card_images = {}
    card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    for value in card_values:
        for suit in card_suits:
            card_name = f"{value} of {suit}"  
            file_name = f"{card_name}.png"  
            file_path = os.path.join("/Users/dev_patel16/Documents/Pokergame/cards", file_name) 
            try:
                card_images[card_name] = pygame.image.load(file_path)  
            except FileNotFoundError:
                print(f"Error: {file_path} not found.")  
    return card_images







def display_hand(screen, hand, start_x, y, card_images):
    x_space = start_x
    card_width = 70  
    card_height = 100 

    for card in hand:
        if card in card_images:
            card_image = card_images[card]
            card_image = pygame.transform.scale(card_image, (card_width, card_height))
            screen.blit(card_image, (x_space, y))
            x_space += card_width + 10
        else:
            print(f"Image for {card} not found.")

def create_deck():
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    deck = []
    for value in values:
        for suit in suits: 
            deck.append(f"{value} of {suit}")
    return deck 
def shuffle_deck(cards):
    random.shuffle(cards)
    return cards

background_image = load_background_image()
shuffled = shuffle_deck(create_deck())
card_images = load_images()
deck = create_deck()
flop = [shuffled.pop(), shuffled.pop(), shuffled.pop()]
player_1_hand = (shuffled.pop(), shuffled.pop())
fourth_card = shuffled.pop()
flop4 = flop.copy()
flop4.append(fourth_card)
fifth_card = shuffled.pop()

flop_width = len(flop) * 70 + (len(flop) - 1) * 10  
start_x = (800 - flop_width) // 2 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN: 
                user_text = ""
            else:
                user_text += event.unicode
    if user_text == "bet":
        prompt_text = "How much would you like to bet?"
    text_surface = font.render(prompt_text, True, (255,255,255))
    user_text_surface = font.render(user_text, True, (255,255,255) )
    screen.blit(background_image,(0,0))
    screen.blit(text_surface, (0,0))
    screen.blit(user_text_surface, (0, 40))
    display_hand(screen, flop, start_x, 200, card_images)  
    display_hand(screen, player_1_hand, start_x, 450, card_images)
    display_hand(screen, flop4 ,start_x , 200, card_images )
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
