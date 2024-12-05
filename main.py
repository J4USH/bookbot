
def sort_on(dict):
    return dict["nums"]

def countWord(str):
    return len(str)

def dictList(dict):
    lists=[]
    for key in dict:
        dicts={}
        dicts["alpha"]=key
        dicts["nums"]=dict[key]
        lists.append(dicts)

    return lists

def countChars(strs):
    count={}
    for str in strs:
        str=str.lower()
        for i in str:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1

    return count

def printDict(dict):
    for key in dict:
        if key['alpha'].isalpha():
            print(f"The '{key['alpha']}' character was found {key['nums']} times")




def main():

    filepath="books/frankenstein.txt"
    print(f"--- Begin report of {filepath} ---")
    with open("books/frankenstein.txt") as f:
        fileContents=f.read()

    
    counts=countWord(fileContents.split())

    print(f"{counts} words found in the document\n")
    
    countChar=countChars(fileContents.split())
    Listdict=dictList(countChar)
    Listdict.sort(reverse=True, key=sort_on)
    printDict(Listdict)
    print("--- End report ---")




main()