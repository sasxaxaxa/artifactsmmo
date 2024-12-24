import http
import json
import time
from parse_file import *


token = parse_file(r'ur_path')


def get_coordinates():
    with open('coordinates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for item in data['coordinates']:
        print(f"{item['name']}, X: {item['x']}, Y: {item['y']}")


def move(name, cor1, cor2):
    payload = "{\n  \"x\": a,\n  \"y\": b\n}".replace("a", str(cor1), 1).replace("b", str(cor2), 1)
    call("move", payload, name)


def fight_monster(name, num):
    payload = ""
    for i in range(num):
        call("fight", payload, name)
        time.sleep(34)


def gathering(name, num):
    payload = ""
    for i in range(num):
        call("gathering", payload, name)
        time.sleep(25)


def crafting(name, code, quantity):
    payload = "{" + f"\n  \"code\": \"{code}\",\n" + f"  \"quantity\": {quantity}\n" + "}"
    call("crafting", payload, name)


def equip(name, code, slot, quantity):
    payload = "{" + f"\n  \"code\": \"{code}\",\n  \"slot\": \"{slot}\",\n  \"quantity\": {quantity}\n" + "}"
    call("equip", payload, name)


def unequip(name, slot, quantity):
    payload = "{" + f"\n  \"slot\": \"{slot}\",\n  \"quantity\": {quantity}\n" + "}"
    call("unequip", payload, name)


def deposit(name, code, quantity):
    payload = "{" + f"\n  \"code\": \"{code}\",\n  \"quantity\": {quantity}\n" + "}"
    call("bank/deposit", payload, name)
    time.sleep(4)


def withdraw(name, code, quantity):
    payload = "{" + f"\n  \"code\": \"{code}\",\n  \"quantity\": {quantity}\n" + "}"
    call("bank/withdraw", payload, name)
    time.sleep(4)


def deposit_gold(name, quantity):
    payload = "{" + f"\n  \"quantity\": {quantity}\n" + "}"
    call("bank/deposit/gold", payload, name)
    time.sleep(4)


def withdraw_gold(name, quantity):
    payload = "{" + f"\n  \"quantity\": {quantity}\n" + "}"
    call("bank/withdraw/gold", payload, name)
    time.sleep(4)


def recycling(name, code, quantity):
    payload = "{" + f"\n  \"code\": \"{code}\",\n  \"quantity\": {quantity}\n" + "}"
    call("recycling", payload, name)


def ge_buy(name, code, quantity, price):
    payload = "{" + f"\n  \"code\": \"{code}\",\n  \"quantity\": {quantity},\n  \"price\": {price}\n" + "}"
    call("ge/buy", payload, name)


def create_char(name_char, skin_char):
    payload = "{" + f"\n  \"name\": \"{name_char}\",\n  \"skin\": \"{skin_char}\"\n" + "}"
    post("/characters/create", payload)


def call(type_of_action, payload, name):
    conn = http.client.HTTPSConnection("api.artifactsmmo.com")
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer " + token
    }
    url = f"/my/{name}/action/{type_of_action}"
    conn.request("POST", url, payload, headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    print(data)

    return data


def post(type_of_action, payload):
    conn = http.client.HTTPSConnection("api.artifactsmmo.com")
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer " + token
    }
    url = f"/{payload}"
    conn.request("POST", url, payload, headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    print(data)

    return data

