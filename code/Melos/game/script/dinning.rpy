image eyes:
    Image("sprites/antiope/default.png")
    size (435, 85) crop (400, 275, 435, 85)

label antiope:

    #Music?

    scene bg inside

    stop music fadeout 5.0
    play music "music/Frozen_Silence_-_Harp.mp3" fadein 5.0

    "I advance quickly through the many rooms of the building, getting around and stepping over the many revelers crossing my path with a consummate skill. I have worked at many similar parties before, and experience taught me how to move with ease despite the chaotic crowd."

    "I make a breach through human walls with a smile and a gentle but firm arm, adroitly avoid stepping on discarded leftovers and other unsavory things, nicely dismiss people asking for a song."

    "While my reflexes alone handle my movements and keep my pace, I gaze at every single person, my sight jumping from face to face, hunting the only prey worth it. A hundred different eyes meet mine, but not the ones I desire. Until they finally lock into perfection."

    show eyes:
        alpha 0.0 xpos 423 ypos 255
        linear 0.5 alpha 1.0
    pause 0.5

    show eyes:
        alpha 1.0

    "They may right now display the slight luster symptomatic of an important consumption of alcohol. But they still shine like twin suns. The reflected flames of the candles dance upon the dark and brown ocean, shifting with the emotions of their owner. Enlarged from the surprise of the sudden encounter. Contracted as she observes the intruder. Sparkling when she recognizes me."

    show antiope behind eyes:
        alpha 0.0 xpos 23 ypos -20 zoom 4.0
        linear 0.5 alpha 1.0
    pause 0.5

    show antiope:
        alpha 1.0

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

    "She cocks an eyebrow at me not answering her mundane question."

    menu:
        "Remain silent":
            jump silence
        "Change topic":
            jump liar

label silence:
    "I sincerely think about outgoing the truth. I came there for this, to stop hiding. But now that we are face to face, my lips are sealed. I don't want to say a lie, as small as it could be, but still cannot open up."

    "So I stay silent, dismissing the question with a mysterious smile and a wave of the hand. She does not insist. Antiope is extremely protective of her own personal space, and respects the one of others with the same might."

    "She hands me a bunch of pastries wrapped in a small piece of fabric. I accept one and starts eating slowly, with little bites, savoring the moment far more than the cake. As for her, she devours them one by one in a single mouthful each and I remark that she has piled up enough food to feed a whole army. Following my glance, she displays a all teeth out smile."

    antiope "Eat like a wolf. As much as you can while you can, so to be ready for when you will have nothing eat."

    "Typical. She knows a seemingly endless list of rules, proverbs, little tales implying carnivorous animals and survival. This one is actually pretty tame compared to the most bloody, dark and depressing you've heard from her."

    "And she does live by them. Always stuffing herself to the limit each time the food is free. It's a wonder how she keeps her physique, even if her stupidly hard and harsh daily routine probably helps a lot."

    "Yet another habit one could find ridiculous at first, but touching once you realized it has been forcefully implemented into her, a scar from a childhood she refuses to talk about."

    "After finishing her (first) plate, she pours herself a cup of wine, then offers me one. The alcohol is a local brew, and even if it has been heavily watered down, the powerful smell is enough for me to understand how potent it still is."

    menu:
        "Accept":
            jump drunk
        "Decline":
            jump sobriety

label liar:
    #TODO
    return

label drunk:
    #TODO
    return

label sobriety:
    "I politely decline. Antiope shrugs and gulps her own portion. Then she resumes her feast."

    "Plates dance on the table as she engulfs then one after the other, swallowing exactly one cup of alcohol between each. Her rhythm is constant, fast-paced, inhuman, frightening. She does not savor anything, she just absorbs liquid and solid nutriments continuously, like some terrible mythological character cursed with eternal hunger."

    "She actually started sweating, and her skin is now turning red from the wine and the effort, fighting to keep her speed against her own fullness and inebriation. But she doesn't stop nonetheless."

    "I'm getting worried. Her meal trance is exceptionally extreme today, and this can only turn badly. The only time I saw herself eat and drink {i}that{/i} much, she made herself sick. She tried to play brave the next day and refused any help, but I cannot forget her weakness, her inability to even walk straight, her paleness, her badly hidden outbreaks of vomiting."

    "I should probably stop her now. But... Antiope is very {i}touchy{/i} about her food."

    menu:
        "Stop her anyway":
            $ dreamer = False
            jump stupor
        "Let her do as she pleases":
            jump sick

