"""
Matthew Rieckenberg
matthew.paul.rieckenberg@gmail.com
Summer 2023

Description: Automates vanilla commands
in Minecraft Java
"""

import pyautogui as gui
import time
import random

class Minecraft_Automation_Class():
    def __init__(self):

        # TODO: update and optimize (go by material)
        self.materials = [
            "terracotta",
            "white_terracotta",
            "light_gray_terracotta",
            "gray_terracotta",
            "black_terracotta",
            "brown_terracotta",
            "red_terracotta",
            "orange_terracotta",
            "yellow_terracotta",
            "lime_terracotta",
            "green_terracotta",
            "cyan_terracotta",
            "light_blue_terracotta",
            "blue_terracotta",
            "purple_terracotta",
            "magenta_terracotta",
            "pink_terracotta",

            # Concretes
            "white_concrete",
            "light_gray_concrete",
            "gray_concrete",
            "black_concrete",
            "brown_concrete",
            "red_concrete",
            "orange_concrete",
            "yellow_concrete",
            "lime_concrete",
            "green_concrete",
            "cyan_concrete",
            "light_blue_concrete",
            "blue_concrete",
            "purple_concrete",
            "magenta_concrete",
            "pink_concrete",

            # Other materials
            "bricks",
            "cobblestone",
        ]

    # Send a vanilla command
    def send_command(self, command):
        print('/' + command)
        
        # # Comment out for testing
        # gui.press('/')
        # gui.typewrite(command)
        # gui.press('enter')

    def build_house_n_stories(self, start_x, start_y, start_z, length, width, height,
                              num_stories,):
        pass










# Call functions here
MC = Minecraft_Automation_Class()
# MC.send_command("testing")