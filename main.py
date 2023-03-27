# Import libraries
import os
import sumy
import wikipedia
import pyttsx3

import nltk

from sumy.parsers.plaintext import PlaintextParser

from sumy.nlp.tokenizers import Tokenizer
# Init speech engine
from sumy.summarizers.lex_rank import LexRankSummarizer
converter = pyttsx3.init()

# Set properties of speech engine before it starts and set speech rate
speaker_rate = 142
converter.setProperty('rate', speaker_rate)
# Set volume of speech
converter.setProperty('volume', 0.7)
# Set voice of speech
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
converter.setProperty('voice', voice_id)


def research_and_sum():
    # This lets the user know what the program is doing
    print("\n\nHello, my name is David. I will be your guide to the world of research.\n")
    converter.say("Hello, my name is David. I will be your guide to the world of research.")
    converter.runAndWait()
    # This asks the user how many topics they want to research
    print("\n\nHow many topics would you like to research? \n")
    converter.say("How many topics would you like to research?")
    converter.runAndWait()
    research_amount = int(input())
    # Creates a var that allows the while loop to understand how many times it should repeat
    x = 0
    while x < research_amount:
        # This gets the user's input to search for a topic
        print("\n\nWhat would you like me to research for you? \n")
        converter.say("What would you like me to research for you?")
        converter.runAndWait()
        user_topic = input()
        raw_research = wikipedia.summary(user_topic, sentences=3)
        # This displays a line for a better user experience
        print("_" * 50)
        print("\n\n")
        # Wikipedia API call
        wiki_page = wikipedia.page(user_topic)
        # output research
        converter.say("Researching: " + user_topic)
        print("Your research on " + user_topic + " is as follows: ")
        print()
        print("*" * 60)
        print(raw_research)
        print("*" * 60)
        print()
        # This displays the references of the topic the user wants to research
        print(wiki_page.references)
        # This displays a line for a better user experience
        print("_" * 50)
        # Saves the users inputs
        # Writes data to a text file
        # If it does not exist it creates a file
        Research = open("data_save.txt", "a")
        # Write some stuff to the file
        # Use the file object, not the file name to handle the file
        Research.write(wiki_page.title + "\n" + wiki_page.summary + "\n\n")
        # Close the file right away
        Research.close()
        # Adds 1 to var x until the while loop has looped the amount of times the user wanted
        x += 1
    # Summarizes all data together
    Research = open("data_save.txt", "r")
    data = Research.read()
    Research.close()
    print(data)

    parser = PlaintextParser.from_string(data, Tokenizer("english"))

    summarizer = LexRankSummarizer()
    NumOfSentence = 9
    summary = summarizer(parser.document, NumOfSentence)
    print("Here is your summary!\n")
    converter.say("Here is your summary!")
    converter.runAndWait()
    for sentence in summary:
        print(sentence)
        converter.say(sentence)
        converter.runAndWait()
    return summary


def main():
    research_and_sum()


if __name__ == "__main__":
    main()
