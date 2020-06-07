import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
#        pass #delete this line and replace with your code here
        assert (type(shift)== int),'shift must be an integer'
        if not shift >= 0 and shift < 26:
            raise IndexError
            return 
        else:
            
            
            shiftBy = shift
            lcAlpha = string.ascii_lowercase
            ucAlpha = string.ascii_uppercase
            localText = lcAlpha + ucAlpha
            keyDict ={}
            for i in localText:
                if i in lcAlpha:
                    encryptLoc = lcAlpha.index(i)-26+shiftBy
                    encryptKey = lcAlpha[encryptLoc]
                    keyDict[i]=encryptKey
                elif i in ucAlpha:
                    encryptLoc = ucAlpha.index(i)-26+shiftBy
                    encryptKey = ucAlpha[encryptLoc]
                    keyDict[i]=encryptKey
#                else:
#                    keyDict[i] = i 
                
            return keyDict
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
#        pass #delete this line and replace with your code here
        
        assert (type(shift)== int),'shift must be an integer'
        if not shift >= 0 and shift < 26:
            raise IndexError
            return 
        lcAlpha = string.ascii_lowercase
        ucAlpha = string.ascii_uppercase
        keyDict = self.build_shift_dict(shift)
        localText = self.get_message_text()
        localTextEncrypted=''
        for i in localText :
            if i in lcAlpha or i in ucAlpha:
                localTextEncrypted += keyDict[i]
            else:
                localTextEncrypted += i
        return localTextEncrypted
            

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
#        pass #delete this line and replace with your code here
        Message.__init__(self,text)
        self.shift = shift
        self.encrypting_dict = None
        self.message_text_encrypted = None
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        
        '''
        return self.shift
#        pass #delete this line and replace with your code here

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        
        '''
#        pass #delete this line and replace with your code here
      
        self.encrypting_dict  = self.build_shift_dict(self.get_shift())
        encrypting_dict = self.encrypting_dict 
        return encrypting_dict
        

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        
        '''
#        pass #delete this line and replace with your code here
       
        shift = self.get_shift()
        self.message_text_encrypted= self.apply_shift(shift)
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
#        pass #delete this line and replace with your code here
        self.shift = shift
        self.encrypting_dict = self.get_encrypting_dict()
        self.message_text_encrypted = self.get_message_text_encrypted()
        

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
#        pass #delete this line and replace with your code here
        Message.__init__(self,text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
#        pass #delete this line and replace with your code here
        
        key = self.search_for_shift()
        
        decrypted_text = self.apply_shift(26-key)
        
        
        
        return (26-key,decrypted_text)
        
        
        
        
    def word_counter(self,words):
        'counts the number of words in the text'
        wordCount = 0
        wordList = self.get_valid_words()
        for i in words:
            if is_word(wordList,i):
                wordCount +=1
        return wordCount
    
    def getkeyShift(self,max_words,num_words):
        for i in num_words:
            if num_words[i] == max_words:
                return i
    
    def search_for_shift(self):
        num_words = {}
        for i in range(1,27):
            shift = 26-i
            decrypted_text = self.apply_shift(shift)
            words = decrypted_text.split(' ')
            wordCount = self.word_counter(words)
            num_words[i]=wordCount
        max_words = max(num_words.values())
        key =self.getkeyShift(max_words,num_words)
        return key
                
            
        
        
        
   
        
        

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('I hate going to the barn on a sunny day', 5)
print('Expected Output: N mfyj ltnsl yt ymj gfws ts f xzssd ifd')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('N mfyj ltnsl yt ymj gfws ts f xzssd ifd')
#print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
