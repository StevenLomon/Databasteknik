from datetime import datetime

def getIntMenuInput(prompt: str, minValue: int, maxValue:int) -> int:
    while True:
        try:
            sel = int(input(prompt))
            if sel < minValue or sel > maxValue:
                print(f"Enter an integer between {minValue} and {maxValue}, please")
            else:
                break
        except:
            print("Invalid input. Try again, please")
    return sel

def sortNumbersList(inputList: list[float]) -> list: #I WILL USE THIS A LOT
    inputSorted = sorted(inputList)
    inputSorted.reverse()
    return inputSorted

#print(sortNumbersList([1.2, 3.55, 99, 60, 4.5]))

def isEvenLength(inputString: str) -> bool: 
    length = len(inputString)
    if length % 2 == 0:
        return True
    return False

def sortByLength(inputList: list[str]) -> list[str]:
    result = sorted(inputList, key=len) #Fucking MVP function
    return result

def convertToDatetime(date: str) -> datetime: #from format yyyy-mm-dd
    #date = str(date)
    year = int(date[0:4])
    mon = int(date[5:7])
    day = int(date[8:10])
    convDate = datetime(year, mon, day)
    return convDate

def getToday():
    today = datetime.date(datetime.now())
    return today

def getDatetime(lang:str, prompt:str = "Enter a date on the format yyyy-mm-dd, or 'today' for today's date: ") -> datetime:
    try:
        date = input(prompt)
        if date.lower() == 'today':
            return datetime.now()
        else:
            if len(date) != 10:
                if lang == "en":
                    print("Invalid input. Try again, please")
                    return
                elif lang == "sv":
                    print("Ogiltig inmatning. Försök igen, tack")
                    return
    except:
        if lang == "en":
            print("Invalid input. Try again, please")
        elif lang == "sv":
            print("Ogiltig inmatning. Försök igen, tack")
    return convertToDatetime(date)

