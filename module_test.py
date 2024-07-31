import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

import constants
constants.math_pi()
constants.speed_of_light()

import calculator
calculator.addition(*[14, 52, 33])
calculator.subtraction(82, 75)
calculator.multiplication(*[2, 8, 14])
calculator.division(25.2, 4)
calculator.int_division(35, 6)

from ecommerce import product_management, order_processing
product_management.product_details("friedge")
order_processing.place_order("friedge", 4, 44000)

import string_utils
string_utils.str_rev("Supriyo")
string_utils.str_cap("Piku")

import file_operations
file_operations.file_writing("supriyo.txt", "Hi!! Myself Supriyo Sarkar.")
file_operations.file_reading("supriyo.txt")
file_operations.file_appending("supriyo.txt", "I am a Mathematician.")
file_operations.file_reading("supriyo.txt")