import pygame
import display_frame
import model_handler
import app_config

model = model_handler.ModelHandler(app_config.MODEL_RATE)
frame = display_frame.DisplayFrame(
    app_config.WIDTH,
    app_config.HEIGHT,
    app_config.FRAME_RATE,
    model
)

frame.update()
print("Finished!")
