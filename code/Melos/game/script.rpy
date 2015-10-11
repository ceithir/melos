define antiope = Character("Antiope", image="antiope")
image antiope:
    Image("sprites/antiope/default.png")
    zoom 0.25

image bg poetry = Image("images/bg/intro.jpg")
image bg inside = LiveTile("images/bg/inside.jpg")

label start:
    jump intro
