import frame
import pygame


class DisplayFrame(frame.Frame):
    def __init__(self, width, height, framerate, model):
        self.width = width
        self.height = height
        self.framerate = framerate
        self.model = model
        pygame.init()
        pygame.display.update()


    def update(self):
        finished = False
        
        draw_old_t = float(pygame.time.get_ticks())
        model_old_t = draw_old_t
        draw_delay = 1000.0 / self.framerate
        model_delay = 1000.0 / self.model.get_update_rate()
        # print_delay = 1000.0
        # print_old_t = draw_old_t
        # draw_ticks = 0
        # model_ticks = 0
        
        while not finished:
            current_t = pygame.time.get_ticks()
            draw_t = current_t - draw_old_t
            model_t = current_t - model_old_t
            # print_t = current_t - print_old_t
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

            if draw_t >= draw_delay:
                self.model.draw()
                pygame.display.update()
                draw_old_t = current_t
                # draw_ticks += 1

            if model_t >= model_delay:
                self.model.update()
                model_old_t = current_t
                # model_ticks += 1

            # if print_t >= print_delay:
            #     print(draw_ticks, model_ticks)
            #     print_old_t = current_t
            #     draw_ticks = 0
            #     model_ticks = 0
            
