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

    menu:

        "I don't see what's so funny.":
            jump 

        ""
            jump


label saddest ending:

    e "I knew that you woud return."

    show bg bothlookoutwindow

    a "Evangeline, I'm tired."


label sad ending:

    a "God, it's cold."

    "The sky is ashy, the sun is dim."

    show bg marilyngrave

    "Adonis squints."

    a "Hello?"









    # This ends the game.

    return
