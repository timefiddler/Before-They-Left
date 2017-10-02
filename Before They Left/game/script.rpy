#Backgrounds
# image bg cafe "cafe.png"
# image bg cafe dark "cafe_dark.png" #darker, washed out version; for depression and opening
# image bg wc "wc.png"
# image bg outcafe "outcafe.png"
# image bg corner "corner.png"
# image bg bedroom "bedroom.png"

#Character sprites
# image sam down "sam_down.png"
# image sam up "sam_up.png"
# image sam depress "sam_depress.png"
# image sam blush "sam_blush.png"
# image sam bold "sam_bold.png" #for confession dream
#
# image sam2 down "sam2_down.png"
# image sam2 up "sam2_up.png"
# image sam2 depress "sam2_depress.png"
# image sam2 blush "sam2_blush.png"
# image sam2 bold "sam2_bold.png" #for confession ending
#
# image cheyenne normal "cheyenne_normal.png"
# image cheyenne smile "cheyenne_smile.png" #cheery appearance
# image cheyenne mute "cheyenne_mute.png" #when she's denied (getting sam a drink) or disappointed
# image cheyenne intimate "cheyenne_intimate.png" #for wc ending
# image cheyenne2 normal #<---light sports windbreaker, loose fitting, blue, when they're outside. needs additional sprites based on confession sequence
#
# image katey normal "katey_normal.png"
# image katey shocked "katey_shocked.png" #for sam's travel variable
# image katey laugh "katey_laugh.png"
# image katey smile "katey_smile.png"
# image katey fingerguns "katey_fingerguns.png"
#
# image julia normal "julia_normal.png"
#
# image emily normal "emily_normal.png"

define s = Character('Sam', color="#CB3766")
define ch = Character('Cheyenne', color="#B95229")
define k = Character('Katey', color="#173FB2")
define j = Character('Julia', color="#6E21D2")
define e = Character('Emily', color="#76D947")

label start:
    $ disappointCheyenne = False
    $ yesdrink = False
    $ nodrink = False
    $ yesnachos = False
    $ extradepress = False
    $ crushpower = False
    $ travelmention = False
    $ Kateytravelnerve = False

    # scene bg black
    # with dissolve

    "..."
    "A cascading wave of isolation fills Sam, with thoughts of entire lifetimes of loneliness creeping in the undercurrent, but mostly just how she feels right now."
    "It didn't make sense. Her brain didn't make sense. Everything in her right now is wrong. She knows that, logically."
    "Why."

    # scene bg cafe dark
    # with fade

    "Crushing darkness surrounds her, exacerbated by harsh florescent lights, and the glare of the sun's reflection off of... everything."
    "Sam closes her eyes. {i}Why is it so god damned bright?{/i} Sam thinks, though not in so many words, but more as a feeling."
    "Words won't fill her head. No, her mind is molasses. Why can't she be back in bed?"

    "The chattering noise around her wouldn't be ignored much longer, nor was she allowed to. Her friends would expect her to talk, or at least say a thing, or join them somehow."

    "A sympathetic voice interrupts."
    "???" "What are ya thinking about, Sam?"

    "Sam's placid pond that she'd put so much effort into focusing on is ruined by a ripple. Eyeballs crawl all over her. Sam raises her gaze to the voice."

    # show cheyenne smile
    # with dissolve

    "It's Cheyenne -- she looks beautiful, effortless, and rugged at the same time. They were both on the girl's basketball team, well... Sam used to be."

    "Cheyenne had made an effort to stay friends with Sam after she'd quit. Sam appreciated the gesture, but... something. Or nothing?"

    "Depression."
    "Sam has depression -- or some form of it that her therapist wrote on her file."
    "Who the fuck cares what it is. Sam wants to go home and sleep. They had spent the day outside hanging out, talking about this and that, eating food and getting boba tea..."

    menu:
        "Sam toys with the leftover boba and ice in her cup with a wide, orange straw, replying..."

        "\"Nothing, actually. Yeah, I'm not really thinking about anything; just listening to you guys talk.\"":
            jump drinkoffer

        "\"Nothing, I'm just sleepy\"":
            jump drinkoffer

        "\"I'm just thinking about how much you guys hang out with me even though I'm just a depressed idiot.\"":
            jump depression

        "\"Cheyenne, have I ever told you you're beautiful?\"":
            jump confessiondream

label drinkoffer:

    ch "Oh, ok. Do you want another boba tea?"

    menu:
        "Sam looks down at her cup, and glances at the drink emptiness levels of her friends at the table. They all have varying amounts."

        "\"Sure, I could go for another.\"":
            $ yesdrink = True
            jump kateystory

        "\"Nah, I think I'm good.\"":
            jump nothanks

label nothanks:
    $ nodrink = True
    ch "You sure?" #look concerned
    s "Yeah. Thank you, though."

    "Sam appreciates the gesture, but the anxiety of owing Cheyenne when she's doing so much for her already wasn't exactly a comfortable thought."
    "Plus, she kinda needs to pee but is stuck between a wall and two other people on her side of the table."
    jump kateystory

label kateystory:
    $ chedrink = _("")
    if yesdrink:
        $ chedrink = _("Cheyenne gets up and stands in line to order. ")
    "[chedrink]K-pop fills the air while Howl’s Moving Castle plays on a nearby flat panel screen in silence. Sam picks at the tray of fries on the table while her friends start talking about boys at school."

    "Apparently there’s someone that Julia and Emily have a crush on, but is maybe problematic."
    "Who cares. No boy’s ever liked Sam like that to begin with. There were a few times where things got awkward with someone at school, but that was it."

    "Someone prods Katey about who she has a crush on."
    "Katey is Sam's childhood best friend; Katey's parents are Sam's god-parents, and she lives with Katey's family while her mom is abroad. Sam’s mom is abroad a lot. Well, all the time."

    k "That’s a secret." #fingerguns

    "Katey teases, motioning finger guns dramatically. The girls groan and pry more."
    "Sam watches in amusement, since she's pretty sure Katey’s crush isn’t anyone at school but a collection of anime and videogame characters."
    "Sam and Katey had talked about crushes plenty of times growing up, whether it was a girl at school, some pop star, or a youtuber. But Sam hasn't felt very strongly about someone since she was in middle school."
    "At least, Sam likes to think she shows ambivalence about romance, though it couldn't be further from the truth."

    "Katey probably knows Sam likes girls, but hasn't said anything. They were practically sisters, but Sam never talks about herself when the subject is broached -- she just has more fun getting swept up in talking with Katey about her newest {i}waifu{/i}."

    "Sam hasn’t thought about crushes lately. She doesn’t want to. The mere thought of rejection is enough to stop the thought in its tracks. She didn’t need more anxiety and doubt about being worth someone’s love like that."
    "She does that plenty on her own."

    menu:
        "Should Sam tell the others about Katey's crush?"

        "\"Well, you know, Katey has a crush on me.\"":
            jump kateycrush

        "What about that one girl...":
            jump juliastory

        "\"Sailor Jupiter.\"":
            jump Jupiter

        "Zone out of the conversation." if nodrink:
            jump nachoorder

        "Watch Cheyenne instead." if yesdrink:
            "Sam's gaze floats to Cheyenne, who just got to the clerk to make her order."
            jump stareCheyenne

label nachoorder:
    $ yesnachos = True
    "A part of Sam feels bad for zoning out and not participating in the conversation, but honestly this is par for the course, and no one really expects more from Sam. She feels most comfortable like this. No one asking questions, no one needing answers."
    "Just being there was hard enough."

    ch "Man, I'm still really hungry. Anyone else want to share nachos?"

    e "They have nachos here?"

    k "It's like... tater-tots with bacon and gravy or something."

    e "That's not nachos!"

    s "I'll share, but I need to go to the bathroom first."

    "Cheyenne stands up from her seat with more excitement for these \"nachos\" than one would expect. Katey and Julia stand up for Sam to get out and go to the restroom."

    #scene bg wc
    #with fade

    "Sam heads to the restroom and does her business. Washing her hands, she catches herself in the mirror."

    "She looks like a total mess. Her bangs have grown out way too long, her hair has split ends everywhere, frizzing out all over the place."
    "Using one of her wrist bands, Sam pulls her hair back into a ponytail."

    "{i}There, that looks a little better{/i}, Sam thinks to herself. At least she didn't make the bad call of wearing her pajamas out. That'd be maybe too sad."

    #scene bg cafe
    #with fade

    "Sam leaves the restroom and joins the group. Cheyenne is in line at the counter."

    "The conversation has turned to teachers they hate. Sam doesn't have the energy to have strong opinions about this, so she zones out a bit more while sucking on the water that melted from the ice in her empty boba tea cup."

    "Sam's gaze wanders to Cheyenne, who just got to the clerk to order \"nachos.\""
    jump stareCheyenne

label stareCheyenne:
    $ thanks1 = ("")
    if yesnachos:
        $ thanks1 = ("Sam thanks her.")

    "Cheyenne always kind of stuck out from the crowd. Straight-A student, AP class load, shoe-in for a number of academic and sports scholarships. But she was just... really extra nice to Sam for some reason."

    "The thought makes Sam feel guilty and worthless."

    "She needs to stop; even though its annoying and frustrating, Cheyenne and Katey keep dragging Sam out of the house every day for her benefit. Sam knows this, but... at the same time it didn't make sense."

    "Why."

    "Cheyenne is so beautiful. Her sun-kissed skin compliments her soft brown hair, clipped to the side of her head haphazardly with bobby pins, and yet despite the \"mess,\" it looks wild and perfect."

    "Wearing a black sport tank top, her shoulders flex every so often to show off the power hidden beneath, lightly spotted with freckles."

    "..."

    "Sam realizes she's staring far too intensly and darts her eyes back at whoever's talking."

    "Cheyenne comes back to the table with a receipt, a \"45\" printed in large text at the top. A waft of apricot and mango washes over Sam -- was that Cheyenne?"
    "She gives Sam a cheery smile. [thanks1]"
    if yesnachos:
        jump thanks2
    else:
        jump collegemenu

label thanks2:
    ch "De nada."
    jump collegemenu

label collegemenu:
    menu:
        "Sam watches as Cheyenne seats herself, and wonders if she should ask something..."

        "Ask where Cheyenne's going to college.":
            jump Cheyennecollege
        "Ask the group if they'd decided what they're doing after high school":
            jump emilystory
        "Go back to picking at fries." if extradepress:
            jump lonerfries

label Cheyennecollege:
    $ travelmention = True
    ch "Oh, I haven't really decided yet. I've gotten a few acceptance letters but I was really hoping to go to UCLA."
    "Cheyenne looks up and away -- her face mixed with excitement and anxiety."

    "Sam nods and smiles. She hadn't been doing any planning for college, even though everyone kept pushing her to do it."
    "Katey was going to go to a famous fashion school in the City while commuting from home, and Sam figured it'd be pragmatic of her to do something similar."
    "Except..."

    s "Traveling away sounds nice..." #depressed expression

    "Katey looks at Sam with some surprise and trepidation -- this is the first time she's heard this."

    ch "How about you? Does Samantha Fiddler have any plans?"
    "There's a lilt in Cheyenne's voice as she teases her."

    "She had set herself up like a fool, now faced with having to actually-probably give an answer to the very question she has no desire to answer to begin with. Small talk sucks."

    "Any plans that Sam may have had in the past were long dashed. The future just... she'd skipped school too many times and dropped out of a number of classes."

    "Depression had hit her too hard in junior year to bother trying to make up for it in her senior year."

    "Her immediate goal was to catch up on credits and at least graduate with her class."

    menu:
        "How does Sam answer?"

        "Be Aloof.":
            "Sam looks away, staring at a wall."
            s "Not really." #absentminded sprite
            jump CheyenneOh

        "Answer her directly...?":
            $ disappointCheyenne = True
            "Sam replies sheepishly."
            s "Not really...?" #sheepish appearance sprite
            jump CheyenneOh

        "Notice Katey who's been staring.":
            "Sam looks at Katey, who she's just noticed is staring somewhat invasively at her, realizing that she hadn't really talked to her about any of this. Sam had avoided the subject."
            jump Kateytravelfight

label CheyenneOh:
    ch "Oh." #looks disappointed? neutral?

    "Cheyenne is aware of Sam's class credit situation, but had wondered if Sam had any particular ambitions she wanted to pursue. Well, maybe the depression was just too much to even think that way at all."
    "She'd done her share of reading on depression... but it still felt so alien to her."
    "She wanted to be supportive and a good friend, but... she knew she'd need to focus on herself, with school and leaving home for college. Katey would always be there, at least. Well, in theory."

    "Sam feels a sudden weight dropped on her, like she had disappointed Cheyenne. It wasn't her fault that she wasn't going to a fancy college, fully paid. Well, it was, but it wasn't, but fuck you. The feeling hurt Sam. It felt irrational."

    if yesnachos:
        "Clerk" "Number 45! Nachos fully loaded!"
    if yesdrink:
        "Clerk" "Number 45! Black milk tea tapioca!"

    if yesdrink and disappointCheyenne:
        "Sam feels her stomach twist as Cheyenne gets up to get the boba tea. Why did Sam tell her that she could go for another? Why? Fucking why? Shit. Fuck. Shit. Fuck. Fuck. Fuck. Fuck."

    menu:
        "Sam's depression decides to kick up her anxiety as Cheyenne heads to the counter..."

        "Pay Cheyenne." if yesdrink and disappointCheyenne:
            "Sam reaches for her wallet to pay Cheyenne for the drink."
            jump wallet

        "Worry about how to pay for the drink." if yesdrink and not disappointCheyenne:
            "Sam gets lost in her head feeling guilty about how she should repay Cheyenne for the drink..."
            jump bringorder

        "Worry about how to pay for nachos." if yesnachos:
            "Sam gets lost in her head feeling guilty about how she should repay Cheyenne for the nachos..."
            jump bringorder

        "Calm down.":
            "Sam calms herself down. Cheyenne didn't even say anything. {i}It's all in your head{/i}."
            jump bringorder

label wallet:
    "Katey blocks Sam's arm, seeing what she was about to do and lightly shakes her head \"no.\" The other girls notice silently. Sam looks around at the others and pulls her hand away. Sam feels guilty, but Katey can be surprisingly stern."
    jump bringorder

label bringorder:
    $ bringnachos = ("")
    $ bringdrink = ("")
    if yesnachos:
        $ bringnachos = ("loaded tater-tots at the center of the table")
    if yesdrink:
        $ bringdrink = ("newly sealed boba drink gracefully infront of Sam")

    "Cheyenne comes back to the table and places the [bringnachos][bringdrink], taking her seat."

    s "Thanks, Cheyenne."
    "Sam musters the best smile her depressed butt can."

    #Cheyenne smiling sprite
    "Cheyenne smiles back with her eyes."

    if yesdrink:
        "Sam punctures the seal on her cup with her straw and takes a sip. It tastes pretty good, but why wouldn't it? Sam sees that Cheyenne is watching her intently, and then sees her turn to Katey."
    if yesnachos:
        "Sam gingerly picks up one of the taters with sauce on it and pops it into her mouth. It tastes pretty good, better than the soggy tater tots from middle school. She notices Cheyenne watching her intently, and then sees her turn to Katey."

    ch "Hey, did you ever watch that one show with giant robots and like its a fantasy world and the main character's this high school girl who's from our world but gets transported to the moon or something?"

    k "Oh, Escaflowne! Yeah, I really liked that show."

    ch "Yeah, yeah! Escaflowne!"

    k "It's one of my dad's favorites; we got the DVD set, but we have this huge, old VHS box set in the garage, too."

    ch "Wow! Yeah, man, I haven't seen that in forever. I think I saw it at my cousin's home when my family went skiing or something when I was like seven, but yeah, I couldn't remember the name of it."

    "Katey brings it up on her phone and shows Cheyenne."

    ch "Yeahh!! This is it. That's cool. So you have the box set, huh?"

    k "Do you wanna borrow it?"

    j "You know, we should just have a marathon viewing party or something. Make it a thing."

    "The others agree. Sam just anticipates feeling overwhelmed, but it'll probably be ok. Its just watching anime and eating food, right? Katey shoots a text to her dad."

    j "Sam, you should make your famous chili dip."

    ch "Oh? How come I've never heard of this?"

    menu:
        "How does Sam answer?"

        "\"It's nothing, but yeah, I can do that,\"":
            $ disappointCheyenne = False
            jump sampressure

        "\"It's nothing special. Katey's mom can do it better.\"":
            $ disappointCheyenne = True
            $ extradepress = True
            jump sampressure

label sampressure:
    if disappointCheyenne:
        "Cheyenne looks a little disappointed. Katey speaks up."
        k "I mean... I guess if you don't want to, mom can do it."

    if disappointCheyenne == False:
        ch "I'll be looking forward to it." #Cheyenne smiling

        "{i}Julia, why did you have to go and open your big mouth{/i}, Sam thinks to herself. This wasn't pressure she needed... but it'd pay back Cheyenne for the food."

    "Emily talks about her favorite anime and some new smartphone dating sim game. It's a yaoi game."
    "Sam listens with vague interest. It sounds a bit absurd, and maybe too much upkeep. Sam's phone is a few generations back, though, and probably can't play it."

    k "I keep seeing fan art for it on tumblr. I was wondering what it was."

    j "Yeah! Its dumb but its pretty fun 'cause you kind of interact with the characters like it's a messaging app. There're a bunch of endings, too."

    "Julia plays it, too? Sam wonders if she's behind the times. Staying home and skipping school does have its effects."

    "The conversation slows into a lull, which is then interrupted by the sound of a food processor."

    "Julia proposes a hypothetical question."
    jump Act2

################ Opening labels - depression - confessiondream

label depression:
    $ extradepress = True
    "The girls are a little stunned at Sam's statement."

    k "Sam, no! We love you!"
    "Katey puts her arms around Sam reflexively."

    "The girls all follow with \"Yeah!'s\" and \"Hey!'s\""

    "Cheyenne reaches her hand out across the table to Sam, palm up."

    ch "Sam, we're your friends, and you're here because we want you here with us. {i}I{/i} want you here."

    "Sam is a bit overwhelmed by the affection but feels a little better. Nothing feels genuine about this moment, and she feels numb, but a little better all the same. Sam reachs for Cheyenne's hand, who grips it."

    ch "Sam, look at me." #cheyenne serious look

    "Sam complies. She feels like such an oaf. Here she is, sitting a good half foot or more above the others except Cheyenne, slouching, and being given this affection."
    "She doesn't deserve any of this. She probably said what she did because she wanted the attention. She's such a fake."

    "Guilt begins creeping up Sam's throat."

    "Cheyenne continues, putting on her best soothing voice."

    ch "Sam, we're your friends, and we want you to have fun and have a good time. You know that, right?"

    "{i}Have fun? This is {b}exhausting{/b}. But yeah, its fun{/i}, Sam guesses to herself."

    s "Yeah, I guess..."

    "Sam looks away in shame. Katey tightens her grip on her, while Cheyenne grips Sam's hand once more before withdrawing."

    ch "Good."

    "Cheyenne smiles at Sam with a hint of consternation."

    "The table is quiet for a moment. Cheyenne eyes Sam's empty cup."

    ch "Hey Sam, do you want another boba?"

    menu:
        ch "Hey Sam, do you want another boba?"

        "Sure":
            $ yesdrink = True
            s "Uhhh... sure, I guess? Thanks."
            jump kateystory

        "No thanks":
            "Sam looks at the empty cup before her and replies."
            s "I think I'm good."
            jump nothanks

label confessiondream:
    #scene needs hazier version of cafe that fades in
    "Cheyenne and the whole group is completely shocked, but Cheyenne the most. This isn't just some plain compliment, teasing or otherwise. Sam had said it in a very clear, forward kind of way."

    "Sam is also not really feeling like giving a shit about inhibitions at the moment."

    "Sam feels Katey is possibly more surprised than anyone in the group, but that's only because she's right next to her. But Sam's not looking at Katey, she's looking at Cheyenne."

    ch "Uhh...! Thank you? Thanks, Sam, I appreciate it. You're gorgeous, too!" #nervous? unsure?

    s "Cheyenne...!" #looks really bold

    s "I've had a crush on you for a really long time, and I want to ask you out. You've been on my mind a lot, and I want you. Will you have me?"

    "The group, and quite frankly at this point the entire cafe, is stunned into silence, everyone at the edge of their seats."

    ch "Sam... I..."

    "Sam..."

    s "Cheyenne..."

    ch "Sam..."

    "Sam..."

    "???" "Sam......"

    "..."
    #scene change to cafe, bright. Look into screen shake animation? shake bg?

    "Sam is shaken awake."

    "She'd been dreaming. It was only a dream. Jesus christ."
    #Sam looks haggard

    "The harsh florescent light, smell of fried food, overly sweet drinks, and the sound of some asian pop music fills Sam's senses all at once. Its overwhelming. God, why is she awake. And her neck aches, too."

    "A voice next to her speaks up."

    "???" "Sam."

    #show Katey sprites

    k "Sam, you were mumbling in your sleep."

    ch "We wanted to let you sleep since you conked out so quickly, but thought you might want to wake up instead of sleep talking in public."

    j "It was pretty funny." #julia giggling with hand over mouth sprite

    "Sam is barely awake enough to feel embarrassed, though only barely. It wasn't the first time."

    ch "Sam, do you want another boba tea? It might help wake you up."

    menu:
        ch "Sam, do you want another boba tea? It might help wake you up."

        "Yes":
            $ yesdrink = True
            "Sam stretches a bit and yawns."
            s "\"Sure, yeah, that sounds good.\""
            jump kateystory

        "No":
            "Sam yawns."
            s "Oh it's okay -- I'll probably grab a cup of water later instead."
            jump nothanks

################## labels for kateycrush, juliastory, and Jupiter. they all go to nachoorder

label kateycrush:
    "Katey's face is flush red."

    "Sam, who's both oblivious and joking, doesn't see Katey's reaction and laughs."

    s "I'm kidding, I'm kidding!"

    "Sam, waving her arm in the air like a drunk, but more sleepy/tired and a touch depressed than drunk."

    "The others kind of just look back and forth between Katey and Sam with surprise and anticipation. {i}They{/i} know that Katey has a crush on Sam, but Sam had been pretty oblivious to it. Like, really oblivious."

    "Bets were made -- that's how bad it is."

    "Katey isn't aware of the bets. It really doesn't help that Katey kind of refuses to make a move. She's become somewhat complacent, in a way."

    "Cheyenne's bet that Sam will never figure it out. Emily and the others have bets one year apart of each other starting with post-graduation."

    "Eager to change the mood, Katey turns the conversation towards plans for the summer."

    "Sam decides to tune out and stare outside."
    if yesdrink:
        "Sam stares at the same space for a good ten seconds before she realizes she's been staring at Cheyenne."
        jump stareCheyenne
    else:
        jump nachoorder

label juliastory:
    "Sam takes a moment to ponder. Isn't there someone that Katey has a crush on that isn't an anime character?"

    s "Katey, isn't there like a cosplayer you saw at a convention that you follow online... what's her name..."

    k "Who... oh, you're talking about Alexa. Sam, don't you remember, we had dinner with her last year."

    s "Oh... really? You'd have to show me her face, I really don't remember. All I remember is you fangirling over someone and making me almost trip."

    k "Yeah, that was her. She was really cool."

    j "What about you, Sam? Who's your crush?"

    "Julia is part of Katey's extended family, on her dad's side. Katey was... Julia's aunt? Or something? Second cousin, twice removed or however the hell that works?"

    "That system never made sense to Sam. It never made sense to Katey either, which is why she likes to call Julia her niece."

    "Julia doesn't like it."

    "She's cool though, pretty chill, very smart. She's right up there with Cheyenne for grades, though definitely more computer science oriented. And memes."

    s "Ehhh..."

    "Sam squirms uncomfortably. Sam didn't really have any answers."
    "Sam speaks slowly trying to find footing, naturally leaning to a corny non-answer."

    s "Who... needs... crushes... when you have friends...?!"

    j "You're just as bad as Katey, Sam."

    "Sam laughs."

    "Julia shifts the conversation back to that boy that she and Emily have a crush on. Sam tunes it out, her eyes now wandering around the cafe."

    if yesdrink:
        "Sam zoned out, only to realize she was staring at Cheyenne's butt."
        jump stareCheyenne
    else:
        jump nachoorder

label Jupiter:
    $ cheline = ("")
    if yesnachos:
        $ cheline = (" from the line")
    "Everyone but Katey and Sam" "Oooh~"
    "The group coos in unision. Their reaction stumps Sam a bit."

    j "Yeah, I can see that."

    e "Yeah!"

    "Cheyenne proudly chimes in[cheline]."
    ch "I'm more of a Sailor Uranus girl."

    "Katey bursts out laughing. Sam and Cheyenne look confused."

    k "Your-Anus?"

    ch "What, I mean isn't that how its pronounced?" #Cheyenne looks annoyed/defensive/furrowed brows?

    j "You're supposed to say it \"Yur-Rin-Us.\""

    s "I mean, that just sounds like \"urine,\" though. Either way you can't win."

    ch "{i}Anyways{/i}, she's my favorite! Her and Mars!"

    j "Katey, you should cosplay Neptune."

    k "What, because my hair's blue?" #scoffing, annoyed

    "Everyone else looks at each other for a moment."

    "Everyone but Katey" "Well, yeah."

    k "Pffft."
    "Katey rolls her eyes."

    "Katey turns the conversation to favorite animes airing at the moment, but Sam is still on what Cheyenne had said. She'd be a really good Haruka if she wanted to cosplay her, though Sam wasn't sure that Cheyenne would be into that."
    if yesdrink:
        "Sam zones out for a bit, only to realize she's been staring at Cheyenne for longer than not."
        jump stareCheyenne
    else:
        "Katey starts getting really excited about something, and Sam realizes she'd been imagining Cheyenne as Sailor Uranus instead of paying attention."
        jump nachoorder

################### labels for emilystory and lonerfries

label emilystory:
    $ travelmention = True
    #Katey super excited, arms out
    k "FIDM!"
    "It's the fashion school that Katey's been eyeing for years. Sam is pretty sure she's already networked with half of the faculty by this point."

    e "You mean like, college? Or what job I want?"

    s "Whatever."

    "The girls think for a moment. Katey, meanwhile drums the table spelling out F-I-D-M over and over."

    ch "I was thinking of heading down to UCLA, honestly..."
    "Cheyenne almost sounds disheartened, but excited."
    ch "I've gotten some acceptance letters but not all of them. I think I have a pretty good shot, though."

    #show sam looking sincere
    "{i}You do{/i}, thinks Sam."

    e "Honestly I was thinking of taking a trip around the world for a bit. Like, go see Japan and England and stuff."

    "The group wows at her answer; none of them expected to hear that from Emily, of all people."

    "Emily is Cheyenne's childhood friend. You wouldn't guess that the two of them were close with how different they are, where Cheyenne was so extroverted and outdoorsey, Emily tended to be a little mousey."
    "But once Sam had gotten to know her, she was surprised at how sarcastic Emily was."

    "Sam feels that Emily would have been the type to dive right into academia much in the same way that Cheyenne or Julia might, but all of Cheyenne's adventurousness must have finally rubbed off on her."
    "Or maybe she just knows herself too well to disappear into college and get stuck chasing a career her entire life. Or something."

    ch "What about you, Sam?"

    "Before Sam could answer (or try to avoid answering), the clerk calls for Cheyenne's order number."

    "Clerk" "45! Order 45!"

    "Cheyenne perks up at hearing her number and heads to the counter."
    jump bringorder

label lonerfries:
    "Sam wonders how long it'd take to die from just eating fries."

    "..."

    "Sam realizes how stupid that is. Fries aren't even the best food."

    "Sam starts daydreaming about a great war between the French Fries and Potatoe Wedges. How absurd that would be, with such minor differences between the two that they'd wage war for whole generations. They'd bleed ketchup (or mayo? Maybe the wedges bleed ketchup and the fries bleed mayo?) They'd call it the... the..."

    "..."

    "Sam is unable to think of a good pun. After a moment, she gives up and eats the last fry that she'd been playing around with. Sam is just... tired."

    "Katey takes a picture of Sam. Sam reflexively poses. Katey shows Sam the filter she had put on. Its rabbit ears and some weird facial morphing. She's utterly unrecognizable."

    "Sam laughs. Katey smiles."

    k "Hey, group selfie!"

    "Everyone poses the best they can with Katey barely managing to fit everyone into frame. They take a good few."

    "Cheyenne starts talking about a youtube video she saw yesterday when she's interrupted by the clerk behind the counter."

    "Clerk" "45! Order number 45!"

    "Sam watches Cheyenne get up to pick up the order."
    jump bringorder

############### Katey travel unnerve route

label Kateytravelfight:
    $ Kateytravelnerve = True

    $ bringnachos2 = ("")
    $ bringdrink2 = ("")
    if yesnachos:
        $ bringnachos2 = ("the \"super nacho\" tater-tots at the center of the table")
    if yesdrink:
        $ bringdrink2 = ("the boba drink infront of Sam gracefully. Sam cools off and thanks Cheyenne, who nods")

    $ bringdrink3 = ("")
    $ bringnachos3 = ("")
    if yesdrink:
        $ bringdrink3 = ("Sam punctures her new boba tea with her oversized straw, taking a sip.")
    if yesnachos:
        $ bringnachos3 = ("Sam gingerly picks up a tater tot with some cheese and sauce on it, popping it into her mouth.")

    "Sam stares back in surprise."

    k "Did... you want to leave the bay area?"
    "Katey asks Sam, sounding a bit sensitive. Her tone takes Sam aback."

    s "Um... I don't know. I think so. I don't know."

    "Sam isn't sure of how to feel. All she knows is that she's not happy with herself and how she feels overall."
    "The last few years had been hell to get through, and she feels grateful for Katey and her family and Cheyenne and everyone... but still, the feeling of failure doesn't clean easy."

    "The feeling of leaving, fleeing somehow, somewhere away from herself if possible, is what she wants the most. Somewhere away from herself -- she'd crawl out of her skin if it meant feeling unburdened."
    "To stop... everything, and get away."

    k "Well, which is it?"

    s "I don't know!" #angry sam, flustered?
    "Sam responds to Katey... maybe a little too loudly. She feels agitated and flushed. Katey's expression softens. Sam, less so."

    "What does it matter to her? It's Sam's life, and she has to deal with her brain 100\% of the time. It sucks. She hates this."

    "Clerk" "Number 45! Number 45!"
    "The clerk calls from behind the counter. Cheyenne gets up to get her order and comes back, placing [bringdrink2][bringnachos2]."

    "[bringnachos3][bringdrink3] She closes her eyes and does her best to ignore the awkward tension at the table."

    "Eager to shift the mood, Julia asks a random hypohetical question."

    jump Act2
