# File to practice python datatypes

def getStringLength(abc):
    i = 0
    for a in abc:
        i += 1

    return i

def getCharacterFrequency(abc):
    frequency_dict = {}

    for a in abc:
        if (a in frequency_dict.keys()):
            frequency_dict[a] += 1
        else:
            frequency_dict[a] = 0

    return frequency_dict

def getFirstAndLastTwoChars(abc):
    if len(abc)<2:
        return ""
    else:
        return (abc[0:2] + abc[-2:])

def replaceRecurringChar(abc):
    result=[]

    for a in abc:
        if (a in result) and (a != " "):
            result.append("$")
        else:
            result.append(a)

    return "".join(result)

def swapFirstTwoCharsOfStrings(x,y):
    first_string = x[:2] + y[2:]
    second_string = y[:2] + x[2:]
    return (first_string + " " + second_string)

def addIngToString(a):
    if len(a) < 3:
        return " "
    else:
        if a[-3:] == "ing":
            return (a + "ly")
        else:
            return (a + "ing")

# replace words with 'not poor' with good
def replaceWords(a):
    list1 = a.split(" ")
    notindex = None

    if "not" in list1:
        notindex = list1.index("not")
        for i in range(notindex,len(list1)):
            if list1[i] == "poor":
                list1.insert(i+1,"good")
                while list1[notindex] != "good":
                    list1.pop(notindex)
            else:
                next
        return " ".join(list1)
    else:
        return a

    # better solution
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1

def longest_string_from_list(list1):
    word = ""
    length = 0

    for a in list1:
        if len(a)>length:
            word = a
            length = len(a)
    
    return word,length

    # better solution?? not sure
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])

def remove_nth_character(abc, n):
    first_part = abc[:n]
    second_part = abc[n+1:]
    result = first_part + second_part
    return result


def exchange_first_and_last_chars (abc):
    result = abc[-1] + abc[1:-1] + abc[0]
    return result
print(exchange_first_and_last_chars("lmao"))