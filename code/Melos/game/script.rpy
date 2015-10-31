define antiope = Character("Antiope", show_two_window=True)
define ambrosia = Character(
    "Ambrosia",
    show_two_window = True,
    image="ambrosia",
    show_side_image = ShowingSwitch(
        "ambrosia angry", Image("images/sprites/Ambrosia/Ambrosia_angry.png", ypos=500, xpos=35),
        "ambrosia smile", Image("images/sprites/Ambrosia/Ambrosia_smile.png", ypos=500, xpos=35),
        "ambrosia worried", Image("images/sprites/Ambrosia/Ambrosia_worried.png", ypos=500, xpos=35),
        "ambrosia default", Image("images/sprites/Ambrosia/Ambrosia.png", ypos=500, xpos=35),
        None, Null()
    )
)

image antiope: 
    Image("images/sprites/Antiope/Anthiope_normalb.png")
    zoom 0.27
image antiope angry:
    Image("images/sprites/Antiope/Anthiope_angryb.png")
    zoom 0.27
image antiope bliss:
    Image("images/sprites/Antiope/Anthiope_blissb.png")
    zoom 0.27
image antiope sad:
    Image("images/sprites/Antiope/Anthiope_sadb.png")
    zoom 0.27

# ShowingSwitch madness. Need to define a bunch of images as Null(), and call "show ambrosia" before the first time she speak in any scene
image ambrosia = Null()
image ambrosia default = Null()
image ambrosia angry = Null()
image ambrosia smile = Null()
image ambrosia worried = Null()

image bg poetry = Image("images/bg/1.jpg")
image bg inside = LiveTile("images/bg/inside.jpg")
image bg garden = LiveTile("images/bg/114cn3l.jpg")
image bg sky = LiveTile("images/bg/sky.jpg")
image bg black = Solid("#000")

label start:
    # Has Antiope drunk too much and only keep hazy memories of the night?
    $ dreamer = True

    # If Ambrosia has it _really_ bad
    $ despair = False

    jump intro
