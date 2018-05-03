# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:
def clean_message(message):
    '''(str) -> str 
    REQ: message contains only 1 line of text. 
    REQ: len(message) > 0
    
    >>> clean_message('fighting,.,.,.,!!Easy5747291---=nvm...')
    'FIGHTINGEASYNVM'
    
    >>> clean_message('........................................')
    ''
    
    >>> clean_message('$$$$money is nothing^^%#@. This system is broken.')
    'MONEYISNOTHINGTHISSYSTEMISBROKEN'
    
    >>> clean_message('                         ')
    ''
    Return a copy of the message that includes only the aplhabetical 
    characters of the original message, where each character has been
    changed to uppercase.
    '''
    removed_spaces = message.replace(' ','')
    changed_copy_of_message = ''
    idx_value = 0
    # Find any sings of int or any other type not acceptable
    for letters in removed_spaces:
        if (letters[idx_value].isalpha()):
            changed_copy_of_message += letters
    return changed_copy_of_message.upper()
            
def encrypt_letter(single_char, keystream_value):    
    '''(str, int) -> str
       REQ:  0 < value <= 26 
       REQ: single_char must only be a single alphabetical character, 
       in which len(single_char) == 1.
       
       >>> encrypt_letter('b', 2)
       'D'
       
       >>> encrypt_letter('B', 2)
       'D'
       
       >>> encrypt_letter('A', 15)
       'P'
       
       Return the encription of the character after the keystream value 
       has been applied to the character. 
       '''
    # Make the single character upper 
    single_char_upper = clean_message(single_char)
    # check if single_char is Upper:
    value_of_char = ord(single_char_upper) - 65
    encripted_vlue = value_of_char + keystream_value 

    if (encripted_vlue > 25):
        encripted_vlue -= 26 
        encripted_vlue = chr(encripted_vlue + 65)     
    else:
        encripted_vlue = chr(encripted_vlue + 65) 
        
    return encripted_vlue


def decrypt_letter(single_char, keystream_value):
    '''(str, int) -> str
    REQ:  0 < value <= 26 
    REQ: single_char must only be a single UPPERCASE alphabetical character, 
    in which len(single_char) == 1.
    
    >>> decrypt_letter('I', 8)
    'A'
    
    >>> decrypt_letter('X', 12)
    'L'
    
    >>> decrypt_letter('M', 14)
    'Y'
    
    Return the encription of the character after the keystream value 
    has been applied to the character. 
    '''
    # Subtract the 2 values:
    value_of_char = ord(single_char) - 65
    decripted_vlue = value_of_char - keystream_value
    
    if single_char.isupper():
        if (decripted_vlue < 0): 
            decripted_vlue = chr((decripted_vlue + 65) + 26)
        
        else:
            decripted_vlue = chr(decripted_vlue + 65)
            
        return decripted_vlue
    
    
def swap_cards(deck_of_crds, index):
    '''
    (list of int, int) -> NoneType
    REQ: len(d_of_crds) >= 1
    REQ: 0 < index < len(d_of_crds) 
    
    >>> swap_cards([1,2,4,6], 2)
    [1,2,6,4]
    
    >>> swap_cards([1,2,4,5,6,7,8,9,10,12,21], 10)
    [21, 2, 4, 5, 6, 7, 8, 9, 10, 12, 1]
    
    Return the swap of the card at the given index with the card that 
    follows it. 
    If the card at the given index is on the bottom of the deck, swap 
    that card with the top card.
    '''
    # check if the given index is the last index in the deck.
    if (index == (len(deck_of_crds) -1)):
        
        # Find the value at first and last index
        last_value = deck_of_crds.pop(index)
        first_value = deck_of_crds.pop(0)
        
        # Swap first and last index values
        deck_of_crds.insert(0, last_value)
        deck_of_crds.insert(index, first_value)
        
    else:
        # Swap any value with the next index value
        any_value = deck_of_crds.pop(index)
        deck_of_crds.insert(index+1, any_value)

def move_joker_1(deck_of_crds):
    '''
    (list of int) -> NoneType
    REQ: JOKER1 in deck_of_crds
    REQ: len(deck_of_crds) >= 2
    
    >>> move_joker_1([1,2,4,27,6])
    [1,2,4,6,27]
    
    >>> move_joker_1([1,2,4,6,27])
    [27,2,4,6,1]
    
    >>> move_joker_1([2,27])
    [27,2]

    Return the swap of JOKER1 with the card that follows it. 
    If JOKER1 is on the bottom of the deck, swap JOKER1 with the top card.
    '''
    if (JOKER1 in deck_of_crds):
        # Find what index JOKER1 lies in deck_of_crds  
        joker_1_index = deck_of_crds.index(JOKER1)
        # Using swap_cards, change JOKER1's position to the next card. 
        swap_cards(deck_of_crds, joker_1_index)
    
    
def move_joker_2(deck_of_crds):
    '''
    (list of int) -> NoneType
    REQ: JOKER2 in deck_of_crds
    REQ: len(deck_of_crds) >= 2
    
    >>> move_joker_2([1,2,4,28,6])
    [28,2,4,6,1]
    
    >>> move_joker_2([28,2,4,6,1])
    [2,4,28,6,1]
    
    >>> move_joker_2([2,4,28,6,1])
    [2,4,6,1,28]
    
    >>> move_joker_2([28,2])
    [28,2]
    
    Return the swap of JOKER2, after it has moved two cards down. If
    JOKER2 is at the bottom of the deck, then swap it with the top card.
    '''
    # Find JOKER2's index in deck_of_crds   
    joker_2_index = deck_of_crds.index(JOKER2)
    # Using swap_cards function, swap JOKER2's position with next card
    swap_cards(deck_of_crds, joker_2_index)
    # Store the first swapped list in a new variable 
    after_frst_swap = deck_of_crds
    # Find JOKER2's index in deck_of_crds, in order to swap it once again.
    joker_2_position_2 = deck_of_crds.index(JOKER2)
    # Swap the already swapped list, once more in order to move JOKER2
    # one more time.
    swap_cards(after_frst_swap, joker_2_position_2)

       
def triple_cut(deck_of_crds):
    '''
    (list of int) -> NoneType
    REQ: Both JOKER1 and JOKER2 are in deck_of_crds
    REQ: len(deck_of_crds) >= 2
    
    >>> triple_cut[28,27]
    [28,27]
    
    >>> triple_cut([28,2,4,6,27])
    [28, 2, 4, 6, 27]
    
    >>> triple_cut([2,3,4,28,27,6,5])
    [6, 5, 28, 27, 2, 3, 4]
    
    >>> triple_cut([28,27,2,3])
    [2,3,28,27]
    
    >>> triple_cut([2,3,4,28,27])
    [28,27,2,3,4]
    
    >>> triple_cut([3,4,5,27,8,11,28,13,15])
    [13, 15, 27, 8, 11, 28, 3, 4, 5]
    
    >>> triple_cut([27,1,2,3,28,6])
    [6, 27, 1, 2, 3, 28]
    
    >>> triple_cut([1,27,3,4,28,9,10])
    [9, 10, 27, 3, 4, 28, 1]
    
    Return the list in which everything above the first joker goes at the 
    bottom of deck of cards, and everything below the second goes to the top.
    '''
    # Find at which index JOKER1 and JOKER2 lie, in deck of cards
    index_joker_1 = deck_of_crds.index(JOKER1)
    index_joker_2 = deck_of_crds.index(JOKER2)
    counter = 0
    # Check if JOKER1 comes before JOKER2
    if (index_joker_1 < index_joker_2):
        # if True then go through all the index values before JOKER1's idx
        while(counter < index_joker_1):
            # Store the values before JOKER1
            values_bfr_JOKER1 = deck_of_crds.pop(0)
            # Insert the values before JOKER1, after JOKER2
            deck_of_crds.insert(index_joker_2, values_bfr_JOKER1)
            counter +=1
        
        # Find the last index number and store it     
        last_index_vlue = (len(deck_of_crds) -1)
        # Check if JOKER2 occurs at the bottom of the deck of cards 
        while (index_joker_2 < last_index_vlue):
            # If True, then store all the index values before JOKER1
            values_bfr_JOKER1 = deck_of_crds.pop()
            # Insert all the values before JOKER1, to the top of the card
            deck_of_crds.insert(0, values_bfr_JOKER1)
            last_index_vlue -= 1    
    # If JOKER2 occurs before JOKER1        
    elif (index_joker_1 > index_joker_2):
        counter =0
        # If true, then go through all the index values before JOKER2's idx
        while(counter < index_joker_2):
            # store all values before JOKER1.
            values_bfr_JOKER1 = deck_of_crds.pop(0)
            # Insert those values before JOKER1
            deck_of_crds.insert(index_joker_1, values_bfr_JOKER1)
            counter +=1
         
        # Find the last index number and store it             
        last_idx_vlue = (len(deck_of_crds) -1)
        while (index_joker_1 < last_idx_vlue):
            # Store the values before JOKER1 and place them at top of deck.
            values_bfr_JOKER1 = deck_of_crds.pop()
            deck_of_crds.insert(0, values_bfr_JOKER1)
            last_idx_vlue -= 1
            
                
def insert_top_to_bottom(deck_of_crds):
    '''(list of int) -> NoneType
    REQ: len(deck_of_crds) > 0
    REQ: len(deck_of_crds) >= len(of the last card in the deck)
    >>> insert_top_to_bottom([1,2,3,4])
    [1,2,3,4]
    >>> insert_top_to_bottom([23,26,27,2,3])
    [2,23,26,27,3] 
    
    Look at the bottom card of the deck, move that many cards from  top of  
    deck to the bottom, inserting them just above the bottom card. If the 
    bottom card is JOKER2, use JOKER1 as the number of cards.
    '''
    index = len(deck_of_crds)
    value = deck_of_crds[index -1] 
    
    # dont change the deck, if the last card has value which is greater than
    # or equal to the len of deck of cards
    if (value >= index):
        pass # dont change anything
        
    # if value is equal to JOKER2, then use JOKER1 value     
    elif (value == JOKER2):
        value = JOKER1
        counter = 0
        # loop through deck of cards and find 
        while counter < value:
            cards_to_move = deck_of_crds.pop(0)
            deck_of_crds.insert(value, cards_to_move)
            counter+=1
    
    # IF the last card is not JOKER2, then:
    else:
        counter = 0
        while counter < value:
            # Find all the cards that need to be moved from top to bottom.
            cards_to_move = deck_of_crds.pop(0)
            # Insert those cards into the given index
            deck_of_crds.insert(len(deck_of_crds)-1, cards_to_move)
            counter+=1   
     
       
def get_card_at_top_index(deck_of_crds):
    '''(list of int) -> int
    REQ: len(deck_of_crds) > 0 
    REQ: 
    >>> get_card_at_top_index ([1,2,3,4])
    2
    
    >>> get_card_at_top_index([1,2,3,23,24,26])
    2
    
    >>> get_card_at_top_index([2,3,23,24,26])
    23
    
     Using the top card value as an index, return the card in that deck 
     at that index. If the top card is JOKER2, use JOKER1 
     as the index.
    '''
    # find what lies at the first index
    first_index = deck_of_crds[0]
    # if that value is JOKER2, then:
    if (first_index == JOKER2):
        # if JOKER1 is greater than length of deck
        if (JOKER1 >= len(deck_of_crds)):
            # Dont return anything
            return 
    # If the first value is greater than length of deck, then dont do anything    
    elif(first_index >= len(deck_of_crds)):
        return 
    # Else, then return the card at the index. 
    else:
        return deck_of_crds[first_index]
       
def get_next_value(deck_of_crds):
    '''(list of int) -> int
    REQ: len(deck_of_crds) > 0
    REQ: FIle contains JOKER1 and JOKER2 
    >>> get_next_value([1 ,4 ,7 ,10 ,13 ,16 ,19 ,22 ,25 ,28 ,3, 6, 9 ,
    12 ,15 ,18 ,21 ,24 ,27, 2, 5, 8 ,11 ,14 ,17 ,20 ,23, 26]}
    11
    
    Return the next potential keystream value.
    '''
    # Call all the functions
    move_joker_1(deck_of_crds)
    move_joker_2(deck_of_crds)
    triple_cut(deck_of_crds)
    insert_top_to_bottom(deck_of_crds)
    next_keystream_value = get_card_at_top_index(deck_of_crds)
    return next_keystream_value

def get_next_keystream_value(deck_of_crds):
    '''(list of int) -> int
    REQ: len(deck_of_crds) > 0
    
    >>> get_next_keystream_value([1 ,4 ,7 ,10 ,13 ,16 ,19 ,22 ,25 ,28 ,3, 6, 
    9 ,12 ,15 ,18 ,21 ,24 ,27, 2, 5, 8 ,11 ,14 ,17 ,20 ,23, 26])
    11
    '''
    # RERUN ALL 5 STEPS BY CALLING get_next_value
    next_keystream_value = get_next_value(deck_of_crds)
    value_is_joker = True
    # Run if there is a joker found
    while (value_is_joker == True):
        # Get a new keystream value
        if (next_keystream_value == JOKER1 or next_keystream_value == JOKER2):
            next_keystream_value = get_next_keystream_value(deck_of_crds)
            return (next_keystream_value)
        else:
            # If no joker found, then return value
            value_is_joker == False
            return next_keystream_value 
        
        
def process_message(deck_of_crds, message, enc_or_dec):
    '''(list of int, str, str) -> str
    REQ: len(deck_of_crds) > 0
    REQ: len of message > 0
    REQ: enc_or_dec == 'e' or 'd'
    '''
    clnd_message = clean_message(message)
    
    counter =0
    x = ""
    # Generate different key_stream_values for each message
    for letters in clnd_message:
        # Store the keystream values
        key_stream_value = get_next_keystream_value(deck_of_crds)
        # Check if the user wants to encript
        if (enc_or_dec == 'e'):
            # Store the encripted messages
            holder += encrypt_letter(letters[counter], key_stream_value)
        
    # If the user wants to decrypt        
        elif (enc_or_dec == 'd'):
            # Hold all the decripted values in a variable and return it.
            holder += decrypt_letter(letters[counter], key_stream_value)
    return holder
            
            
def process_messages(deck_of_crds, list_of_messages, enc_or_dec):
    '''
    REQ: len(deck_of_crds) > 0
    REQ: len(list_of_messages) > 0
    REQ: enc_or_dec must be strictly equal to 'e' or 'd'
    
    >>> process_messages([1,2,3,4,5,27,28],['Hello','134405584'],'e')
    
    '''
    list_of_str = list()
    for words in list_of_messages:
        list_of_messages = process_message(deck_of_crds, words,
                                           enc_or_dec)
        # Add all the encripted or decripted values in one list by appending
        list_of_str.append(list_of_messages)
    return list_of_str
        

def read_messages(file):
    '''(file open for reading) -> list of str
    REQ: One line holds only a single message
    REQ: len(file) > 0
    
    Return contents of file as a list of messages, which is a list of str. 
    This is done by stripping the newline from each line.
    '''
    list_of_str = list()
    hold_changed_file = ''
    # Read all the lines in the file
    file = file.readlines()
    for words in file:
        # Remove all the spaces in the file, to read the line as a single str
        hold_changed_file = words.strip('\n')
        # Store all the single str's into a list of strings. 
        list_of_str.append(hold_changed_file)
    return list_of_str

    
def read_deck(file):
    '''(file open for reading) -> list of int
    REQ: len(file) > 0
    REQ: file must contain atleast 1 line, and must all be int
    
    Read and return the contents of the file as a list of int.
    ''' 
    counter = 0
    # create a empty list
    list_of_str = list()
    # Read through all the lines in the file
    file = file.readlines()
    for numbers in file:
        # Split all the numbers at the spaces and split them into a list of str
        list_of_str += numbers.split()
    # hold the list_of_str
    hold = list_of_str 
    # Change the list of str to list of int and return
    for counter in range(len(hold)):
        hold[counter] = int(hold[counter])
    return hold
    
    
        


    

        

    
    
    
        
        
        
        
        
        
    
    