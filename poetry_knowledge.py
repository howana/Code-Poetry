import pronouncing
import random
import pyttsx3
haiku = [[],[],[]]
textfile = open("words.txt","r")
previousWord = "cat"
words_string = textfile.read()
wordList = words_string.split(" ")
def Speak(haiku):
    engine = pyttsx3.init();
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-10)
    engine.setProperty('age', 10)
    engine.say(haiku)
    engine.runAndWait()

def claim(what):
    print what,

def think_of_a_haiku(listofLinestoWrite):
    for i in range(0,len(listofLinestoWrite)):
        syllableCount = 0
        oldSyllableCount = 0
        previousWord = "cat"
        line = listofLinestoWrite[i]
        while syllableCount < line:
            currentWord = wordList[random.randrange(0,len(wordList)-1)]
            currentWord_pronounceList = pronouncing.phones_for_word(currentWord)
            if currentWord == previousWord:
                #print "same word"
                continue
            if len(currentWord_pronounceList) == 0:
                #print "I found a word I don't know 1"
                continue
            else:
                new_s_count = pronouncing.syllable_count(currentWord_pronounceList[0])
                if new_s_count == oldSyllableCount and syllableCount != line-1:
                    #print "same syllables lol"
                    continue 
                if (new_s_count+syllableCount) <=line:
                    haiku[i].append(currentWord)
                    syllableCount +=new_s_count   
                    previousWord = currentWord
                    oldSyllableCount = new_s_count
                #print currentWord, new_s_count
    return haiku
