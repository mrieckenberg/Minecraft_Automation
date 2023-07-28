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

        # TODO: update materials and init
        self.colours = [
            "",
            "white",
            "light_gray",
            "gray",
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "lime",
            "green",
            "cyan",
            "light_blue",
            "blue",
            "purple",
            "magenta",
            "pink",
        ]

        self.blocktype = [
            "",
            "cracked",
            "mossy",
        ]

        self.terracottas = [
            colour + "_terracotta" for colour in self.colours
        ]

        self.concretes = [
            colour + "_concrete" for colour in self.colours
        ]

        self.wools = [
            colour + "_wool" for colour in self.colours
        ]

        self.new_materials = [
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

        self.old_materials = [
            "clay",
            "white_terracotta",
            "terracotta",
            "yellow_terracotta",
            "black_terracotta",
            "red_terracotta",
            "lime_terracotta",
            "pink_terracotta",
        ]

        # Any blocks that wish to be deleted
        self.delete_materials = [
            "dirt",
            # "gray_concrete",
            # "yellow_concrete",
        ]

        self.facing = [
            "north",
            "south",
            "east",
            "west"
        ]

        self.half = [
            "top",
            "bottom",
        ]

        self.old_stairs_materials = [
            "nether_brick_stairs",
            "red_nether_brick_stairs",
            "spruce_stairs",
        ]

        self.new_stairs_materials = [
            "cut_copper_stairs",
        ]

        self.old_slab_materials = [
            "nether_brick_slab",
            "red_nether_brick_slab",
            "spruce_slab",
        ]

        self.new_slab_materials = [
            "cut_copper_slab"
        ]

        self.old_cut_copper_stairs = [
            "exposed_cut_copper_stairs",
            "weathered_cut_copper_stairs",
            "oxidized_cut_copper_stairs",
        ]

        self.old_cut_copper_slabs = [
            "exposed_cut_copper_slab",
            "weathered_cut_copper_slab",
            "oxidized_cut_copper_slab"
        ]

        self.old_cut_copper_blocks = [
            "exposed_cut_copper",
            "weathered_cut_copper",
            "oxidized_cut_copper",
        ]

        self.unoxidized_copper_blocks = [
            "waxed_cut_copper",
            "cut_copper",
            "exposed_cut_copper",
            "weathered_cut_copper",
            "copper_block",
            "exposed_copper",
            "weathered_copper",
        ]

        self.oxidized_copper_blocks = [
            "exposed_cut_copper",
            "weathered_cut_copper",
            "exposed_copper",
            "weathered_copper",
            "oxidized_cut_copper",
        ]

        self.unoxidized_copper_stairs = [
            "waxed_cut_copper_stairs",
            "cut_copper_stairs",
            "exposed_cut_copper_stairs",
            "weathered_cut_copper_stairs"
        ]

        self.unoxidized_copper_slabs = [
            "waxed_cut_copper_slab",
            "cut_copper_slab",
            "exposed_cut_copper_slab",
            "weathered_cut_copper_slab"
        ]
    
    # Send a vanilla command
    def send_command(self, command):
        print('/' + command)
        
        # # Comment out for testing
        # gui.press('/')
        # gui.typewrite(command)
        # gui.press('enter')
        










# Call functions here
