import pygame
import display_frame
import model_handler

WIDTH = 800
HEIGHT = 600
MODEL_RATE = 500
FRAME_RATE = 60

frame = display_frame.DisplayFrame(
    WIDTH,
    HEIGHT,
    FRAME_RATE,
    model_handler.ModelHandler(WIDTH, HEIGHT, MODEL_RATE)
)

frame.update()
print("Finished!")
