image eyes:
    Image("sprites/antiope/default.png")
    size (435, 85) crop (400, 275, 435, 85)

label antiope:
    #Background? Music?

    scene
    stop music fadeout 5.0
    play music "music/Frozen_Silence_-_Harp.mp3" fadein 5.0

    "I advance quickly through the many rooms of the building, getting around and stepping over the many revelers crossing my path with a consummate skill. I have worked at many similar parties before, and experience taught me how to move with ease despite the chaotic crowd."

    "I make a breach through human walls with a smile and a gentle but firm arm, adroitly avoid stepping on discarded leftovers and other unsavory things, nicely dismiss people asking for a song."

    "While my reflexes alone handle my movements and keep my pace, I gaze at every single person, my sight jumping from face to face, hunting the only prey worth it. A hundred different eyes meet mine, but not the ones I desire. Until they finally lock into perfection."

    show eyes:
        alpha 0.0 xpos 423 ypos 255
        linear .5 alpha 1.0

    "They may right now display the slight luster symptomatic of an important consumption of alcohol. But they still shine like twin suns. The reflected flames of the candles dance upon the dark and brown ocean, shifting with the emotions of their owner. Enlarged from the surprise of the sudden encounter. Contracted as she observes the intruder. Sparkling when she recognizes me."

    show antiope behind eyes:
        alpha 0.0 xpos 23 ypos -20 zoom 4.0
        linear .5 alpha 1.0

    "She half rises, hemmed in her movements by the food plate on her knees, but I stop her with a sign of the hand and sit at her side at the extremity of the narrow bench, pushing her a little. She holds back a grin and I show a mischievous smile. Her military mind had naturally chosen a position from which she could have easily fled. An advantage I just negated, cutting her way out."

    "From so close, it's obvious I'm at least half a head taller than her, which never ends to surprise me. She looks big in everyday life, thanks to her headstrong confidence and athletic build, but is actually pretty average when using factual measurements."

    hide eyes

    show antiope:
        linear 2.0 zoom 1.0 xpos 462 ypos 50
    pause 2.0

    "My shoulder brushes against her own, my robe touching the skin left nude on that place by her old style of clothing. Some judge it barbaric. She judges it practical. I judge it sexy as..."

    antiope "Ambrosia, where have you been? I looked after you when the party started, but you were nowhere to be found."

    "Her voice returns me to the real world. Sort of. Before answering, I savor my own name in her mouth like it is the divine nectar it refers to. She pronounces it with a slight but unmissable accent, giving it a strange sonority unique to her, a cute quirk I have learned to enjoy."

    "On the opposite side, despite my talents as a singer, I'm unable to breath proper life into her own name. I pronounce it perfectly, but it sounds so bland when it should ring like the thunder in the summer sky. {i}Antiope{/i}! A warrior name, an amazon name, a mythological name, yet one escaping me as her bearer escapes me."

    "I display a pale smile. I could easily answer truthfully. I could as easily direct the conversation in another direction. Or even more easily remain silent."

    return
