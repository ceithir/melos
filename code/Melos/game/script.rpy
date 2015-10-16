define antiope = Character("Antiope", image="antiope")
define ambrosia = Character("Ambrosia")

image antiope:
    Image("sprites/antiope/default.png")
    zoom 0.25

image bg poetry = Image("images/bg/intro.jpg")
image bg inside = LiveTile("images/bg/inside.jpg")

# Has Antiope drunk too much and only keep hazy memories of the night?
$ dreamer = True

label start:
    jump intro
