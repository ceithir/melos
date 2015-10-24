define antiope = Character("Antiope", image="antiope")
define ambrosia = Character("Ambrosia")

image antiope:
    Image("sprites/antiope/default.png")
    zoom 0.25

image bg poetry = Image("images/bg/intro.jpg")
image bg inside = LiveTile("images/bg/inside.jpg")
image bg garden = LiveTile("images/bg/dark-garden.jpg")
image bg sky = LiveTile("images/bg/sky.jpg")
image bg black = Solid("#000")

label start:
    # Has Antiope drunk too much and only keep hazy memories of the night?
    $ dreamer = True

    # If Ambrosia has it _really_ bad
    $ despair = False

    jump intro
