import json
import sys
from time import sleep
from googletrans import Translator, LANGUAGES
import random
import os
import pyperclip
import ctypes
from fuzzywuzzy import fuzz
import hashlib
translator = Translator(raise_exception=True)
clear = lambda: os.system('cls')
languages = ["af", "sq", "am", "en", "ar", "hy", "az", "my", "eu", "be", "bn", "bs", "bg", "ceb", "cs", "ny", "zh-CN",
             "da", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "gu", "ht", "ha", "haw", "iw", "hi", "hmn", "nl",
             "hr", "ig", "id", "ga", "is", "it", "ja", "jw", "yi", "yo", "kn", "ca", "kk", "km", "ko", "co", "ku", "ky",
             "lo", "la", "lt", "lv", "lb", "hu", "mk", "ml", "ms", "mg", "mt", "mi", "mr", "mn", "de", "ne", "no", "pa",
             "ps", "mn", "pl", "pt", "ro", "ru", "el", "sm", "st", "sd", "si", "gd", "sk", "sl", "so", "sr", "su", "sw",
             "sn", "es", "sv", "tg", "ta", "te", "th", "tr", "ug", "uk", "ur", "or", "uz", "cy", "vi", "xh", "zu"]


def getsimilarity():
    with open('settings.json') as f:
        data = json.load(f)
    return data['similarity']


def getlang():
    with open('settings.json') as f:
        data = json.load(f)
    return data['language']


def getlangword():
    with open('settings.json') as f:
        data = json.load(f)
    return data['languageword']


def getlangs():
    with open('settings.json') as f:
        data = json.load(f)
    return data['languages']


def getdelay():
    with open('settings.json') as f:
        data = json.load(f)
    return data['delay']


def getseedinput():
    with open('settings.json') as f:
        data = json.load(f)
    return data['seedinput']


def choose():
    if getlangs() > 50:
        with open('settings.json') as f:
            data = json.load(f)
        data['languages'] = 50
        rewrite = open("settings.json", "w")
        json.dump(data, rewrite)
        rewrite.close()
    ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Menu')
    clear()
    type1 = input("(1) Translate phrase\n(2) Translate text.txt\n(3) Settings\n(4) Exit\n").replace(" ", "")
    if type1 == "1":
        translate()
    elif type1 == "2":
        translatefromfile()
    elif type1 == "3":
        settings()
    elif type1 == "4":
        sys.exit()
    else:
        choose()


def translatefromfile():
    ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | File Translate')
    langs = []
    clear()
    if getseedinput():
        seed = input("Seed: ").encode(encoding='utf-8')
        if not str(seed).isnumeric():
            hashed = hashlib.md5(seed).hexdigest()
            seed = int(''.join([n for n in hashed if n.isdigit()]))
        random.seed(seed)
    num = getlangs()
    word = open("text.txt", "r", encoding="utf-8").read()
    if word == "":
        choose()
    startlang = LANGUAGES[translator.detect(word).lang].title()
    laststring = ""
    startword = word
    for i in range(num):
        languageindex = random.randrange(0, 104)
        language = languages[languageindex]
        langs += [language]
        try:
            word2 = translator.translate(word, dest=language)
        except:
            input("You are ratelimited! Wait a while or use a VPN/proxy.")
            choose()
        print(f"{LANGUAGES[language].title()}: {word2.text}\n\n")
        word = word2.text
        sleep(getdelay())
    try:
        finalword = translator.translate(word, dest=getlang())
    except:
        input("You are ratelimited! Wait a while or use a VPN/proxy.")
        choose()
    for i in langs:
        laststring += LANGUAGES[i].title() + " -> "
    print(f"\n\n\n\n\n{startlang} -> {laststring}{getlangword()}")
    pyperclip.copy(finalword.text)
    if getsimilarity():
        input(f"Original: {startword}\nTranslated: {finalword.text}\nSimilarity: {fuzz.ratio(startword, finalword.text)}%\n")
    else:
        input(f"{finalword.text}\n")
    choose()


def translate():
    ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Phrase Translate')
    langs = []
    clear()
    num = getlangs()
    if getseedinput():
        seed = input("Seed: ").encode(encoding='utf-8')
        if not str(seed).isnumeric():
            hashed = hashlib.md5(seed).hexdigest()
            seed = int(''.join([n for n in hashed if n.isdigit()]))
        random.seed(seed)
    word = input("Phrase: ")
    if word == "":
        choose()
    startlang = LANGUAGES[translator.detect(word).lang].title()
    startword = word
    laststring = ""
    for i in range(num):
        languageindex = random.randrange(0, 104)
        language = languages[languageindex]
        langs += [language]
        try:
            word2 = translator.translate(word, dest=language)
        except:
            input("You are ratelimited! Wait a while or use a VPN/proxy.")
            choose()
        print(f"{LANGUAGES[language].title()}: {word2.text}")
        word = word2.text
        sleep(getdelay())
    try:
        finalword = translator.translate(word, dest=getlang())
    except:
        input("You are ratelimited! Wait a while or use a VPN/proxy.")
        choose()
    for i in langs:
        laststring += LANGUAGES[i].title() + " -> "
    print(f"\n\n\n\n\n{startlang} -> {laststring}{getlangword()}")
    pyperclip.copy(finalword.text)
    if getsimilarity():
        input(f"Original: {startword}\nTranslated: {finalword.text}\nSimilarity: {fuzz.ratio(startword, finalword.text)}%\n")
    else:
        input(f"{finalword.text}\n")
    choose()


def settings():
    ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Settings')
    clear()
    type2 = input("(1) Change language\n(2) Set delay between translations\n(3) Set language amount\n(4) Allow seed input\n(5) Show similarity\n(6) View settings\n(7) Help\n(8) Exit\n")
    if type2 == "1":
        clear()
        ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Change Language')
        language = input(
            "(1) English\n(2) Czech\n(3) Slovak\n(4) German\n(5) French\n(6) Russian\n(7) Croatian\n(8) Polish\n(9) Exit\n")
        with open('settings.json') as f:
            data = json.load(f)
        langu = data['language']
        if language == "1":
            prefix = "en"
        elif language == "2":
            prefix = "cs"
        elif language == "3":
            prefix = "sk"
        elif language == "4":
            prefix = "de"
        elif language == "5":
            prefix = "fr"
        elif language == "6":
            prefix = "ru"
        elif language == "7":
            prefix = "hr"
        elif language == "8":
            prefix = "pl"
        elif language == "9":
            choose()
        lang = LANGUAGES[prefix].title()
        if langu == prefix:
            input(f"Your language is already set to {lang}.\n")
        else:
            data['language'] = prefix
            data['languageword'] = lang
            rewrite = open("settings.json", "w")
            json.dump(data, rewrite)
            rewrite.close()
            input(f"Successfully changed language to {lang}.\n")
        choose()
    elif type2 == "2":
        ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Change Delay')
        clear()
        try:
            delay = int(input("What do you want to set as the delay? A bigger delay might help with ratelimiting.\n"))
        except ValueError:
            choose()
        else:
            with open('settings.json') as f:
                data = json.load(f)
            olddelay = data['delay']
            if delay == olddelay:
                input(f"Delay is already set to {delay}.\n")
            else:
                data['delay'] = delay
                rewrite = open("settings.json", "w")
                json.dump(data, rewrite)
                rewrite.close()
                input(f"Successfully changed delay to {delay}.\n")
            choose()
    elif type2 == "3":
        ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Change Language Amount')
        clear()
        try:
            langs = int(
                input("What do you wanna set as the language amount? A smaller number might help with ratelimiting.\n"))
        except ValueError:
            choose()
        if langs > 50:
            yn = input(f"Language amount can't be set to a larger number than 50. Do you want to set it to 50? (Y/N)\n").upper()
            if yn == "Y":
                with open('settings.json') as f:
                    data = json.load(f)
                data['languages'] = 50
                rewrite = open("settings.json", "w")
                json.dump(data, rewrite)
                rewrite.close()
                input(f"Successfully changed language amount to 50.\n")
                choose()
            else:
                choose()
        else:
            with open('settings.json') as f:
                data = json.load(f)
            oldlangs = data['languages']
            if langs == oldlangs:
                input(f"Language amount is already set to {langs}.\n")
            else:
                data['languages'] = langs
                rewrite = open("settings.json", "w")
                json.dump(data, rewrite)
                rewrite.close()
                input(f"Successfully changed language amount to {langs}.\n")
            choose()
    elif type2 == "4":
        clear()
        ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Allow Seed Input')
        yn = input(f"Do you want to be able to set a seed every translation? (Y/N)\n").upper()
        if yn == "Y":
            setseed = True
            with open('settings.json') as f:
                data = json.load(f)
            oldseed = data['seedinput']
            if oldseed == setseed:
                input("You already have seed input turned on.\n")
                choose()
            data['seedinput'] = True
            rewrite = open("settings.json", "w")
            json.dump(data, rewrite)
            rewrite.close()
            input(f"Successfully turned seed input on.\n")
        elif yn == "N":
            setseed = False
            with open('settings.json') as f:
                data = json.load(f)
            oldseed = data['seedinput']
            if oldseed == setseed:
                input("You already have seed input turned off.\n")
                choose()
            data['seedinput'] = False
            rewrite = open("settings.json", "w")
            json.dump(data, rewrite)
            rewrite.close()
            input(f"Successfully turned seed input off.\n")
        choose()
    elif type2 == "5":
        ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Show Similarity')
        clear()
        yn = input(f"Do you want to show similarity? (Y/N)\n").upper()
        if yn == "Y":
            similarity = True
            with open('settings.json') as f:
                data = json.load(f)
            oldsimilarity = data['similarity']
            if similarity == oldsimilarity:
                input("You already have similarity turned on.\n")
                choose()
            data['similarity'] = True
            rewrite = open("settings.json", "w")
            json.dump(data, rewrite)
            rewrite.close()
            input(f"Successfully turned similarity on.\n")
        elif yn == "N":
            similarity = False
            with open('settings.json') as f:
                data = json.load(f)
            oldsimilarity = data['similarity']
            if similarity == oldsimilarity:
                input("You already have similarity turned off.\n")
                choose()
            data['similarity'] = False
            rewrite = open("settings.json", "w")
            json.dump(data, rewrite)
            rewrite.close()
            input(f"Successfully turned similarity off.\n")
        choose()
    elif type2 == "6":
        ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | View Settings')
        clear()
        input(f"(1) Language Prefix: {getlang()}\n"
              f"(2) Language: {getlangword()}\n"
              f"(3) Delay: {getdelay()}\n"
              f"(4) Language amount: {getlangs()}\n"
              f"(5) Seed input: {'ON' if getseedinput() else 'OFF'}\n"
              f"(6) Similarity: {'ON' if getsimilarity() else 'OFF'}\n")
        choose()
    elif type2 == "7":
        ctypes.windll.kernel32.SetConsoleTitleW('Fuck-It-Up Translator | Settings Help')
        clear()
        input("(1) Language - Output language\n"
              "(2) Delay - Delay between translations\n"
              "(3) Language amount - The amount of languages to translate to. Limited to 50.\n"
              "(4) Seed - Allows you to always generate the same languages.\n"
              "(5) Similarity - Compares the starting phrase with the output phrase in percentage.\n")
        choose()
    else:
        choose()


choose()
