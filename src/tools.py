import sys
from .movie import Saga

try:
    debug = sys.argv[1]
except:
    debug=0

def Text_to_List(path:str,debug:str='') -> list:
    '''
    process text file to list
    '''
    if debug == '--debug':
        print(path)

    orderList=[]
    try:
       with open(path,'r',encoding="UTF-8") as f:
            line = f.readline()
            while line:
                if line.strip():
                   orderList.append(line.strip())
                line=f.readline()

            if debug =='--debug':
                print(orderList)
       return orderList

    except FileNotFoundError:
        print("Could not open/read file:", path)
        raise FileNotFoundError("The file isn't in the path or cannot be read")
        return list()


def SliceBaseTitle(title:str,debug:str='') -> str:
    '''
    if title = Star wars 2 return [Star wars,2]
    '''
    roman_numbers=['I','II','III','IV','V','VI','VII','VIII','IX','X']
    res = ''
    deleted = "not saga"
    try:
        elements = title.split(' ')

    except:
        raise ValueError("object cannot be slice")


    if debug == "--debug":
       print("List of words in title : ",elements)
    if elements[-1].isdigit():
        deleted =elements.pop(-1)
        if debug == "--debug":
            print("Episode : ",deleted)
    else:
        if elements[-1] in roman_numbers:
           deleted= elements.pop(-1)
           if debug == "--debug":
              print("Episode:",deleted)


    for ele in elements:
        res= res + ele + ' '
    return res.strip(),deleted





def OrderPrice(orderList:list = [],debug:str=''):
    '''
    Create Saga object per Saga, and sum all price gathered from saga objects

    '''
    sagaDict = {}  # {"Star wars" : Saga object, "Avatar" : Saga object}
    price = 0
    for movie in orderList:
        title,episode = SliceBaseTitle(movie,debug)

        if title not in sagaDict:
            sagaDict[title] = Saga(title = title, episode = episode,debug=debug)
        else:
            sagaDict[title].add_episode(episode=episode)

    if debug == "--debug":
        print("Dictionnary of movies per Saga {0}".format(sagaDict))
    for key in sagaDict:
        price = price + sagaDict[key].getPrice()
    return price
