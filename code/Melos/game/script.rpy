define antiope = Character("Antiope", image="antiope")
define ambrosia = Character("Ambrosia")

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
