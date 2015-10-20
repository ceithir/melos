image poem = ParameterizedText(text_align=0.5)

label intro:
    scene bg poetry:
        size (1280, 720) crop (0, 0, 1280, 720)
    play music "music/Frozen_Silence_-_Harp.mp3" fadein 5.0

    show poem "Ποικιλόθρον᾽ ἀθάνατ᾽ ᾽Αφρόδιτα,\nπαῖ Δίος, δολόπλοκε, λίσσομαί σε\nμή μ᾽ ἄσαισι μήτ᾽ ὀνίαισι δάμνα,\nπότνια, θῦμον.\n\n{i}On the throne of many hues, Immortal Aphrodite,\nchild of Zeus, weaving wiles--I beg you\nnot to subdue my spirit, Queen,\nwith pain or sorrow{/i}" at truecenter with dissolve

    window show dissolve

    "I remember that morning on the road.{w}\n\nI had finally managed to have her talk a little about her past. For a second, for a few words, she opened the door of her heart to me, and I felt like I had unlocked the path to Elysium."

    hide poem with dissolve

    show poem "ἀλλὰ τυίδ᾽ ἔλθ᾽, αἴποτα κἀτέρωτα\nτᾶς ἔμας αὔδως ἀίοισα πήλοι\nἔκλυες, πάτρος δὲ δόμον λίποισα\nχρύσιον ἦλθες\n\n{i}but come--if ever before\nhaving heard my voice from far away\nyou listened, and leaving your father's\ngolden home you came{/i}" at truecenter with dissolve

    "I remember that afternoon in the pond.{w}\n\nWe bathed together, not for the first time nor the last. But from that moment onwards, I was suddenly well aware of our common nudity, of our physical closeness."

    hide poem with dissolve

    show poem "ἄρμ᾽ ὐποσδεύξαια· κάλοι δέ σ᾽ ἆγον\nὤκεες στροῦθοι περὶ γᾶς μελαίνας\nπύκνα δινεῦντες πτέρ᾽ ἀπ᾽ ὠράν᾽ αἴθε-\nρος διὰ μέσσω,\n\n{i}in your chariot yoked with swift, lovely\nsparrows bringing you over the dark earth\nthick-feathered wings swirling down\nfrom the sky through mid-air{/i}" at truecenter with dissolve

    "I remember that evening in a tavern overflowing with people.{w}\n\nOur table was crowd, but that did not bother her. Actually, she was smiling, joking, {i}flirting{/i} with the man next seat. I kept my best polite face, but deep inside my chest the infernal fire of jealousy and the chilling wind of despair were battling each other."

    hide poem with dissolve

    show poem "αἶψα δ᾽ ἐξίκοντο· σὺ δ᾽, ὦ μάκαιρα\nμειδιάσαισ᾽ ἀθάνατῳ προσώπῳ,\nἤρε᾽ ὄττι δηὖτε πέπονθα κὤττι\nδηὖτε κάλημι\n\n{i}arriving quickly--you, Blessed One,\nwith a smile on your unaging face\nasking again what have I suffered\nand why am I calling again{/i}" at truecenter with dissolve

    "I remember that night in a particularly desolate region.{w}\n\nWe had set up camp in a small grove. It was summer, it was hot, so we decide to sleep under the stars. She indeed did sleep. As for myself, I spent the entire night contemplating her, watching the slow up-and-down of her bust as she quietly breathes."

    hide poem with dissolve

    show poem "κὤττι μοι μάλιστα θέλω γένεσθαι\nμαινόλᾳ θύμῳ· \"τίνα δηὖτε †πείθω\nἄψ σ᾽ ἄγην† ἐς σὰν φιλότατα; τίς τ᾽, ὦ\nΨάπφ᾽, ἀδίκηει;\n\n{i}and in my wild heart what did I most wish\nto happen to me: \"Again whom must I persuade\nback into the harness of your love?\nSappho, who wrongs you?{/i}" at truecenter with dissolve

    "I remember our first encounter.{w}\n\nI knew nothing of her except of her skills with the spear and the snare. She was certainly a fugitive on the run from the authorities, a potential thief, bandit, murderer. Yet I still entrusted my safety to her. Out of necessity I tried to convince myself then. But perhaps, already, unconsciously, under the whispers of some malicious goddess."

    hide poem with dissolve

    show poem "καὶ γάρ αἰ φεύγει, ταχέως διώξει,\nαἰ δὲ δῶρα μὴ δέκετ᾽, ἀλλὰ δώσει,\nαἰ δὲ μὴ φίλει, ταχέως φιλήσει,\nκωὐκ ἐθέλοισα.\"\n\n{i}For if she flees, soon she'll pursue,\nshe doesn't accept gifts, but she'll give,\nif not now loving, soon she'll love\neven against her will.\"{/i}" at truecenter with dissolve

    "I remember our last discussion.{w}\n\nWe were waiting outside the stadium, before dawn, before this long day of festivities starts. More daring than usual, I had not so subtly directed the conversation on the various interpretations of my repertoire's works, and was watching her closely, attentive to any sign, any reaction which could have given me hope. I saw none."

    hide poem with dissolve

    show poem "ἔλθε μοι καὶ νῦν, χαλέπαν δὲ λῦσον\nἐκ μερίμναν, ὄσσα δέ μοι τέλεσσαι\nθῦμος ἰμέρρει, τέλεσον· σὐ δ᾽ αὔτα\nσύμμαχος ἔσσο.\n\nCome to me now again, release me from\nthis pain, everything my spirit longs\nto have fulfilled, fulfill, and you\nbe my ally" at truecenter with dissolve

    "I remember these moments, and many others, small and big, casual and special, every precious little brick of the time I spent with her.{w}\n\nI remember, and I am happy.{w}\n\nI remember, and I am sad."

    hide poem with dissolve

    show bg poetry:
        linear 3.0 crop (0, 717, 1280, 720)

    stop music fadeout 5.0

    # Add sound effect. Applauses _during_ the fadeout + Fade in another music shortly after

    "A final strum, and the last note escapes the lyre, rises into the air, rings through the night. In its mourning, it echoes the end of the song, and is answered with applauses and cheers."

    "About twenty persons noisily show their appreciation of this recital of Sappho's classic. I join them as well, if only to be polite. Secretly, I'm unconvinced, and I'm not alone. When I played the exact same song on the same rostrum for the same audience about an hour ago, the public response was far more enthusiast. Even if the night has only grown darker and colder since, it's obvious this show is subpar."

    "Yet, despite the absence of any real passion in the voice, the technical mistakes when handling the lyre, and even a few distorted lines, I can't help but be moved by this music."

    "The {i}Hymn to Aphrodite{/i} is a powerful piece, one people expect and enjoy, one I have played many times in the past, and that I will probably play many times in the future too."

    "But for several months now, I have been unable to hum its melody without picturing a specific face, without imagining a certain pair of beautiful eyes looking at me while I'm singing, without dreaming about one unique person listening to the words between the lines and understanding the special meaning this song has for me."

    "And this is but the most harmless of my recent quirks. I have turned obsessive, possessive. I sleep little and badly, cannot bear the shortest of separations, constantly observing her and overinterpreting each and every of her words and actions. I do my best to hide it, and as a professional artist trained to save face and smile in all circumstances, I'm pretty sure I have managed to keep the mask of sanity and happiness on until now."

    "But deep inside, I'm crumbling, I'm on the verge of breaking, at the gates of madness. The flames are in me, they want to go out, but I keep them locked inside, and so they consume my soul. More than the passion itself, it's the silence which is killing me. I haven't told anyone, nor her, nor any other person, to be sure this would not reach her ears somehow. In fear of the consequences of such reveal."

    "I have observed her for days and nights. Yet, I never found a single hint that she may feel about me the same way that I feel about her. But I have grasped enough to understand she was born in a culture of power and steel which does not value highly romance, a world where reproduction takes precedence over proper love. And that she still lives by the spirit of her education if not by its customs."

    "And I'm afraid. Very afraid. Of what will happen when she will discover my passion, my desires."

    "Afraid of bewilderment.{w} Afraid of rejection.{w} Afraid of fear.{w} Afraid of anger.{w}\n\nAfraid this will break our special relationship.{w}\n\nAfraid that by wanting too much of her, I will lose her whole."

    play music "music/Frozen_Silence_-_Harp.mp3" fadein 5.0

    "As a background noise for my worries, the man on the scene starts playing. I recognize a composition from Alcaeus. A supposedly appropriate answer to the last piece, as he was Sappho's senior and rival. But a poor idea in the end, as the stanzas I hear simply cannot compare to the majesty of Sappho's texts. She was the uncontested Tenth Muse, and the artistic world still mourns her death a couple of decades ago."

    "The nagging melody nonetheless calms me down a little. I review my options. This afternoon, I took part in one of the main events of the festival, in the city theater, under the gazes of hundreds of people. A grand contest of poetry in whom many artists tried their luck, including the one distracting us right now."

    "Triumphing in such a competition is usually a life's goal for a singer, but this was not my main concern this year. However, I did plan my day with an extreme precision. As soon as my early and obligatory performance ended, I retreated back to the shadows, discreetly escaped the theater to hide myself in the nearby woods."

    "Then I sat, on the ground of a sunny clearing. Alone, while the whole city was directly or indirectly focused on the festival, from the shouting people on the theater's tiers to the humblest food vendor. To think. Think far away from the constant noise and movement of the ordinary life. Think without the weight of exhaustion and the terrors of the night overtaking me."

    "And after a few hours, when I knew I couldn't hide or flee anymore, I made my decision. It's this night or never. The moment couldn't be more perfect. Today, the city is celebrating Aphrodite. Today, we both shone in our own specialty, prove ourselves to the world, reminded it we exist by our own rights. This night, right now, her mood should be at its best, on the edge of ecstasy."

    "If I don't talk to her this night, I know I will never have enough will to do it again. That my mouth will stay shut and my heart closed. So... I just need to stand up, walk away from this quiet corner of the property where a few artists and enthusiasts gathered for some impromptu rehearsals, find her in the crowd, take her apart, and open my heart to her."

    "As simple as that."

    menu:
        "Wait":
            jump coward
        "Go":
            jump intro2

label intro2:
    "I raise my head. Before me, the artist is almost done, and soon a new volunteer will take his place. It could even be me if I wanted to. I look at my own lyre, waiting impatiently in its bag at my side."

    "On my left, within arm's reach, I notice a few appetizers and drinks. I pick an olive, make it roll upon my palm."

    "On my right, a group of people are having a hearty discussion about the last musical trends. Classicists versus moderns, as usual, but interesting nonetheless."

    menu:
        "Stay":
            jump coward
        "Go":
            jump intro3

label intro3:
    "I force myself to look at the nearby exit. Just a few steps away. Could as well be beyond the Pillars of Heracles."

    "I'm pitifully delaying, trying to find something to do, anything, to push back the moment. Even the time I'm currently using to think about this is a form of temporizing."

    "I lash myself mentally. It would be easy to postpone forever, like a bad poet always rescheduling to tomorrow the writing of their masterpiece, and finally passing down with a blank page pressed against their chest.\n\nEasy and infinitely regretful."

    "I gather my will.\n\nI clench my teeth.\n\nI rise."

    "My knees are shaking like a set of knucklebones. I'm shivering more than an old lady. Nonetheless, I stumble on the short distance separating me from the main building. With each step, my footing is more secure, my pace more stable. Not that I'm less afraid. But once you jumped into the water, you have no other choice than to swim or sink."

    show bg poetry as trans_poetry:
        crop (0, 717, 1280, 720)
        linear 2.0 xpos -1280
    show bg inside as trans_inside:
        xpos 1280
        linear 2.0 xpos 0
    pause 2.0

    jump antiope

