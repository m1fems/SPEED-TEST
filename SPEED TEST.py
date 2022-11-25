import math
import random
import time
list_texts = []
text1 = ("They say that money doesn't bring you happiness,"
         " I say neither does being broke, so let me suffer with a new car.").split(' ')

text2 = ("Oh... and how is education supposed to make me feel smarter?"
         " Besides, every time I learn something new, it pushes some old stuff out of my brain."
         " Remember when I took that home wine-making course and I forgot how to drive?").split(' ')

text3 = ("There's something moving through the windows and walls,"
         " I've seen it before, seen it before. You left me living with a lingering soul,"
         " how little you know, how little you know.").split(" ")

text4 = ("I was shaking like a leaf, so without thinking I lit up a cigarette on the airplane to calm my nerves."
         " I was trembling, I was very emotional and that's when all the rest of it happened. It's very regrettable."
         " Now, I don't want to kick up a fuss, press charges, contact the British embassy."
         " I'd rather not pursue those channels, that's not my style. I'm not that sort of a bloke.").split(" ")

text5 = ("It's a sad communication with little reason to believe when one isn't giving and one pretends to receive."
         " Pardon my heart if I showed that I cared, but I love you more than moments"
         " we have or have not shared.").split(" ")

text6 = ("Any physical theory is always provisional, in the sense that it is only a hypothesis: you can never prove it."
         " No matter how many times the results of experiments agree with some theory,"
         " you can never be sure that the next time the result will not contradict the theory.").split(" ")

text7 = ("One day when I was able to get up, I decided to look at myself in the mirror on the opposite wall."
         " I had not seen myself since the ghetto. From the depths of the mirror, a corpse was contemplating me."
         " The look in his eyes as he gazed at me has never left me.").split(" ")

text8 = ("begin hold hand real govern these old part you develop down feel before develop"
         " while still place state write very").split(" ")

text9 = ("move turn still house think each again should by own eye look should say time each form develop"
         " those both lead from number interest not long").split(" ")

text10 = ("The whole point was to find a way to practice nuclear war without destroying ourselves."
          " To get the computers to learn from mistakes we couldn't afford to make."
          " Except I never could get Joshua to learn the most important lesson.").split(" ")

text11 = ("Outside of two men on a train platform there's nothing in sight. They're waiting for spring to come,"
          " smoking down the track. The world could come to an end tonight, but that's alright."
          " She could still be there sleeping when I get back.").split(" ")

text12 = ("I am Dracula and I welcome you to my house. I must apologize for not being here to greet you personally,"
          " but I trust you've found everything you needed.").split(" ")

text13 = ("His ear heard more than what was said to him, and his slow speech had overtones not of thought,"
          " but of understanding beyond thought.").split(" ")

text14 = "early lead turn general little face these point good school day too".split(
    " ")

text15 = ("May your hands always be busy, may your feet always be swift."
          " May you have a strong foundation when the winds of changes shift. May your heart always be joyful,"
          " may your song always be sung, and may you stay forever young.").split(" ")

text16 = ("So ran the speech. Burdened and sick at heart, he feigned hope in his look,"
          " and inwardly contained his anguish. Aeneas, more than any, secretly mourned for them all.").split(" ")

text17 = ("not nation some while become year to ask without order same increase by well turn man begin most never"
          " back general where such another stand open").split(" ")

text18 = ("seem help life think group both the just part play between then just for people may"
          " want than one do not say around begin both good").split(" ")

text19 = ("Take a drink, my friend, and say what you have in your heart. But you never drink. You never say."
          " Because you are afraid of what you have in your heart!").split(" ")

text20 = ("plan very under become mean might after and write move never just govern fact go than about take or nation"
          " small early both those tell first").split(" ")

text21 = ("The main thing to do is pay attention. Pay close attention to everything, notice what no one else notices."
          " Then you'll know what no one else knows, and that's always useful.").split(" ")

text22 = "I don't want to live someone else's idea of how to live.".split(" ")

text23 = ("I was left there with no water and no food while he stumbled off across the cobbles and up into"
          " the farm-house beyond. There was the sound of slamming doors and raised voices before I heard footsteps"
          " running back across the yard and excited voices coming closer. Two heads appeared at my door.").split(" ")

text24 = ("But he didn't and he never will. We all pay for our choices kid. Maybe your old man fought for you,"
          " maybe he did it for himself. The only thing you know for sure is he's gone now. But I'm here. Now, get up."
          " Time to stop taking a beating and start giving one.").split(" ")

text25 = ("I was assailed by memories of a life that wasn't mine anymore, but one in which"
          " I'd found the simplest and most lasting joys: the smells of summer, the part of town I loved,"
          " a certain evening sky, Marie's dresses and the way she laughed.").split(" ")

text26 = ("big big big big big big big big big big big big big big big big big big big big big big big big"
          " big big big big big big big big big big").split()

text27 = ("For a moment the last sunshine fell with romantic affection upon her glowing face;"
          " her voice compelled me forward breathlessly as I listened - then the glow faded, each light deserting"
          " her with lingering regret, like children leaving a pleasant street at dusk.").split(" ")

text28 = ("I only know that learning to believe in the power of my own words has been the most freeing experience"
          " of my life. It has brought me the most light. And isn't that what a poem is?"
          " A lantern glowing in the dark.").split(" ")

text29 = ("Say what you will. But a person just cannot know what he doesn't know. And you can't always see that"
          " a bad thing is going to happen before it happens. If you could, no bad would ever come.").split(" ")

text30 = "Will the witness please state his name and occupation.".split(" ")

text31 = ("I'm just not the guy for you. I mean, you need a guy who's happy and perky all the time."
          " Maybe a guy who's had part of his brain removed and he thinks he's a bunny and you can go off and"
          " be bunnies together.").split(" ")

text32 = ("I wish I could just make you turn around and see me cry. There's so much I need to say to you,"
          " so many reasons why. You're the only one who really knew me at all.").split(" ")

text33 = ("A powerful monster, living down in the darkness, growled in pain,"
          " impatient as day after day the music rang loud in that hall, the harp's rejoicing call"
          " and the poet's clear songs, sung of the ancient beginnings of us all.").split(" ")

text34 = ("Most popular song lyrics have two sections - a verse and a bridge, where the bridge offers a contrast"
          " to the verse but is not the place where the song is summarized.").split(" ")

text35 = ("When has anyone ever told me I had the right to stop it all without my knuckles, or my anger,"
          " with just some simple words.").split(" ")

text36 = ("Keying text quickly is important, but it is more important to be able to make it look professional."
          " Making the text readable involves positioning, style, and size.").split(" ")

text37 = ("Well, isn't this great, we've all learned something. Tony can't choose who his sister's gonna fall for,"
          " Monica can't choose who she's gonna fall for, and I think that I've learned the greatest lesson of all."
          " I love being lifted.").split(" ")

text38 = ("We look not at the things which are what you would call seen, but at the things which are not seen."
          " For the things which are seen are temporal. But the things which are not seen are eternal.").split(" ")

text39 = ("She hangs her head and cries on my shirt. She must be hurt very badly. Tell me what's making you sad, Li?"
          " Open your door, don't hide in the dark. You're lost in the dark, you can trust me 'cause you know that's"
          " how it must be.").split(" ")

text40 = ("Stay, you're not gonna leave me. This place is right where you need to be."
          " And why your words gotta mean so much to them? They mean nothing to me.").split(" ")

text41 = ("I had considered how the things that never happen are often as much realities to us, in their effects,"
          " as those that are accomplished.").split(" ")

text42 = ("If you come to a river and find a boat at the edge, you will use that boat and it will serve you well,"
          " but once across the river, do you put the boat on your shoulders and carry it with you"
          " on the rest of your journey?").split(" ")

text43 = ("There's a hole in the world like a great black pit. And the vermin of the world inhabit it."
          " And its morals aren't worth what a pig could spit. And it goes by the name of London.").split()

text44 = ("It's an odd feeling, farewell. There is such envy in it. Men go off to be tested for courage."
          " If we're tested at all, it's for patience, for doing without,"
          " for how well we can endure loneliness.").split(" ")

text45 = ("My darling, you have to be standing up in order to be able to fall. I mean, if you keep sitting on your ass,"
          " nothing's gonna happen. 'Only brave warriors fall off their horses in battle."
          " How can kneeling cowards know what a fall is?'").split(" ")

text46 = ("Some feeling had started in my stomach and was traveling up to my face,"
          " and I knew that when it got there I would turn bright red and hear the ocean,"
          " which is what happens when I get put on the spot.").split(" ")

text47 = ("And if I should ever go away, well, then close your eyes and try to feel the way we do today,"
          " and then if you can remember, keep smiling, keep shining, knowing you can always count on me for sure."
          " That's what friends are for.").split(" ")

text48 = "The greatest sources of our suffering are the lies we tell ourselves.".split(
    " ")

text49 = ("Once in a lifetime there comes a motion picture which changes the whole history of motion pictures."
          " A picture so stunning in its effect, so vast in its impact that it profoundly"
          " affects the lives of all who see it.").split(" ")

text50 = ("both long if some both home have can few after open number take since during lead world nation down"
          " play many that mean call world since").split(" ")

list_texts.append(text1)
list_texts.append(text2)
list_texts.append(text3)
list_texts.append(text4)
list_texts.append(text5)
list_texts.append(text6)
list_texts.append(text7)
list_texts.append(text8)
list_texts.append(text9)
list_texts.append(text10)
list_texts.append(text11)
list_texts.append(text12)
list_texts.append(text13)
list_texts.append(text14)
list_texts.append(text15)
list_texts.append(text16)
list_texts.append(text17)
list_texts.append(text18)
list_texts.append(text19)
list_texts.append(text20)
list_texts.append(text21)
list_texts.append(text22)
list_texts.append(text23)
list_texts.append(text24)
list_texts.append(text25)
list_texts.append(text26)
list_texts.append(text27)
list_texts.append(text28)
list_texts.append(text29)
list_texts.append(text30)
list_texts.append(text31)
list_texts.append(text32)
list_texts.append(text33)
list_texts.append(text34)
list_texts.append(text35)
list_texts.append(text36)
list_texts.append(text37)
list_texts.append(text38)
list_texts.append(text39)
list_texts.append(text40)
list_texts.append(text41)
list_texts.append(text42)
list_texts.append(text43)
list_texts.append(text44)
list_texts.append(text45)
list_texts.append(text46)
list_texts.append(text47)
list_texts.append(text48)
list_texts.append(text49)
list_texts.append(text50)

random_text = random.choice(list_texts)
cnt = 0
start_time = time.time()
wpm = 0

print(*random_text)
user_input = input().split(" ")

for i in range(len(random_text)):
    if i >= len(user_input):
        if cnt == 0:
            accuracy = 100 / (len(random_text) / 1)
        else:
            accuracy = 100 / (len(random_text) / cnt)
        end_time = time.time()-start_time
        wpm = round(end_time, 2)/len(user_input)
        print(f'Accuracy: {round(accuracy,2)}%')
        print(f'Time: {round(end_time, 2)}')
        print(f"Words per minute: {wpm}")
        quit()
    if random_text[i] == user_input[i]:
        cnt += 1

if cnt == 0:
    accuracy = 100 / (len(random_text) / 1)
else:
    accuracy = 100/(len(random_text)/cnt)
end_time = time.time()-start_time
wpm = 60*(len(user_input)/round(end_time, 2))

print(f'Accuracy: {round(accuracy, 2)}%')
print(f'Time: {round(end_time, 2)} seconds')
print(f'Words per minute: {round(wpm,2)}')

if accuracy < 100:
    print('Wrong words:')
    for x in range(len(user_input)):
        if user_input[x] != random_text[x]:
            print(f'{user_input[x]} ------> {random_text[x]}')
