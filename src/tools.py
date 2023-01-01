import sys
from .movie import Saga



def Text_to_List(path:str,debug:str='') -> list:
    '''
    Transform text file to list
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


def SliceBaseTitle(title:str,debug:str='',mode:bool=False) -> str:
    '''
    if title = Star wars 2 return [Star wars,2]
    if title = Star wars II return  [Star wars,II]
    '''
    roman_numbers=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
    res = ''
    deleted = None
    try:
        elements = title.split(' ')

    except:
        raise ValueError("object cannot be slice")


    if debug == "--debug":
       print("Sliced title : ",elements)
    if elements[-1].isdigit():
        deleted =elements.pop(-1)
        if debug == "--debug":
            print("Episode number : ",deleted)
    else:
        if elements[-1] in roman_numbers:
           deleted= elements.pop(-1)
           if debug == "--debug":
              print("Episode number :",deleted)


    for ele in elements:
        res= res + ele + ' '
    res = res.strip()

    if mode == True:
        return res,deleted
    else:
        if res.lower() != "back to the future":
           return res.strip(),None
        else:
            return res.strip(),deleted





def OrderPrice(orderList:list = [],debug:str='',mode:bool=False):
    '''
    Create Saga object per Saga, and sum all price gathered from saga objects
    if input = [Back to the Future 1,Back to the Future 2,Back to the Future 3,La chèvre] --> return :{"Back to the Future" : Saga object, "La chèvre" : Saga object}
    '''
    sagaDict = {}
    price = 0

    '''
    if this is the first time we meet a movie, we create a saga object for him,
    ex: if we have Back to the Future 1, we create , Back to the Future saga object, then if we have Back to the Future 2,
    we not consider it as a new movie but as an extension, a new episode.
    if we have already meet the movie, we add episode to the saga object already created
    '''
    for movie in orderList:
        title,episode = SliceBaseTitle(movie,debug,mode)

        if title not in sagaDict:
            sagaDict[title] = Saga(title = title, episode = episode,debug=debug)
        else:
            sagaDict[title].add_episode(episode=episode)

    if debug == "--debug":
        print("Dictionnary of movies per Saga {0}".format(sagaDict))
    for key in sagaDict:
        price = price + sagaDict[key].getPrice()
    return price
