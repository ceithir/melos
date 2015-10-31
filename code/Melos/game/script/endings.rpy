init python:
    def ending(name, number):
        ending_text_string = "Ending %s: %s" % (number, name)
        ending_text = Text(ending_text_string, text_align=0.5, xalign=0.5, yalign=0.5, size=48, color="#000")

        renpy.music.stop(channel='sound')
        renpy.music.stop(channel='music', fadeout=10)
        _window_hide()
        renpy.show("ending_background", what=Solid("#fff"))
        renpy.show("ending_text", what=ending_text)
        renpy.with_statement(fade)
        renpy.pause()
        renpy.jump('_renpy_return')

label coward:
    scene black with dissolve
    stop music

    "I feel bad, nauseous, stiff. My head is heavy, aching, my mouth furred, my throat hurting. I sense a hand on my shoulder and two fingers tapping repeatedly on my forehead. Reluctantly, I open my eyes, painfully, and the darkness recesses."

    "I am lying in an unknown seat, folded in an uncomfortable position, one arm as a pillow. My hair and my dress are competing with each other for the position of most messy, but that's probably only because I cannot see my face. But I can see {i}her{/i}."

    show antiope with fade

    "She seems tired, but yet is ready for departure, fully clothed and equipped. Her eyes are filled with concern as she hands me a flask of water. I accept mechanically, drink a little. The fresh liquid dissipates part of my forgetful stupor, unearthing the terrible reality."

    if despair:
        "I remember that after our one-sided discussion, we went back to the party. And we may have drunk. A lot. Especially me. I knocked myself out with alcohol. Not a reasonable solution, but it helped. Antiope drank a lot too, but our constitutions are not even comparable."
    else:
        "I remember delaying, postponing, pushing back, assuring myself I would go after that last song, that last cup, my will to move actually decreasing as time passed on and alcohol filled up my body. I don't know which of my mind or my organism forfeited first, but at some point my memories cease. I suppose – hope – I have drunk myself to sleep."

    "And now, I stand, feeble on my feet, and excuse myself pitifully. I ask her to wait for me while I fetch my belongings and I run away."

    play sound "sound/134991__zombiechaser3__running-sounds.ogg"

    hide antiope with moveoutright

    pause 0.5

    show antiope with moveinright

    stop sound fadeout 1.0

    "A few minutes later, after a lighting flash toilette, I'm back and ready to go. I do a bad joke about not knowing my own limits and them we move on. In the end, the cold facts are that we have a long trip ahead of us, and we already are several hours behind our schedule."

    stop sound

    scene bg sky with dissolve
    play music "music/Celestial_Aeon_Project_-_Harp_Music.ogg" fadein 1.0

    "As the walk goes on under the light on the sun, she starts shining, the physical effort purifying her body, her pace sure and quick, her cheeks pinkish from the extra ardor put into the back-and-forth sprints she regularly does while scouting ahead. She quickly is as radiant as ever, if not more."

    "Me? I am slow, gloomy and depressed. Not only do I not emit any light, but I'm unable to simply reflect it like I usually do. At the moment, I cannot play properly my own role in the play which is my life, cannot force myself to fit the mood, to drape my insignificance in the brilliance of others to make it looks like I glow a little."

    "I am in broad daylight, yet I am what I really am in the dark, once stripped of the clouds of facilitating lies I usually wear as a second skin."

    "I'm myself. A coward. An actor afraid of herself, afraid of letting her audience look beyond the mask. Able to speak the most complicated, lyrical, convoluted, impressive sentences as long as they're perfectly useless, but suddenly mute as soon as the truth may come out of my lips. A highly educated, perfectly trained master of form without substance."

    "And that's exactly why I need to rebuild the illusion immediately, before anyone realizes how fake it is and could confront me on what I really am. So, I take a deep breath, readjust my posture, reorder my hair, compose myself a \"happy but tired\" smile and a couple of seconds later, the veil is back on."

    "I can already fool the world outside, and I'm sure I will soon be able to fool myself into thinking this was just a missed opportunity, that another will arise and that this time I will find the necessary courage."

    if despair:
        "I assure myself I will tell her my true feelings before she leaves, most certainly forever. Even if it is pointless, because it must be done."

    "A white lie to keep myself sane."

    "Still a lie."

    $ ending("Coward", 6)

    return

label oblivion:
    scene black with dissolve
    stop music

    "I feel groggy. I suppose I have slept. At least, I'm currently uncomfortably seated sit in an armchair with no memory of a couple of hours. But I don't feel rested, not even close. My head hurts. Too much... something."

    "I stand back up without haste. My mind is having difficulties putting back together what happened that night. So many things and yet so little."

    "Real life strikes in, and I realize I'm late. The sun looks like it has been up for some hours now, and that means I should already be ready for departure. So I rush to pick back my belongings and make myself presentable. I do so without thinking, still half asleep. Perhaps because I don't want to really wake up, to face reality."

    scene bg sky with fade
    play music "music/Celestial_Aeon_Project_-_Harp_Music.ogg" fadein 1.0

    "Then, with a lasting headache, I walk to the place where Antiope and me agreed to meet once the party will be over. My anxiety keeps growing as I come closer to the location."

    show antiope with dissolve

    "When I see that she is indeed there, I'm relieved, but only partly. Because I'm still afraid of how the events of this night impacted her. Of how they changed our relationship. Of what will happen next."

    "But her reaction is worst that anything I could imagine. She simply acts as she always does. She is not a single bit different from how she was two days prior. She is the same old Antiope in good and bad."

    "Did the alcohol wipe out her memories?  Was everything that happened last night so unimportant to her? Or is she just pretending? I can't say. And I don't dare to dig further for the truth. She is there. We're talking like friends, still sharing the same intimacy. I'm not brave enough to risk breaking this special bond once again."

    hide antiope with dissolve

    "So I go on with the flow. I imbue myself with my own role, I put on my mask of Ambrosia the happy musician, the good friend, the naive poet. I remodel my face into a bright smile, I chitchat cheerfully, I dance around her like I was excited by the rest of our tour. Antiope is grumpy but cool, and we go on like we always do."

    "Pretending soon turns to be quite tiring, to only increase my inner depression, but it's a game I cannot stop. I am prisoner of my own cowardice, of my own character. If I put down my mask, Antiope may remove her own in response, and then anything could happen. A universe of unpredictable possibilities I'm not ready to face up right now."

    "So even if the inner side of the mask is a forest of red hot barbed spikes inflicting me the greatest of pain, I must wear it. Until courage or madness releases me, whichever comes first."

    "And I already know which virtue I'm better at."

    $ ending("Oblivion", 5)

    return

label apology:
    scene bg black with fade

    antiope "I'm sorry."

    show bg inside with fade
    show antiope sad with fade

    play music "music/Frozen_Silence_-_Harp.ogg" fadein 1.0

    "I don't know how she found me. I must have dozed off at some point, while she kept searching. We're back in the banquet room, almost empty as dawn is upon us. The only people still around are those who fell asleep here and there, defeated by their many excesses. I could scream with all my lunges that they will not wake up. I'm still alone in the end."

    "Antiope looks extremely pitiful. Ravaged. Vanned. There is no trace of her usual confidence on the desperate face looking at me."

    antiope "I'm really, really sorry. I didn't want to... I'm sorry."

    "I don't answer. I just look at her with cold eyes."

    antiope "I'm sorry. I didn't want to hurt you. I know I did, both physically and emotionally. I was exhausted and drunk, but that's no excuse. I know my own weaknesses first and foremost, and yet I still let them control my actions."

    antiope "I'm sorry. It's easy to say, but I don't know what else to say."

    menu:
        "Answer":
            jump talk
        "Silence":
            jump broken

label broken:
    "I don't answer. I stand up, and I leave her to her pitiful apologies. My wrist is still nagging me, even if the pain is more psychological than physical. I walk away, slowly, without looking back, simply desiring to be alone."

    jump bramble

label bramble:
    stop music fadeout 1.0
    scene bg sky with fade

    play music "music/Celestial_Aeon_Project_-_Harp_Music.ogg" fadein 1.0

    "The sun is rising. I can count the passing of minutes simply from the light slowly filling up the room. I have been walking non-stop since my last one-sided talk with Antiope, going in and out, and my legs are hurting. I didn't exactly dress myself for a hike, and the cries of my body are more audible now that my rage has cooled down a little."

    scene bg garden with fade

    "I once again enter the garden, look into the pond. I don't recognize the crazed stranger looking back at me, the dark rings around her eyes, the rivers dug by tears on her cheeks, the hair more mixed up than the ones of Medusa."

    "But this is nothing. This, I can easily fix with a brush and some makeup. My main problem is my future from now on."

    "I'm afraid of Antiope. Terrified. I knew she was violent. I always knew. I've seen her enter fights more than once, and guessed she did so many more times when I wasn't looking. The bruises she had a hard time hiding at dawn couldn't lie."

    "But, I always tried to convince myself it was a part of her bigger than life character. I dismissed the idea that her violence could have other targets than random thugs or wild beasts."

    "She did not inflict any permanent damage to me. Far from it. In a day or two, my wrist will be as good as new. But I saw the fire in her eyes. For a moment, she was about to pummel me senselessly. Without any good reason. Just because I was there."

    "Even worse: I still love her. Thinking about her still kicks in my passions, now alongside my fears. My dreams and my nightmares are merging into a confusing oneiric story, where she plays both the heroine and the villain."

    "I'm lost. I want to see her again, to talk to her, to share her life. But I don't want to confront her madness ever again."

    "And the worst of the worst? Right now, I {i}need{/i} her. I have a job to do, a tight schedule to respect, and I haven't got the time to find another companion for my tour, not enough money to miss this festivals' season."

    "I know I {i}need{/i} to go back to her, fix that up one way or the other, and continue with my ordinary live. I know I {i}will{/i}."

    "In the water, the living incarnation of despair looks at me, and I answer her with a maddened smile."

    $ ending("Despair", 4)

    return

label talk:
    "My own voice is grave, icy, like coming from a deep cavern. I don't do this on purpose, it's just a consequence of my extreme fatigue."

    show ambrosia
    ambrosia angry "Sorry for what?"

    show antiope bliss with dissolve

    "Despite my tone, Antiope looks ecstatic that I'm simply talking to her."

    antiope "For my behavior. For being an idiot in general. For having attacked you in all possible manners when you were just trying to prevent me from hurting myself. No, that's not it. For having attacked you, regardless of the circumstances."

    show antiope with dissolve

    "She takes a deep breath. Antiope has talked more this night than she usually did in days. But contrary to her precedent drunken outburst, she sounds more serene, more honest, less theatrical."

    antiope "It's hard to put into words, but I need to try even so. I'm no nice girl. Violence, furry, death and destruction run in my blood. That is very obvious."

    "She flexes her muscles, points out the marks on her body demonstrating her daily usage of weapons."

    antiope "But that's only the beginning of it. Not only am I a naked blade, but I always point it at the wrong people. I'm a living pile of stupid reflexes and biases. I don't trust anyone, I only consider the part which could endanger me in other people's actions, ignoring what good it could do to me, and without caring for the consequences for themselves."

    antiope "Do you know that the first nights we passed together, I barely got any sleep because I didn't completely rule out you wouldn't rob me as soon as I close my eyes? Despite everything and anything proving me you were no bandit? It took weeks before I learned to trust you enough to get a full night of sleep."

    "I try to appear unfazed, but this piece of information is indeed new to me. At that time, I remember Antiope's not sleeping a lot, but we were passing through dangerous regions, and I ruled out these memories as simple precautions against the outside danger. I never thought she was afraid of me."

    antiope "I'm fighting it every day that... {i}paranoia{/i}. I don't know if it's the proper word. Sort of fear of everything. Usually, I manage to keep these urges to flee or fight the whole world in check, or at least to hide myself when they're at their worst. But when I'm stressed, exhausted, drunk, the monster shows its face again."

    "She pauses."

    antiope "I understand this is no excuse, only explanation. I know myself for what I really am. I know you are one of the best friends I have ever had, and that you only wanted to help me in my fight with my inner darkness. And yet, I've unleashed it against you."

    antiope "Please believe me, I'm really sorry. You're the last person I want to hurt and... I don't want to lose you. Even if I would understand if you asked me to leave. You gave me a lot, and I've thanked you with nothing but disrespect and pain."

    "I sigh. Lengthily. Some part of me is still angry at her, but I simply cannot resist her when she is looking at me like that. With a wave of the hand, I invite her to sit by my side, which she promptly does."

    ambrosia default "Why didn't we have this conversation earlier?"

    antiope "I don't really know. I went overboard a few times already when you were there, even if never as hardly as today... Most of the time, I managed to escape this talk by cutting short the dialog and fleeing... And the other times..."

    ambrosia "Yes. I know. I'm the one who fled."

    "I look at her right in the eyes, seeing my own face reflected in her pupils. Yes, there are a few times when I just kept silent on Antiope's sick habits. Today the first time she ever hurt me, but on several mornings, her face or fists were bearing the marks of fights she got herself into. And I never dared to ask."

    "I will not say idiot things like \"I'm as much a culprit as you\". Because that's not true. But the crime of Antiope, her refusal to open up her heart before the darkness in it frees itself and almost destroys her own world... I can relate to it. It is nothing more than a distorted, flawed, extreme reflection of my own weakness."

    "I readjust my position, closing the distance between me and the broken warrior. Our faces are only separated by the width of a hand when I speak again."

    ambrosia "Antiope. You are a big dumb idiot. But you're not the only one."

    ambrosia "The moment is not perfect, but it will never be. I cannot ask you to be honest with me when I'm not telling you the whole truth myself."

    ambrosia "Antiope, despite your many flaws, despite your early and lately behavior, I know I'm about to forgive you. I somehow know that you could do much worse, and that even if that would hurt me terribly, I would still forgive you."

    ambrosia smile "And I would do so Antiope, because I love you. I adore you. I would go to the underworld to negotiate with Hades for you."

    show antiope bliss with dissolve

    "Antiope's reaction is refreshingly simple. A flash of surprise succeeded by an extraordinary deluge of embarrassment. She turns almost comically pink from all the blood rising up to her head and mumbles some incomprehensible words."

    "I smile warmly. I know she couldn't have misinterpreted my words. The tone of my voice was not friendly or motherly. It was utterly passionate."

    "I feel calm. I have done it. The arrow has been shot, and there is nothing I can do to change its course now. Antiope mumbles, unable to pronounce any intelligible word. From her struggling alone, I can already guess what she wants to say, but that she doesn't know how to formulate it clearly, without hurting me more than she already did this night."

    ambrosia "Take your time. No need to hurry."

    antiope "I... Thanks. I understand this was not an easy thing to say, particularly in our situation. But... Ambrosia... You're a extraordinary friend, but... I have no romantic interest in you."

    "Silence."

    show antiope sad with dissolve

    antiope "I'm sorry."

    "I try to keep my voice cool and articulate."

    ambrosia default "I guessed so. Thank you for your frankness."

    "More awkward silence sets in."

    ambrosia "If I may ask... Could you give me some time alone?"

    "As a reaction to my request, I can see fear in Antiope's eyes. That I would do something stupid certainly."

    antiope "Are you sure?"

    ambrosia "Certain. I will see you tomorrow, don't worry."

    "She hesitates. Looks at me. I give her an encouraging nod."

    antiope "To tomorrow. Promise?"

    ambrosia "Promise."

    hide antiope with Dissolve(1.0)

    "She utters some last civilities, and finally departs, not without looking back a few times, worry painted on her face. I disarm her with a bright smile each time."

    "Only when I'm certain she is far from here do I allow myself to break up into tears."

    play music "music/JAyFS_-_Quiet_village.ogg" fadein 2.0
    scene sky with fade

    "I'm late. By at least one hour. I already woke up late, but it's the time I spent cleaning my face which really put me in. The minutes flew by while I was erasing all traces of sadness, tiredness, despair from my face with a professional care, water, soap and an appropriate use of cosmetics. But now I look fresh and ready again."

    show antiope with fade

    "Antiope is at the meeting point, and by the look of her own face, she has been worryingly waiting for quite a bit now. She did no effort to hide her own exhaustiveness, but her superb constitution still allows her to appear as strong as ever. I greet her happily and she welcomes me with open arms and a touch of awkwardness."

    hide antiope with dissolve

    "And then we depart. As it was planned. Our agenda for the season is quite full, and we have no time to rest. Soon, this place of memories we will never forget is behind us. We may come back to the same location next year, but then it will not be the same. It will never be the same."

    "As we walk through the city, eying the people cleaning the excesses of yesterday, the distance between us becomes even more obvious."

    "Or perhaps, on the contrary it's the new proximity which is strange. Objectively, before, we never talked that much. I idealized her from far, and she never was really sociable. Now, we're at least both conscious of the other's existence as a real person."

    "It's awkward. I know I will probably never awake any passion in Antiope, and that continuing to live by her side will certainly break my heart on a regular basis. I'm sad. New tears are just waiting for an excuse to roll out of my eyes. Yet I feel lighter. Like I've been freed of iron chains I didn't even know existed before."

    "And if my relationship with my amazonian beauty of friend didn't evolve the way I would have loved it to, I think it is now at least {i}healthier{/i} that it was previously."

    "Soon, we've passed by the walls of the city and we're entering the main road, about to start a long trip in the countryside and the wild. Above us, the sun is high and bright. It shines with all its might, ignorant of the terrors of the night, upon the path to our future."

    "And with a single step on the uncobbled path, we start the first day of the rest of our lives."

    $ ending("Truth", 1)

    return

label kiss:
    "I lean a little more."

    show antiope bliss:
        linear 1.0 zoom 4.0 ypos -100
    pause 1.0

    "My lips encounter hers. A small smack from two closed mouths bumping into each other."

    "For a full second, we stay like this."

    stop music fadeout 1.0

    "Then, Antiope's reflexes, having been slowed down by the incredible amount of alcohol she took in, finally takes charge."

    play sound "sound/144015__satanicupsman__bone-flesh-crush-punch.ogg"
    hide antiope with fade
    show bg garden with hpunch

    stop sound
    show bg black with vpunch

    "Her forehead hits my own in a violent headbutt. She returns to her feet in a single bound, shoving me aside. Unable to find back my balance, I fall on my behind and the ground is not gentle with me. But this is nothing compared to Antiope's fury."

    show antiope angry with dissolve

    "She is towering me, her fists convulsively opening and closing, her mouth sputtering, dribbling, her bloodshot eyes burning with rage."

    "I try to mumble an explanation but she cuts me short."

    antiope "I thought I could trust you. But you were just a smugger snake, weren't you?"

    "She gets closer from my defenseless body, and positions herself to kick me."

    hide antiope with fade

    "I instantly put my arms before my face in a self-preservation instinct."

    "But the assault never comes. I hear her stepping backwards, spitting, then talking to me. For the last time."

    antiope "Never approaches me again if you value your life."

    "And walking so quickly this could as well be called running, she goes away."

    stop sound
    play music "music/Frozen_Silence_-_Harp.ogg" fadein 1.0

    "The sound of her departure has long died, but I still cannot stand up. Perhaps because I only want to lie down and cry right now, even on the cold hard ground. Everything went so quickly and so badly. Why did I do that? That was beyond idiotic, and made me lose everything. I have but myself to blame for my infinite stupidity."

    "My consciousness is fighting some primal creature deep inside not to tear down my hair or scratch my skin out of hate of myself. I'm not even sure the human part is winning. Perhaps I'm simply so dull at this moment I'm unable to take any action, even one that's most ill-advised."

    "On the icy floor I lie, in the darkness I belong, alone I am."

    $ ending("Kiss", 2)

label fight:
    "I refuse to let it end like that. I gather all my courage and I rise."

    ambrosia worried "Antiope, you... You're completely missing the point there."

    "She cocks an eyebrow. She is not used to me contradict her or simply raising my voice."

    ambrosia "I did want to speak to you about our future..."

    "I step back. Draw a big breath. And go."

    ambrosia default "But on a more personal point of view."

    "Antiope looks confused."

    ambrosia "It's not about our... careers. It's about us. As people. As we are now. As we may be in the future."

    "Too far in to back down, but still cannot help but postpone the ineluctable. Antiope is not helping, constantly fidgeting on her seat that she is. I try to focus. I kneel to look at her right into the eyes."

    ambrosia "What I'm trying to tell you is the exact opposite of what you guessed. I don't want you to leave. I want you to stay. Until the cruelty of the gods take us apart."

    stop music fadeout 0.5

    "I need a last break. A last breath. And here rolls the thunder."

    ambrosia "Antiope, I love you."

    "Antiope's reaction is priceless. She just stares at me, completely lost. If I was in the mood for a good laugh, I could giggle almost endlessly. But I'm not."

    antiope "No."

    play music "music/Celestial_Aeon_Project_-_Harp_Music.ogg" fadein 1.0

    "Her answer is disturbing. She said it calmly, without hate, actually with a bit of... affection?"

    antiope "No. You don't love me. You love the part of me I've let you see. And believe me, if you really knew me, you wouldn't try to get closer."

    antiope "You would cower in fear."

    "She stands up."

    antiope "I think I should move forward my agenda. The sooner we part ways, the better for the both of us."

    "I'm totally astonished. I try to speak, but Antiope seals my lips with one finger."

    antiope "You're the best friend I've ever had Ambrosia. And that's why I must go before screwing everything up."

    "And on these words, she leaves. She simply walks away, abandoning me there. I'm unable to pursue her. I... don't understand anything anymore."

    scene bg sky with fade

    "There is no word to describe how relieved I am to find Antiope at our rendez-vous point as planned. After searching for her all night long, I had convinced myself she had vanished for good, fleeing by the main road under the cover of darkness. To see her in the flesh again is the best gift the new day could offer me."

    "However, I'm quickly disenchanted. Antiope is physically there, and she does her job, but she does just that. She is cold, distant, and at lunch, she would evoke for the first time and not the last her accelerated planning."

    "In the following weeks, I will try to understand, try to make her talk about her sudden change in behavior. But from that point onwards, she will simply be more secret, more withdrawn. More absent also, sometimes disappearing for full days while we're in town. Usually coming back with bruises she refuses to talk about."

    "My emotions are a complex mix. There is love but also..."

    "Also, I'm afraid."

    "The harder she tries to hide, the more pressure she puts on herself. Her temper has shortened radically, the slightest of vexations releases her rage. She is a hornet's net on two legs, and could break at any moment, unleashing the fury of nature over whoever will be there at that wrong instant."

    "Namely me."

    "And so, as the day of our final separation that she herself decided is closing in, if my heart rejects it, wants for time to stand still until I manage to fix up our relationship, my brain is starting to long for it. That it may come before the executioner's sword falls on my neck."

    $ ending("Secret", 3)

    return

