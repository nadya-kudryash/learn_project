import requests
import json

def get_flags():
    final_dict=dict()
    url = "https://flagcdn.com/en/codes.json"
    info = requests.get(url).json()
    for key, value in info.items():
        if key.find("-")!=2:
            final_dict[value] = f"https://flagcdn.com/16x12/{key}.png"
    return final_dict

# get_flags()

def get_right_answer(d, link):
    for key, value in d.items():
        if value == link:
            return key