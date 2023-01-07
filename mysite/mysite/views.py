from django.shortcuts import render
import re
user_text = ""
analyze_resutl = ""


def index_view(request):
    global analyze_resutl
    global user_text
    user_text = request.GET.get('inputText', "")
    user_choice = request.GET.get('choice', 'off')
    print(user_choice)
    print(user_text)
    print(analyze_resutl)
    if user_choice == "capitalize":
        analyze_resutl = capitalization()
    
    elif user_choice == "removespacesandlines":
        analyze_resutl = removeExtraSpacesAndLines()
    

    elif user_choice == "charcount":
        analyze_resutl = characterCounter()

    elif user_choice == "wordcount":
        analyze_resutl = wordCounter()

    result = {'analyzedText': analyze_resutl}
    print(result)
    return render(request, 'index.html', result)


def capitalization():
    myStrText = ""
    txt_storage = []
    for word in re.split(r'(\s+)', str(user_text)):
        txt_storage.append(word.capitalize())
    for joinString in txt_storage:
        myStrText += joinString
    return myStrText

def removeExtraSpacesAndLines():
    mystrList = user_text.split()
    return " ".join(mystrList)

def characterCounter():
    characterWithSpaces = len(user_text)
    characterWithOutSpaces = len(user_text.replace(" ", ""))
    finalResutl = f"Characters (no spcaces): {characterWithOutSpaces}\nCharacters (With Spaces): {characterWithSpaces}"
    strFinalResult = str(finalResutl)
    return strFinalResult

def wordCounter():
    list_userText = user_text.split()
    return len(list_userText)
