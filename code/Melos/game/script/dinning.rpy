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
    "I answer without answering."

    ambrosia "I was here and there, doing what needed to be done and that I haven't got the occasion to do of late."

    "In an overplayed movement of the arm, I cover the room around us, and beyond that, the whole city."

    ambrosia "Preparing the festival took almost all our time these last two weeks. But that was worth it. Especially with the extraordinary performance you offered us this morning."

    antiope "An {i}extraordinary{/i} performance would have been to win."

    "I can't tell by her tone if she is joking or dead serious. I'm not sure she knows herself. When Antiope plays, it's always to win, but she couldn't really hope to defeat professional athletes which trained for months, sometimes years, for this particular type of race, on an adequate soil and with an exact distance in mind, while Antiope usually runs on uneven terrains for random periods of time."

    ambrosia "You can say that, but I still think your were... incredible."

    "My voice is casually cheerful, but I feel a far more ardent fire rising to my cheeks as my mind fills itself with the corresponding memories."

    "As per tradition, the morning was filled with numerous sportive events. Nothing as glorious as the Olympic games, but still a good deal of different competitions: jumping, wrestling, javelin throws, horse races... But I have little recollections of any of them, completely eclipsed by the one which dried out my throat. The foot race."

    "More exactly, it's not the competition itself which left me unable to speak. I cannot even remember the name of the one who won it. But I do remember that she took part in it."

    "It's not that unusual for a woman to participate in such an event. Actually, there is often a token Spartan female athlete alongside the males, and they generally do quite well. But that was not any woman. That was her."

    "Such events are first and foremost a present to the gods, and the competitors must be as resplendent as they are skilled, the sight of their nude bodies as much an offering as their actual performances. And resplendent she was."

    "I helped her oiled herself before dawn, a pleasant moment certainly, but there is an absurd difference between watching a greasy skin from close under the weak light of a candle and contemplating it shining under the bright sun. A thousand reflections were stressing each line, each curve of her body, every movement of her sculpted muscles revealing a new detail, a new secret, a new wonder, in a never-ceasing display of beauty."

    "She had gathered her hair in a strict bun, but that only managed to stress out more her face, her eyes, her nose, her lips, making her cuter than ever. Enthralled, I was unable to look at anything else for the entire duration of the race, from the moment she entered the field to the last second before she retreated in the temple, out of sight."

    "Her expression when she covered the final meters, her carmine face transfigured from the intense action, her forehead constellating with drops of sweat changed into pearls of light, her determined cinnamon eyes looking far beyond the final line, her throat pulsating at the same rhythm as the world moves..."

    "From that image alone, I can hear the frantic beating of her heart, feel the tickling of the lock of hair having escaped the band, taste the shortness of her warmth breath. An instant of perfection worth a poem, an ode, an Odysseus."

    #Small sound effect?

    "Antiope drops a cup before me and starts pouring wine into it, ending my short, probably no longer than a couple of real life seconds, but intense daydreaming."

    antiope "Drink something, you're sweating. Can't blame you, it's quite hot there."

    "I observe the liquid with a suspicious eye. It is watered down, but not that much, and must still be pretty potent, in good or bad."

    menu:
        "Accept":
            jump drunk
        "Decline":
            jump quirk

label drunk:
    "I take a sip. As suspected, the wine is quite pure, but good. I take my time to finish my cup while Antiope devours what looks like a meat pie."

    "The alcohol shouldn't have had the time to kick in so quickly, but I still feel a little bolder after the last drop. I put back the empty recipient on the table with more energy that I planned to, and the clap sound attracts Antiope's attention. She points out the bottle, in an obvious silent question."

    menu:
        "Another one":
            jump drunkard
        "Stop there":
            jump quirk

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

label quirk:
    antiope "Your loss."

    "From one hand, Antiope refills her own cup and gulps it straight away. From the other, she continues eating."

    "The conversation somehow launched, I try to guide it to the subject I want to address."

    ambrosia "Do you remember our first days together? We were going to Delphi by the land road, a trip of a few weeks through scarcely populated regions."

    "Antiope shrugs and answers casually."

    antiope "Of course I remember. A damn eventful trip. We even nearly got attacked by bandits once. If we hadn't spot their lookout and made a detour, things would have turned ugly."

    "She displays a crooked smile at the evocation of missed violence."

    ambrosia "Do you remember what we discussed during these long days and nights?"

    "Antiope thinks for a few seconds, gathering her memories."

    antiope "Actually... I don't. Is there something I've forgotten? Something you told me... or that I told you?"

    "She suddenly raises up her defenses, searching for a trap. I reassure her."

    ambrosia "Far from it. Actually, it's normal you don't remember... Because there is nothing worth remembering. We pretty much didn't talk to each other back then. Sure, we did exchange civilities and factual data about our environment and planning... But that's all. No actual conversation."

    antiope "Ah, yes... I wasn't really talkative back then."

    ambrosia "{i}Withdrawn{/i} would be a more accurate word. But slowly, you began to speak more openly. Can you explain why?"

    antiope "I never really thought about this. I guess it's happened naturally. At first, we were pretty much strangers traveling together, and I was more wary than friendly. I'm not the kind to fake amicability in such situations. It's only with time passing on that things got better."

    ambrosia "How?"

    antiope "How?"

    "She seems completely lost."

    ambrosia "How did they get better?"

    antiope "I guess... I leaned to trust you, began to relax more when being with you and... Damn, Ambrosia, you're far better are putting this feelings' stuff into words than me."

    "She pours herself a new cut and takes a sip before continuing."

    antiope "You're trying to make me say something or to have a point through rhetoric. I honestly find that quite boring, and even a little unfair. If there is something you want to say, just say it."

    "I mentally swear. So far from subtlety."

    ambrosia "Fine. Can we discuss this somewhere else? This place is a little too crowded and noisy."

    "She looks down on the feast she prepared for herself, then sights exaggeratedly."

    antiope "Fine, let's do it."

    "She stands up, and I follow. Together, her pouting, me trying to keep my heartbeat in check, we go away from the small and hot room."

    jump misconception

