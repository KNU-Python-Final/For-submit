angel_str = 'angel'

angel_1_path = './assets/3round_images/angel/1.png'
angel_2_path = './assets/3round_images/angel/2.png'
angel_3_path = './assets/3round_images/angel/3.png'
angel_4_path = './assets/3round_images/angel/4.png'
angels_path = [
    angel_1_path, 
    angel_2_path, 
    angel_3_path, 
    angel_4_path, 
]

heart_angel_str = 'heart_angel'

heart_angel_1_path = './assets/3round_images/heart_angel/1.png'
heart_angel_2_path = './assets/3round_images/heart_angel/2.png'
heart_angel_3_path = './assets/3round_images/heart_angel/3.png'
heart_angel_4_path = './assets/3round_images/heart_angel/4.png'
heart_angels_path = [
    heart_angel_1_path, 
    heart_angel_2_path, 
    heart_angel_3_path, 
    heart_angel_4_path, 
]


king_str = 'king'

king_1_path = './assets/3round_images/king/1.png'
king_2_path = './assets/3round_images/king/2.png'
king_3_path = './assets/3round_images/king/3.png'
king_4_path = './assets/3round_images/king/4.png'
kings_path = [
    king_1_path, 
    king_2_path, 
    king_3_path, 
    king_4_path, 
]


heart_king_str = 'heart_king'

heart_king_1_path = './assets/3round_images/heart_king/1.png'
heart_king_2_path = './assets/3round_images/heart_king/2.png'
heart_king_3_path = './assets/3round_images/heart_king/3.png'
heart_king_4_path = './assets/3round_images/heart_king/4.png'
heart_kings_path = [
    heart_king_1_path, 
    heart_king_2_path, 
    heart_king_3_path, 
    heart_king_4_path, 
]


leaf_str = 'leaf'

leaf_1_path = './assets/3round_images/leaf/1.png'
leaf_2_path = './assets/3round_images/leaf/2.png'
leaf_3_path = './assets/3round_images/leaf/3.png'
leaf_4_path = './assets/3round_images/leaf/4.png'
leafs_path = [
    leaf_1_path, 
    leaf_2_path, 
    leaf_3_path, 
    leaf_4_path, 
]


heart_leaf_str = 'heart_leaf'

heart_leaf_1_path = './assets/3round_images/heart_leaf/1.png'
heart_leaf_2_path = './assets/3round_images/heart_leaf/2.png'
heart_leaf_3_path = './assets/3round_images/heart_leaf/3.png'
heart_leaf_4_path = './assets/3round_images/heart_leaf/4.png'
heart_leafs_path = [
    heart_leaf_1_path, 
    heart_leaf_2_path, 
    heart_leaf_3_path, 
    heart_leaf_4_path, 
]


default_str = 'default'

default_1_path = './assets/3round_images/default/1.png'
default_2_path = './assets/3round_images/default/2.png'
default_3_path = './assets/3round_images/default/3.png'
default_4_path = './assets/3round_images/default/4.png'
defaults_path = [
    default_1_path, 
    default_2_path, 
    default_3_path, 
    default_4_path, 
]

def get_image_path(name: str) -> str:
    if name == default_str:
        return default_1_path
    elif name == king_str:
        return king_1_path
    elif name == heart_king_str:
        return heart_king_1_path
    elif name == leaf_str:
        return leaf_1_path
    elif name == heart_leaf_str:
        return heart_leaf_1_path
    elif name == angel_str:
        return angel_1_path
    elif name == heart_angel_str:
        return heart_angel_1_path
    else:
        return '' # error

def get_images_path(name: str) -> list[str]:
    if name == default_str:
        return defaults_path
    elif name == king_str:
        return kings_path
    elif name == heart_king_str:
        return heart_kings_path
    elif name == leaf_str:
        return leafs_path
    elif name == heart_leaf_str:
        return heart_leafs_path
    elif name == angel_str:
        return angels_path
    elif name == heart_angel_str:
        return heart_angels_path
    else:
        return [] # error