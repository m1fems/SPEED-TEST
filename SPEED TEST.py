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
