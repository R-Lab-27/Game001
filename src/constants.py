import os

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 60

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_ITEMS = os.path.join(BASE_DIR, "assets", "icons", "objects_icons.png")

ITEM_SPRITESHEET = None

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
