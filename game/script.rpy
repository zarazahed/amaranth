# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Adonis")
define s = Character("Servant")
define g = Character("Guests")
define e = Character("Evangeline")
define m = Character("Marigold")
define a2 = Character("Acheron")
define k = Character("King")
define m = Character("Mother")
define i = Character("Iris")
define s = Character("Styx")
define o = Character("Orion")
define m2 = Character("Marius")
define h = Character("Helena")

# The game starts here.
label start:

    scene bg room

    show eileen happy

    "The kingdom of Sylthae is the most prosperous in the entire world."
    
    "The royal family has three princes: Acheron, Adonis, and Styx."

    "Acheron is the eldest. He has substantial control over what goes on within the kingdom, serving the role of an advisor to his father."

    "Styx is the most beloved. He is the queen's golden son, showered with praise."

    "And Adonis, the middle child, is the mystery."

    "It is assumed that Acheron will be the one to inherit the throne. It's a fitting role."

    "And in the kingdom of Caelora, there are no princes."

    "The kingdom has been greatly suffering since their previous monarch died in battle."

    "The people have no faith in his widow's ability to rule, and the prospect of the daughter taking the throne eventually is even more grim."

    "Evangeline is an cunning girl, hardened by the pressures she's faced from a young age."

    "Caelora is desperately trying to regain their status as a feared, powerful state, but to no end."

    "They refuse to accept the olive branch that Sylthae has accepted - the people have mutual lingering resentment towards each other."

    show bg ballroom doors

    "However, even while diplomatic ties are strained, nothing is quite as tempting as an invitation to a royal ball, is there?" 

    show bg ballroom
    
    "Adonis is terribly bored."

    # fade in crowd talking music

    a "This is an utter waste of time."

    a2 "You seem to think that about everything."

    a "Well, royal balls in particular are irksome. Everyone laughs far too loudly at the most unfunny of jokes, and the place is entirely too small to fit this many people. If Father hadn't made us attend, you would not see me here."

    a2 "Maybe try to talk to people instead of trailing after me like a ghost. It really is embarassing."

    a "What's the point? Everyone here is only interested in talking to the future ruler of Sylthae. All other conversation is performative."

    a2 "You only think that because you can't fathom speaking to someone if not to simply further your own interests."

    a "As if! I'm charming enough. I'm just tired of talking to people who clearly aren't interested."

    a2 "Maybe try finding some peasants to talk to. Since that seems to be your taste in acquaintances."

    a "What's that supposed to mean?"

    a2 "Nothing. Now go away, I think I spotted the Caeloran queen."

    "Acheron leaves."

    a "Stupid crowded ballrooms."

    a "At least the food isn't half bad."

    show bg ballroom stairs

    "Adonis decides to visit the bottom floor."

    # crowd noise stops

    # play the eerie music

    "Oh? Who's this?"

    # evangeline turning animation

    "Adonis is startled. Anyone would; she looks like a walking corpse."

    "And so, he trips and falls down the stairs."

    "The deity of luck must have surely laughed at that moment."

    # crash noise

    g "What was that?"

    g "Is that Adonis?"

    a "{i}Splendid. Just splendid.{/i}"

    e "Hm."

    "He comtemplates how to reply."

    menu(time=10, timeout="rude"):

        "I don't see what's so funny."
            jump rude

        "You're anything but splendid yourself."
            jump rude

label rude:

    "Evangeline turns and ignores him."

label meeting orion:
    a "Well, if you think that he's competent, then I trust you."

    "The man enters."

    a "Hello."

    o "Hello, Adonis."

    a "I trust that you've been primed on what we expect from you?"

    o "Yes, sir."

    a "I hope you understand how important your role is, Orion."

    o "Believe me, sir, I do. And that's why I feel like I should begin by asking an important question."

    # he takes a seat.

    o "Adonis, are you certain that the person you've been searching for so carefully isn't yourself?"

    # glitch effect, show Adonis sprite with blur, music stops.

    # record scratch ahh

    # a "Yup, that's me! You're probably wonderng how I ended up in this situation, heh. Well, its a long story!!!"

    a "That's... quite a bold question to ask. And a ridiculous one, as well. You should be grateful that I would tolerate that type of accusation."

    o "I mean no offense - I'm simply trying to approach this from an objective perspective. Acheron has been seen at the same time as him. Styx has as well. But he has yet to address you in any of his threats."

    a "Let's rewind a bit. What makes you think that there would be any truth to that kind of theory?"

    o "Well, to put it plainly, your little Caeloran acquaintance does."

    # he pulls out a folder with photographs and letters.

    a "(internally) Where the hell did he find these?"

    a "I still don't see how my relations with the Caeloran royalty are relevant."

    o "It's simple. By assuming the throne, you would find yourself in a position of power. If I had to guess, you would want to honor your mother's Caeloran roots, and avenge her by cutting of ties - if not destroying - the people who led to her death."

    a "I-I don't know what to say. How did you even-?"

    o "Does it not enrage you? Having to look at the faces of her killers? I've done my research, sir"


label marilyn death:

    a "Where's Marilyn?"

    s "She left to the party, sir."

    a "No, don't tell me that. Please, anything but that."

    s "Sir, if you could tell me what - "

    "Adonis sprints out the door."

    a "She's not there. She's not going to be there. She's not..."

    screen black with fade
    
    m "I love Adonis, but he really does worry me."

    h "I don't know what you see in him. He's awfully cold sometimes."

    m "No, he really is a kind man. He's just... "

    m "Where is he, anyways?"

    # music stops, fades out

    # explosion noise

    # random frames showing the destruction n stuff

    m "HELENA!"

    m "Oh, god."

    # helena got impaled by shards of rocks

    m "Adonis! Adonis?"

    "Among the chaos, she runs, searching for a singular face."

    m "Adonis..."

    # second explosion all that fun stuff again

    # pan over to marilyn unconsious

    screen black with fade

    # we see adonis

    a "Marilyn?"

    a "MARILYN!"

    # he spots marilyn

    a "Oh, no. No, no, no."

    "Adonis runs to Marilyn. It can't be, can it?"

    #just imagine ts guy looking like zane from lego ninjago

    #like yk the "NOOO! IT CANT BE!" ahh emote

    m "Adonis..."

    a "Why did you leave?"

    # she's running out of time

    m "Thank you, Adonis."

    # her eyes lose that sparkle

    a "Please wake up. Marilyn. Please?"

label second ending:

    e "I knew that you woud return."

    show bg bothlookoutwindow

    a "Evangeline, I'm tired."

    e "You certainly look it."

    "His eyes grow distant as he gazes at the city."

    a "Isn't it funny, how quickly things change..."

    e "Why did you come?"

    a "I've come to make things right."

    a "We both know that what happened was wrong. This entire mess was avoidable. Dozens of people I knew are dead because of our carelessness."

    e "You can't bring the dead back to life, Adonis."

    a "No. You're right. I can't."

    a "But I can do my part to bring justice."

    "Adonis raises a gun towards Evangeline's neck."

    a "I should have done this the moment I laid eyes on you."

    e "I feel likewise."

    a "As soon as I kill you, your guards will come and drag me off to some prison. Then I'll be tried by the court and everyone will realize how despicable I am."

    a "I'll tell them about my brothers, Marilyn, and the others that I stole life from. Then I'll surely be executed."

    a "At that point, we'll have atoned for our sins as well as we can. Whether we meet again in hell or not is in God's hands now."

    e "Adonis."

    "There is no convincing him otherwise. His eyes are locked on his target, and his grip is firm.

    a "Goodbye, Evangline."

    # shot noise plays

    # show bg evangline getting her brain blown out (silhouette as to not traumatize people :3)

    scene black with fade

    "And so, their tale came to a bitter end."

    "Adonis confessed to everything. When his sentence was declared, he did not resist."

    scene bg execution

    "In his last moments, his eyes flit around the crowd."

    scene bg marilyncrowd

    scene fade with black

    "Ending 1: Justice"

    return

label sad ending:

    "The aftermath of the explosion is void of life."

    "Excepting one half-dead corpse of a prince."

    a "God, it's cold."

    "The sky is ashy, the sun is dim."

    # play marilyns theme

    "Adonis squints."

    a "Hello?"

    "With what feels like the last of his strength, he pushes himself upright and lies against the rubble."

    # show adonis shocked eyes with marilyn in reflection

    a "Marilyn?"

    "He can't believe what he is seeing, because it surely cannot be real."

    scene black with fade

    "Ending 2: Regret"

    return

label third ending:

    "Adonis is asleep. Unsurprisingly, he's not in bed."

    "The desk is covered in letters. Not from foreign officials, but from his late mother."

    # door slam noise

    a "Who's there?"

    o "Adonis."

    a "What brings you here at this hour?"

    "Adonis sits upright."

    o "It confounds me how you can sleep so peacefully, sleep at all."

    o "You filthy traitor."

    a "Orion, calm yourself. What's going on?"

    o "I knew my suspicions were correct. I've known for ages."

    a "Known what, exactly?"

    o "That you're the most vile human I've ever laid my eyes on. My sister, my parents, my lover. God, you've killed everyone. Even the ones closest to you haven't been spared."

    "Adonis carefully shifts his hand towards the guard bell."

    o "Your guards won't come in time anyways."

    a "So you plan to kill me, then? Or take me as your prisoner?"

    o "Listen, you rat. I would take you and torture you in a cellar till the sun rises from the east, if I could. But I would hate having to see your face every day."

    "Orion draws his sword."

    a "Wait. You've misunderstood..."

    o "I'm afraid it's you, {i}prince{/i}, who has misunderstood. You've been dying since the moment you met that witch, and dead since I walked through the door."

    #sword noise

    "Orion accomplishes what he came to do."

    "Ending 3: Assasination."

    return

label fourth ending:

    "Many, many years pass."

    "There is a knocking on the bedroom door."

    a "Come in. Cough."

    m2 "Father, what have the doctors said?"

    a "The usual. That I'm going to die soon."

    m2 "I'm sure that they're just -"

    a "No, Marius. I've seen what this disease can do. I would be a fool to assume that I can survive it."

    "Marius reaches for his hand. Adonis yanks it away."

    a "Idiot child. Don't you have any sense to try to not contact it as well?"

    "Silence."

    m2 "How long do you think you have to live?"

    a "Not long enough, that's certain."

    m2 "First mother, now you... how do you expect me to take up this responsibility by myself?"

    a "I would say that you'll be fine, but truth be told, I have no idea."

    m2 "You could try and give me some advice, anyways."

    a "I don't have much good advice to give, anyways. I lived a pitiful life. There's not the slightest bit of glory in bloodshed, and only a slow-witted young man could imagine otherwise."

    m2 "Is there anything I can do for you?"

    "Adonis hesitates."

    a "There is a grave I want you to visit."

    screen black with fade

    m2 "Beloved daughter... and wife... Marilyn?"

    #bittersweet music starts, maybe music box noise?

    "Adonis came every week, with amaranths."

    "His regrets never faded, nor did the memory of Marilyn."

    #scene bg with grave with dozens of rotting amaranths.

    m2 "{i}Father said that I was named after her.{/i}"

    "He leaves amaranths on her grave."

    "Ending 4: Remembrance"
