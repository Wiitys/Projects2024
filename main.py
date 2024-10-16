import pygame

pygame.init()

WIDTH, HEIGHT = 1080,720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Dames")

def main():

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
 

if __name__ == "__main__":
    main()