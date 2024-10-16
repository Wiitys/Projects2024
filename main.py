import pygame

pygame.init()

m_width, m_height = 1080,720
WIN = pygame.display.set_mode((m_width, m_height))
pygame.display.set_caption("Jeu de Dames")

def main():

    v_clock = pygame.time.Clock()
    v_run = True

    while v_run:
        v_clock.tick(60)
        for v_event in pygame.event.get():
            if v_event.type == pygame.QUIT:
                v_run = False

        pygame.display.update()

    pygame.quit()
 

if __name__ == "__main__":
    main()