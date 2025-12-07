

#Alla vokaler:
vokaler = "aeiouyåäöAEIOUYÅÄÖ"

def is_vokal(letter):
    #om bokstaven är en vokal return True:
    return letter in vokaler


def is_konsonant(letter):
    #Om bokstaven inte är en vokal (eller bokstav alls)
    return letter.isalpha() and letter not in vokaler



    



