import sys
import streamlit as sl
import os
from pathlib import Path

BASE_REPO_PATH = str(Path(os.path.abspath(__file__)).resolve().parent.parent.parent)
print(BASE_REPO_PATH)
sys.path.append(BASE_REPO_PATH)
sys.path.append(os.path.join(BASE_REPO_PATH, "BeyondChaosRandomizer\\BeyondChaos"))

from BeyondChaosRandomizer.BeyondChaos.options import NORMAL_FLAGS, MAKEOVER_MODIFIER_FLAGS, get_makeover_groups

get_makeover_groups()
SORTED_FLAGS = sorted(NORMAL_FLAGS + MAKEOVER_MODIFIER_FLAGS, key=lambda x: x.name)


@sl.cache_data
def load_female_character_names():
    names = ""
    with open(Path("BeyondChaosRandomizer\\BeyondChaos\\custom\\femalenames.txt")) as namefile:
        for line in namefile:
            names += line
    return names.strip()


@sl.cache_data
def load_male_character_names():
    names = ""
    with open(Path("BeyondChaosRandomizer\\BeyondChaos\\custom\\malenames.txt")) as namefile:
        for line in namefile:
            names += line
    return names.strip()


@sl.cache_data
def load_moogle_character_names():
    names = ""
    with open(Path("BeyondChaosRandomizer\\BeyondChaos\\custom\\mooglenames.txt")) as namefile:
        for line in namefile:
            names += line
    return names.strip()


@sl.cache_data
def load_sprite_replacements():
    sprite_data = ""
    with open(Path("BeyondChaosRandomizer\\BeyondChaos\\custom\\spritereplacements.txt")) as namefile:
        for line in namefile:
            sprite_data += line
    return sprite_data


def initialize_states():
    for flag in SORTED_FLAGS:
        if flag.inputtype == "boolean":
            sl.session_state[flag.name] = False
        elif flag.inputtype == "integer":
            sl.session_state[flag.name] = int(flag.default_value)
        elif flag.inputtype == "float2":
            sl.session_state[flag.name] = float(flag.default_value)
        elif flag.inputtype == "combobox":
            sl.session_state[flag.name] = flag.default_value

    sl.session_state["selected_flags"] = []
    sl.session_state["initialized"] = True
    sl.session_state["input_rom_data"] = None
    sl.session_state["output_files"] = None
    sl.session_state["female_names"] = load_female_character_names()
    sl.session_state["male_names"] = load_male_character_names()
    sl.session_state["moogle_names"] = load_moogle_character_names()
    sl.session_state["sprite_replacements"] = load_sprite_replacements()
    sl.session_state["batch"] = 1
    sl.session_state["seed"] = 0
    sl.session_state["gamemode"] = "Normal"
    sl.session_state["export_file_data"] = {}
