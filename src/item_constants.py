import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_ITEMS = os.path.join(BASE_DIR, "assets", "icons", "objects_icons_mod.png")

ITEM_SPRITESHEET = None
SPRITE_COLS = 8
SPRITE_ROWS = 12

ALLOWED_ITEMS = {
    "apple": {
        "index": 0,
        "max_stack": 10,
        "description": "Una manzana rica y saludable"
    },
    "banana":{
        "index": 1,
        "max_stack": 10,
        "description": "Banana muy nutritiva"
    },
    "potion": {
        "index": 36,
        "max_stack": 5,
        "description": "Restaura 25 HP"
    },
    "key": {
        "index": 25,
        "max_stack": 1,
        "description": "Abre puertas especiales"
    }
}