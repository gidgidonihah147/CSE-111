#-------------------WEEK 03-------------------
# Purpose
# Prove that you can write functions with parameters and call those functions multiple times with arguments.

# Problem Statement
# The Turing test, named after Alan Turing, is a test of a computer’s ability to make conversation that is indistinguishable from human conversation. A computer that could pass the Turing test would need to understand sentences typed by a human and respond with sentences that make sense.

# In English and many other languages, grammatical quantity (also known as grammatical number) is an attribute of nouns, pronouns, adjectives, and verbs that expresses count distinctions, such as “one”, “two”, “some”, or “many”. The grammatical quantity of the words in a sentence must match. In English, there are two categories of grammatical quantity: single and plural. For example, here are three English sentences that contain single nouns, pronouns, and verbs:

# The boy laughs.
# One dog eats.
# She drinks water.
# Here are three English sentences that contain plural nouns, pronouns, and verbs:

# Two birds fly.
# Some animals eat.
# Many cars drive.
# Grammatical tense is an attribute of verbs that expresses when an action happened. Many languages include past, present, and future tenses. For example, here are three English sentences, the first with past tense, the second with present tense, and the third with future tense:

# The cat walked.
# The cat walks.
# The cat will walk.
# Assignment
# Write a Python program named sentences.py that generates simple English sentences. During this prove milestone, you will write functions that generate sentences with three parts:

# a determiner (sometimes known as an article)
# a noun
# a verb
# For example:

# A cat laughed.
# One man eats.
# The woman will think.
# Some girls thought.
# Many dogs run.
# Many men will write.
# For this milestone, your program must include at least these five functions:

# main
# make_sentence
# get_determiner
# get_noun
# get_verb
# You may add other functions if you want. The functions get_determiner, get_noun, and get_verb, must randomly choose a word from a list of words and return the randomly chosen word. All the functions that you must write for this milestone assignment are described in the Steps section below.

#-------------------WEEK 04-------------------
# Problem Statement
# In English, a preposition is a word used to express spatial or temporal relations, such as “in”, “over”, and “before”. A prepositional phrase is group of words that begins with a preposition and includes a noun. For example:

# above the water
# in the kitchen
# after the meeting
# Assignment
# Write the second half of a Python program that generates simple English sentences that you began in the previous lesson’s prove milestone. As part of the previous lesson’s prove milestone, you wrote a program that generates English sentences with three parts: a determiner, a noun, and a verb. During this prove assignment, you will add functions so that your program generates sentences with four parts:

# a determiner
# a noun
# a verb
# a prepositional phrase
# For example:

# One girl talked for the car.
# A bird drinks off one child.
# The child will run on the car.
# Some dogs drank above many rabbits.
# Some children laugh at many dogs.
# Some rabbits will talk about some cats.
# To complete this prove assignment, your program must include at least these seven functions:

# main
# make_sentence
# get_determiner
# get_noun
# get_verb
# get_preposition
# get_prepositional_phrase
# You may add other functions if you find them helpful. The get_preposition function must randomly choose a preposition from a list and return the randomly chosen preposition. The get_prepositional_phrase function must make a prepositional phrase by calling the get_preposition, get_determiner, and get_noun functions.

 #Week 03 Assignment
import random

 #Week 03 Assignment
def main():
    #Looping through make_sentence with each of the different versions of the sentence. Only using 1 variable as we can replace the value each time. #Week 03 Assignment
    sentence = make_sentence(1, "past")
    print(sentence)
    sentence = make_sentence(1, "present")
    print(sentence)
    sentence = make_sentence(1, "future")
    print(sentence)
    sentence = make_sentence(2, "past")
    print(sentence)
    sentence = make_sentence(2, "present")
    print(sentence)
    sentence = make_sentence(2, "future")
    print(sentence)
    
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    #Output either a single or multiple based on the quantity #Week 03 Assignment
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner. #Week 03 Assignment
    word = random.choice(words)
    return word

 #Week 03 Assignment
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    #Output either a single or multiple based on the quantity #Week 03 Assignment
    if quantity ==1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a determiner. #Week 03 Assignment
    noun = random.choice(nouns)
    return noun

 #Week 03 Assignment
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    #Output a different verb list to be random chosen based on the tense chosen #Week 03 Assignment
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    # Randomly choose and return a determiner.
    verb = random.choice(verbs)
    return verb

 #Week 04 Assignment
def get_preposition():
    """Return a randomly chosen preposition from this list of prepositions:
    "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition."""
    prep_words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    word = random.choice(prep_words)
    return word

 #Week 04 Assignment
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three words: a preposition, a determiner, and a noun by calling the get_preposition, get_determiner, and get_noun functions.
    Parameter
        quantity: an integer that determines if the determiner and noun in the prepositional phrase returned from this function should be single or pluaral.
    Return: a prepositional phrase."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_preposition()
    phrase = (f"{preposition} {determiner} {noun}")
    return phrase

#Week 03 Assignment
def make_sentence(quantity, tense):
    """Build and return a sentence with three words: a determiner, a noun, and a verb. The grammatical quantity of the determiner and noun will match the number in the quantity parameter. The grammatical quantity and tense of the verb will match the number and tense in the quantity and tense parameters."""
    #Combine all the other functions that have been created to output a sentence #Week 03 Assignment
    sentence = f"{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)} {get_prepositional_phrase(quantity)}."
    return sentence


 #Week 03 Assignment
main()