# https://adventofcode.com/2019/day/1 (part 1, part 2)
# --- Part One ---
# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass, divide by three, 
# round down, and subtract 2.
#
# What is the sum of the fuel requirements for all of the modules on your spacecraft?
# 
# --- Part Two ---
# Apparently, you forgot to include additional fuel for the fuel you just added.
# Fuel itself requires fuel just like a module - take its mass, divide by three, 
# round down, and subtract 2. However, that fuel also requires fuel, and that fuel 
# requires fuel, and so on. Any mass that would require negative fuel should instead 
# be treated as if it requires zero fuel; the remaining mass, if any, is instead handled 
# by wishing really hard, which has no mass and is outside the scope of this calculation.


from typing import List, Generator
import re

def required_fuel_sum(masses:List[int]) -> int:
    fuel = 0
    for mass in masses:
        fuel += required_fuel(mass)
    return fuel


def required_fuel(mass:int) -> int:
    return mass // 3 - 2


def required_fuel_sum_rec(masses:List[int]) -> int:
    sum = 0
    for mass in masses:
        sum += all_fuel(mass)
    return sum


def all_fuel(mass:int) -> int:
    fuel_list:List[int] = list()
    fuel_list.append(fuel(mass))
    while fuel_list[-1] != 0:
        fuel_list.append(fuel(fuel_list[-1]))
    return sum(fuel_list)


def fuel(mass:int) -> int:
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel