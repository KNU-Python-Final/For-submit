angel_90_str = 'angel_90'

angel_90_1_path = './assets/2round_images/angel_90/1.png'
angel_90_2_path = './assets/2round_images/angel_90/2.png'
angel_90_3_path = './assets/2round_images/angel_90/3.png'
angel_90_4_path = './assets/2round_images/angel_90/4.png'
angels_90_path = [
    angel_90_1_path, 
    angel_90_2_path, 
    angel_90_3_path, 
    angel_90_4_path, 
]

heart_angel_90_str = 'heart_angel_90'
heart_angel_90_1_path = './assets/2round_images/heart_angel_90/1.png'
heart_angel_90_2_path = './assets/2round_images/heart_angel_90/2.png'
heart_angel_90_3_path = './assets/2round_images/heart_angel_90/3.png'
heart_angel_90_4_path = './assets/2round_images/heart_angel_90/4.png'
heart_angels_path = [
    heart_angel_90_1_path, 
    heart_angel_90_2_path, 
    heart_angel_90_3_path, 
    heart_angel_90_4_path, 
]


king_90_str = 'king_90'

king_90_1_path = './assets/2round_images/king_90/1.png'
king_90_2_path = './assets/2round_images/king_90/2.png'
king_90_3_path = './assets/2round_images/king_90/3.png'
king_90_4_path = './assets/2round_images/king_90/4.png'
kings_path = [
    king_90_1_path, 
    king_90_2_path, 
    king_90_3_path, 
    king_90_4_path, 
]


heart_king_90_str = 'heart_king_90'

heart_king_90_1_path = './assets/2round_images/heart_king_90/1.png'
heart_king_90_2_path = './assets/2round_images/heart_king_90/2.png'
heart_king_90_3_path = './assets/2round_images/heart_king_90/3.png'
heart_king_90_4_path = './assets/2round_images/heart_king_90/4.png'
heart_kings_path = [
    heart_king_90_1_path, 
    heart_king_90_2_path, 
    heart_king_90_3_path, 
    heart_king_90_4_path, 
]


leaf_90_str = 'leaf_90'

leaf_90_1_path = './assets/2round_images/leaf_90/1.png'
leaf_90_2_path = './assets/2round_images/leaf_90/2.png'
leaf_90_3_path = './assets/2round_images/leaf_90/3.png'
leaf_90_4_path = './assets/2round_images/leaf_90/4.png'
leafs_path = [
    leaf_90_1_path, 
    leaf_90_2_path, 
    leaf_90_3_path, 
    leaf_90_4_path, 
]


heart_leaf_90_str = 'heart_leaf_90'

heart_leaf_90_1_path = './assets/2round_images/heart_leaf_90/1.png'
heart_leaf_90_2_path = './assets/2round_images/heart_leaf_90/2.png'
heart_leaf_90_3_path = './assets/2round_images/heart_leaf_90/3.png'
heart_leaf_90_4_path = './assets/2round_images/heart_leaf_90/4.png'
heart_leafs_path = [
    heart_leaf_90_1_path, 
    heart_leaf_90_2_path, 
    heart_leaf_90_3_path, 
    heart_leaf_90_4_path, 
]


santa_90_str = 'santa_90'

santa_90_1_path = './assets/2round_images/santa_90/1.png'
santa_90_2_path = './assets/2round_images/santa_90/2.png'
santa_90_3_path = './assets/2round_images/santa_90/3.png'
santa_90_4_path = './assets/2round_images/santa_90/4.png'
santas_path = [
    santa_90_1_path,
    santa_90_2_path,
    santa_90_3_path,
    santa_90_4_path,
]


heart_santa_90_str = 'heart_santa_90'

heart_santa_90_1_path = './assets/2round_images/heart_santa_90/1.png'
heart_santa_90_2_path = './assets/2round_images/heart_santa_90/2.png'
heart_santa_90_3_path = './assets/2round_images/heart_santa_90/3.png'
heart_santa_90_4_path = './assets/2round_images/heart_santa_90/4.png'
heart_santas_path = [
    heart_santa_90_1_path,
    heart_santa_90_2_path,
    heart_santa_90_3_path,
    heart_santa_90_4_path,
]

default_90_str = 'default_90'

default_90_1_path = './assets/2round_images/default_90/1.png'
default_90_2_path = './assets/2round_images/default_90/2.png'
default_90_3_path = './assets/2round_images/default_90/3.png'
default_90_4_path = './assets/2round_images/default_90/4.png'
defaults_path = [
    default_90_1_path, 
    default_90_2_path, 
    default_90_3_path, 
    default_90_4_path, 
]

def get_image_path_90(name: str) -> str:
    if name == default_90_str:
        return default_90_1_path
    elif name == king_90_str:
        return king_90_1_path
    elif name == heart_king_90_str:
        return heart_king_90_1_path
    elif name == leaf_90_str:
        return leaf_90_1_path
    elif name == heart_leaf_90_str:
        return heart_leaf_90_1_path
    elif name == angel_90_str:
        return angel_90_1_path
    elif name == heart_angel_90_str:
        return heart_angel_90_1_path
    elif name == santa_90_str:
        return santa_90_1_path
    elif name == heart_santa_90_str:
        return heart_santa_90_1_path
    else:
        return '' # error

def get_images_path_90(name: str) -> list[str]:
    if name == default_90_str:
        return defaults_path
    elif name == king_90_str:
        return kings_path
    elif name == heart_king_90_str:
        return heart_kings_path
    elif name == leaf_90_str:
        return leafs_path
    elif name == heart_leaf_90_str:
        return heart_leafs_path
    elif name == angel_90_str:
        return angels_90_path
    elif name == heart_angel_90_str:
        return heart_angels_path
    elif name == santa_90_str:
        return santas_path
    elif name == heart_santa_90_str:
        return heart_santas_path
    else:
        return [] # error