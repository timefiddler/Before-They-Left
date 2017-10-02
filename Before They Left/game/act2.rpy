label Act2:
    j "If 90\% of the world got submerged into water, what kind of mutation would you want in order to survive?"

    ch "What?" #cheyenne looks very confused, furrowed brows

    j "Like, with global warming and the polar ice caps melting and shit, if you were to get a weird super power or evolutionary trait to survive this new {i}waterworld{/i}, what kind of thing would you want?"

    k "Is this like post-apocalyptic with people barely surviving or has civilization somehow adapted?"

    j "Umm..."
    j "Let's say two-thousand years have passed since the flood and any surviving civilization has blossomed into its own unique thing, but people have genetically diversified."
    j "'Cuz like you know how humans are apparently 98\% the same as each other or something and how its weird compared to other animal species -- humans have somehow been forced to diversify due to unknown reasons."

    e "So its post-post apocalypse."

    j "Yeah."

    ch "Okay..." #cheyenne rubbing chin

    "The group takes a moment before Sam breaks the silence."

    s "Fuck it, I'm a mermaid."
    "The others approve enthusiastically."

    j "Ahh, that's what I wanted!"

    e "I mean, nothing's stopping you." #deadpan face

    j "Yeah, but it'd be boring if we all said mermaid."

    ch "Ok, if you're a mermaid..."
    ch "What about some kind of amphibious adaption. Like, somewhere between mermaid and human, where your skin and breathing has adapted or something."

    s "Are you saying you're a frog girl?"

    ch "No and yes." #shit eating grin
    "Sam's mood lifts a bit."

    "The girls go around the table coming up with absurd details of how their mutations and evolution would work, citing various science factoids and embellishing upon any knowledge of animal biology."

    if extradepress:
        "Sam puts on her best smile as the conversation spirals, laughing."

    if Kateytravelnerve:
        "Cheyenne keeps glancing at Sam."
    else:
        "Katey takes Sam's hand under the table and rubs with her thumb comfortingly."

    menu:
        "What does Sam do?"
        "Hold herself together." if extradepress and not Kateytravelnerve:
            jump Samtrying
        "Notice Katey." if Kateytravelnerve == False:
            jump Kateycomfort
        "Look around." if Kateytravelnerve:
            "Cheyenne keeps glancing at Sam. Sam catches her eye."
            jump Cheyenneeye

#restroom path
label Cheyenneeye:
    "Cheyenne sees that Sam's noticed, and softly maintains eye-contact. Sam stares back, but is surprised by Cheyenne's expression: a look of... longing? No, that's not right. Concern? No, Sam had seen plenty of that."

    "One microexpression morphing into another; a sixth of a smile shifting into a tenth of sorrow, a twentieth of fear feeding into a fifth of hope,  constantly changing until Sam finally breaks eye contact."

    "What was that? That was more than a random stare goof. Was it, though?"
#fade back from dark cafe to normal
    "Katey declares she would be be one of the last remaining \"true\" humans... but with a surprise plot twist of being the prince of a bird kingdom who'd been kidnapped as an infant and kept in a glamour all their life."
    if extradepress == False:
        if yesdrink:
            "Sam works through her milk tea, keeping her eyes averted from any further eye contact. What was that? Did she imagine it? Sam steals a glance back up and Cheyenne catches her."

        if disappointCheyenne == False:
            s "I... need to go to the restroom."
            if yesnachos:
                k "You just went, though."
                "Sam looks at Katey for a moment, and settles back into her chair."
                jump endofday
            if yesdrink:
                "Katey and Julia stand up for Sam to get out."
                ch "I'll come with you."
                jump Cheyennebasketball
    if disappointCheyenne or extradepress:
        "Sam puts the thought out of her mind. Awkward staring doesn't actually mean anything."
        jump Samignores

label Cheyennebasketball:
    "Cheyenne follows Sam to the restroom, and the door closes behind them. It appears no one else is in the restroom."

    "Sam walks to the furthest end of the faucet counter and turns around to see Cheyennne, with a few footsteps between them."

    s "...Um...!"
    "Sam finds her breath shaking. Its unexpected. She feels nervous for some reason. Why?"

    ch "Sam, um... there's..."
    "Sam's eyes decide to intensly focuses on a wet splot on the restroom counter."

    ch "...a bit of sauce on your face."

    s "...O-oh! Thanks!"
    "Sam hurriedly looks at the mirror and washes away the mark. The mirror is huge, and she can see herself and Cheyenne standing in the restroom alone. Sam doesn't look away. Cheyenne looks at Sam's reflection."

    ch "I kind of miss us hanging out more."
    ch "Don't you miss basketball? I could talk to the coach to have you back. Wouldn't-"

    s "No, I..."
    "Sam takes a moment to form her thoughts."
    s "I... can't. Yeah, being on the team was fun, but... I..."
    "The words won't come out."

    ch "Okay."
    "Cheyenne sounds... defeated. Sam stares at the bottom edge of her reflection, while Cheyenne turns around to lean on the counter."

    menu:
        "The restroom flourescent light hums as the two stand silently."

        "Thank her.":
            s "...I...don't think I've told you \"thank you\" for coming and hanging out with me all the time. You don't have to do this if you don't want to, you know."
            jump restroomhug

        "Use the restroom.":
            s "I need to go pee..."
            jump awkwardpiss

label restroomhug:
    ch "What? Of course I want to hang out with you, and you're not about to stop me, either! I'm your friend, you don't need to say thanks!"
    "Cheyenne feigns feeling insulted, and steps closer to Sam."
    "Cheyenne's voice softens."

    ch "Sam..."

    "Sam looks up and sees in the reflection that Cheyenne is looking at her directly, so she turns to her."
    "Sam is surprised by Cheyenne's expression -- a look of both mirth and anxiety. She never knew her for anxiety."
    "Cheyenne's eyes twitch around, searching all over Sam's face. She takes a few audible breaths through her nose. Cheyenne takes Sam's limp hands into her own."

    ch "Sam... you are one of the kindest, bravest, most beautiful people I know. I care about you, ok?"
    "Cheyenne speaks to Sam in a soft, hushed tone. Sam looks down, flushed; everything she's saying sounds wrong."
    "Her, {i}kind? Brave? Beautiful?{/i} The words feel hollow. She wants to tell herself Cheyenne's being honest, but..."

    "Cheyenne brings her hands up to Sam's face, palms holding each of her cheeks. Sam could feel Cheyenne's hands trembling. Why was she trembling? Sam should be trembling."
    "Sam feels like she's outside of her own body. Not feeling, just... watching."
    "There's nothing to do but to stand there."

    "Cheyenne pulls Sam's face towards her lightly, and Sam's body complies. She leans up, and with one hand clearing away Sam's bangs, kisses her forehead."

    "..."

    "They stand there like that for a good few moments, with Cheyenne kissing her forehead a few times more. Sam's face begins to flush a little as an intense feeling of sorrow fills her."
    "An intense pain shoots its way up from a large, empty darkness. Emotions begin to sear their way through Sam. And then it stops."
    "Cheyenne pulls Sam into a tight hug, and she lets herself feel Cheyenne's grip, her touch, and let's her clenched chest relax into Cheyenne's shape."

    "..."

    "...."

    "A minute or more passes -- sense of time is unclear. Cheyenne finally lets go of Sam. Sam looks at Cheyenne, and they both share a look of relaxed intimacy."

    #Cheyenne cheery
    ch "We should go back to the others."
    "Cheyenne's chipper voice contrasts the mellow moment they had just shared."

    s "Oh, uh, yeah, ok."
    "Sam finds her voice relaxed, with the slightest hint of wanting the moment to last a bit longer."

    ch "Oh, wait...!"
    "Cheyenne stops as Sam passes by her. Sam starts to turn around but Cheyenne stops her, gripping her shoulders."

    ch "One second."
    "Sam feels Cheyenne pulling her hair back and moving it around. Sam glances towards the mirror to see what in the hell she was doing."

    "Just as she does, Cheyenne lets go and Sam sees that she had put her hair in a ponytail. A high, one, in fact. It looks... kind of really nice."
    "Sam's face feels a bit naked without her hair flanking her cheeks, but maybe this is what she needs. Some kind of... bold vulnerability. Sam turns around to Cheyenne, who's smiling quite a bit."

    ch "Yes! Much better. That's the Sam I know."

    "Cheyenne opens the door for Sam, and they return to the brightly colored walls of the milk tea cafe, joining the others at the table."

    ".:. Intimate Ending."
    jump credits

label awkwardpiss:
    ch "Oh...! Yeah, sure. Umm. I'll see you outside."
    "Cheyenne finds herself stumbling to find words."

    "Cheyenne leaves the restroom, leaving Sam with the low hum of the restroom ventilation and gurgling of pipes."

    "Sam sits in one of the stalls, hunched over with her face in her hands. {i}What am I doing{/i}, she asks herself. {i}What was that?! Why are you so bad at this?{/i}"

    "Sam sits for a minute, frustrated with herself, uses the toilet, cleans up and leaves to join the others back in the cafe."

    ".:. Awkward Ending."
    jump credits

# Confession path
label endofday:
    "Finally, it seems it's time to wrap things up and the group shuffles around the table and chairs. Sam finishes up first, and waits outside for the others."

    if crushpower:
        "Sam thinks to herself and everything she'd noticed with Cheyenne. Was she just imagining it? No... maybe?"
        "A sense of dread fills Sam... a sense of not getting another chance ever again, a sense of never seeing Cheyenne again. Everyone was going to move on with their lives after high school."

        "Katey comes out first, followed by Cheyenne and the others."

        "Sam's chest tightens. Should she? Sam's fists tighten as they walk down the block and everyone starts to split off, her anxiety off the charts. The corner for where Cheyenne would head home comes up."

        menu:
            "What does Sam do?"
            "Confess.":
                if disappointCheyenne:
                    s "Hey Cheyenne..."
                    "Her nervousness betrays her voice."
                    jump Samnerves
                else:
                    s "Hey Cheyenne, could I talk to you about something in private before you go?"
                    jump realconfess
            "Stay quiet.":
                "Sam chooses to keep her mouth shut and bids farewell like it was just another day."
                jump goodlongday

    else:
        "Sam thinks to herself about Cheyenne's eye contact... was she just being silly? Sam's unsure, but doesn't feel motivated to try and investigate more."

        "Katey comes out first, followed by the others. They walk down the block and slowly part ways until its just Sam and Katey."
        jump goodlongday

label Samnerves:
    ch "What's up?" #Cheyenne chirps.

    "Sam's nerves grind against chalk and gravel. Her body clenches all over."
    "She wants... she wants to tell Cheyenne how grateful she is of her. She wants to tell her... more. So much more. But she's such a good friend, she's such a close friend. No, this is a bad idea. Bad idea. Bad idea! Bail out!"

    s "......Um, it's, actually, nevermind. I'll see you later!" #Sam expells, her face tense.

    ch "Oh, okay. Seeya guys!"

    "Katey looks at Sam with some concern as they walk home."

    k "You alright?"
    "Sam walks for a bit in silence before answering."

    s "Yeah, I'm fine."
    "Sam does her best to mask her feelings. Failing, but still doing her best to."

    k "Okay."

    ".:. Bail Ending."
    jump credits

label realconfess:
    "Cheyenne looks surprised. So does Katey."

    k "I'll... go on ahead."

    s "Thanks, Katey."

    "Cheyenne and Sam move to another block to talk. Sam notices that Cheyenne's movement has tensed a bit and her skin tone has reddened a bit."

    ch "So what's up, Sam?"
    "Cheyenne does her best to hide the nervousness in her voice."

    s "Um...!"
    "Sam stammers. She notices that her own breathing has become difficult and that her chest is beating faster than she'd like. She hadn't noticed how intensely she was clenching her hands."

    "Sam breathes in and out and paces a little. Cheyenne looks at Sam nervously, smiling."

    s "Okay! Soooo..."

    s "I... really... I'm... I want you to know that I think you're one of my best friends and thank you for dealing with me and coming by the house and hanging out..."

    "Cheyenne nods expectantly. Sam continues."

    s "I... we've been friends since we met during tryouts, and you're really awesome, and you're kind, and smart, and pretty. And..."

    ch "Sam..."

    s "I...! I really like you! I like-like you. And I hope that's okay. And..."
    "Sam's eyes begin to tear up."
    s "I'm... I'm wondering if you like me, too."

    "Sam realizes she's breathing in really hard, and she's crying. Embaressed beyond repair, she wipes her face, holding her ground, every microsecond feeling longer than it needs to."

    ch "Sam, I... thank you so much."
    "Her voice is noticably calm."
    ch "Sam, I like you too, and thank you for telling me this. But I need to think about it. Us, dating, I mean... I need to think about it."

    "Sam looks up to Cheyenne's face -- she looks so much more adult than how Sam feels right now; Sam feels like a small child being consoled by an adult. Sam nods."

    "Cheyenne gives Sam a big hug and wipes her tears away."

    ch "I'll see you at school, okay?"

    "Sam replies, her voice broken."

    s "Yeah..."

    "Cheyenne walks away as Sam watches. She turns around to wave, and Sam waves back. Sam heads home."

    ".:. Confession Ending."
    jump credits

label goodlongday:
    "Finally, Katey and Sam come home, and Sam goes and falls onto her bed. She naps for an unknown amount of time until Katey wakes her up, walking into their bedroom with glasses of water."

    k "Hey Sam. That sleepy, huh?"
    "Katey rests one of the cups on the night counter."

    s "Mhmm."
    "Sam mumbles in reply, half awake."

    k "Okay, sleepyhead. Want me to turn off the light?"

    s "Mmm."

    k "Okay, goodnight~."
    "Katey switches off the light as she leaves the room, closing the door."

    ".:. A Good, Long Day Ending."
    jump credits

# A Good Long Day paths

label Samtrying:
    "Sam does her best to laugh and smile as the girls escalate this fictional water world. They're having fun, and Sam wants to make sure she's not being a downer."
    "She knows she can be too much. She hates it. She hates everything at this moment and herself the most. But she needs to be more. Katey and Cheyenne and Katey's family put so much energy into her. She can't."
    "..."

    "She lets herself go, to forget the depression and doubt for a moment."

    #manic Sam sprite
    s "But {i}secretly{/i} the {b}aliens{/b} are the cause of destruction of civilization and the flooding of the planet so that they can terraform the planet and the mermaids and human mutations are a {i}hybrid species{/i} that were abandoned by the alien terraformers after there was some kind of internal war due to some kind of ethics strife."
    "So they wind up abandoning terraforming the planet, and there's still maybe a handful still left around in government positions in the few places there are still larger populations of persons"

    #laughing emily
    e "That's some serious world building."

    j "What about dolphins, though? Do they take over or become one of the races of this world that the humans, merpersons, and frog people interact with?"

    ch "Yeah, I think so."

    k "Yeah!"

    "The conversation goes on for quite a bit, and Sam does her best to hold it together, but she's at her limit."

    menu:
        "What does Sam do?"

        "Look around.":
            "Sam notices Cheyenne smiling at her."
            jump Cheyenneeye

        "Go home.":
            jump gohome

label gohome:
    "Sam murmurs weakly to Katey:"

    s "I want to go home."

    "Katey nods and suggests to the group that they must leave for the day."

    "The group shuffles around their table and leave the cafe, talking as they round the block and slowly part ways, hugging and waving bye."
    jump goodlongday

label Kateycomfort:
    "Sam is a little surprised by the gesture, and glances at Katey who's talking with the others. Katey must have felt that Sam needed some emotional support in that moment... or Katey just wants to hold onto Sam."
    "Its unclear, but she lets Katey continue to do so, adjusting her own hand to hold Katey's."

    "Sam had begun living with Katey since she was 14 or so; her mother took on a new job that required her to be abroad. At first, she'd come back and stay for weeks at a time, but eventually she just stopped coming back, and Sam stopped bothering her."
    "Katey and her family remained Sam's only emotional support, and at times this meant she felt like a burden. Katey and her parents would violently disagree with such a claim, but it's how Sam would feel sometimes."
    "They're Sam's god-parents, and she herself had grown up with Katey her entire life. Sam's parents never had other kids, but Sam never felt like she needed more than Katey and her siblings anyways. As far as Sam is concerned, Katey is her sister."

    "Sam feels some comfort in this, some of her anxiety and tension relieved. Katey knows that Sam can feel exhausted when she's out like this."

    menu:
        "What does Sam do?"

        "Look around.":
            "Cheyenne keeps glancing at Sam. Sam catches her eye."
            jump Cheyenneeye

        "Go home.":
            "Sam feels like going home."
            jump gohome

# bad end path
label Samignores:
    "Cheyenne stands up and excuses herself to go to the bathroom."

    "A sense of exhaustion overwhelms Sam. It'd been a long day, and it was time to go home."

    menu:
        "A sense of exhaustion overwhelms Sam. It'd been a long day, and it was time to go home."

        "Stick it out.":
            "Sam decides she should stick it out and wait for Cheyenne to come back before leaving."
            jump endofday

        "Leave.":
            "Sam turns to Katey and tells her she wants to go home."
            jump Cheyennestops

label Cheyennestops:
    "Sam and Katey leave before Cheyenne comes back, with Katey telling the others to tell Cheyenne they're sorry but Sam's not feeling good. Julia and Emily agree and tell Sam they hope she feels better."

    "Sam and Katey get home, and Sam heads to their bedroom. She slides into her bed, hoping for sleep to make her exhaustion and her darkness to go away. She was done, and she felt done in more than one way. What did anything matter anyways."

    "In the proceeding days, Sam skips school more often, staying at home more often, and Cheyenne eventually stops coming by to pull Sam out of the house. Eventually, everyone but Katey stops."

    "Graduation would be the last time Sam sees Cheyenne."

    ".:. Depression Ending."
    jump credits

######################## credits

label credits:
    "Thank you for playing {i}{b}Before The End{/b}{/i}!"

    "There are several endings! Which one did you get? Did Sam confess? Did Cheyenne have a moment with Sam in the restroom? Did nothing happen? Or worse?"

    "Let me know what you think so far!"

    "I want to thank various members of the Yuri Game Jam 2017 Discord for helping me a ton with programming questions, including Leethe, Raven, Liz Aardt, and others!"

    "If you liked Sam and her story, you can follow what happens in her life after high school (and becoming a time traveler!) in my webcomic, {i}Time Fiddler{/i}, which you can read at the following links:"

    "http://timefiddler.com"
    "http://tapas.io/series/timefiddler"
    "http://www.webtoons.com/en/challenge/time-fiddler/list?title_no=33282"

    "You can also follow me on:"
    "http://twitter.com/timefiddler"
    "and"
    "http://instagram.com/timefiddler"

    "Please look forward for the next update!"
    return
