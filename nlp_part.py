from nltk import word_tokenize, pos_tag


def processData(sentence):
    
    #sentence = input("Enter something: ")
    tokens = word_tokenize(sentence)
    posTaggedList = pos_tag(tokens)
    #print("Sentence : ", sentence)
    print("Tokens : ", tokens)
    print("Parts of speech : ", posTaggedList)

    noun = []
    verb = []
    determiner= []
    adjective = []
    adverb = []
    particle = []
    pronoun = []
    to = [] 
    modal = []
    preposition = []

    for tuple in posTaggedList:
        if tuple[1] == 'NNP':
            noun.append(tuple[0])
        if tuple[1] == 'NNS':
            noun.append(tuple[0])
        if tuple[1] == 'NNPS':
            noun.append(tuple[0])
        if tuple[1] == 'VBZ':
            verb.append(tuple[0])
        if tuple[1] == 'VBN':
            verb.append(tuple[0])
        if tuple[1] == 'VBP':
            verb.append(tuple[0])
        if tuple[1] == 'VB':
            verb.append(tuple[0])
        if tuple[1] == 'VBD':
            verb.append(tuple[0])
        if tuple[1] == 'VBG':
            verb.append(tuple[0])
        if tuple[1] == 'NN':
            noun.append(tuple[0])
        if tuple[1] == 'DT':
            determiner.append(tuple[0])
        if tuple[1] == 'WDT':
            determiner.append(tuple[0])
        if tuple[1] == 'PDT':
            determiner.append(tuple[0])
        if tuple[1] == 'JJ':
            adjective.append(tuple[0])
        if tuple[1] == 'JJR':
            adjective.append(tuple[0])
        if tuple[1] == 'JJS':
            adjective.append(tuple[0])
        if tuple[1] == 'RB':
            adverb.append(tuple[0])
        if tuple[1] == 'RBR':
            adverb.append(tuple[0])
        if tuple[1] == 'WRB':
            adverb.append(tuple[0])
        if tuple[1] == 'RBS':
            adverb.append(tuple[0])
        if tuple[1] == 'RP':
            particle.append(tuple[0])
        if tuple[1] == 'PRP':
            pronoun.append(tuple[0])
        if tuple[1] == 'POS':
            pronoun.append(tuple[0])
        if tuple[1] == 'PRP$':
            pronoun.append(tuple[0])    
        if tuple[1] == 'WP$':
            pronoun.append(tuple[0])
        if tuple[1] == 'WP':
            pronoun.append(tuple[0])
        if tuple[1] == 'TO':
            to.append(tuple[0])
        if tuple[1] == 'MD':
            modal.append(tuple[0])
        if tuple[1] == 'IN':
            preposition.append(tuple[0])
        
        

            
    print("Nouns : ", noun)
    print("Verb : ", verb)
    print("Determiners : ", determiner)
    print("Adjectives : ", adjective)
    print("Adverbs : ", adverb)
    print("Pronouns : ", pronoun)
    print("Particles : ", particle)
    print("Tos : ", to)
    print("Modals : ", modal)
    print("Prepositions : ", preposition)

    return noun[0], verb[0], noun[1]
    #return noun[0], verb[0], verb[1], verb[2], verb[3], verb[4], verb[5], noun[1], noun[2], noun[3], determiner[0], determiner[1], determiner[2], adjective[0], adjective[1], adjective[2], adverb[0], adverb[1], adverb[2], adverb[3], modal[0], to[0], preposition[0], particle[0], pronoun[0], pronoun[1], pronoun[2], pronoun[3], pronoun[4], pronoun[5]