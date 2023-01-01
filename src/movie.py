


class Saga:
    '''
    This class will keep in memory saga (or single movie) and how many episode are purchase from this saga
    '''
    def __init__(self,title:str,episode:str,debug:str=''):

        '''
        if episode = 'None' , the movie isn't yet a saga

        Example:

        self._basetitle = 'Avatar'
        self._nomenclature={"1":2,"2":1,"3",1} if the order is composed of 2 avatar 1, 1 avatar 2 and 1 avatar 3  structur = {episode : number of purchase}
        self._total_price = 48 euros
        '''

        self._basetitle = title      # basetitle of Back to the Future 2 is Back to the Future
        self._nomenclature={}        # {episode : number of purchase}
        self._total_price = 0        # calculed price
        self._reduction=[0.1,0.2]    # reduction of 10% or 20%
        self._sagaPrice = 15         # price of 15 euros for saga
        self._usualPrice = 20        # price of 20 euros for simple movie, not saga
        self.debug =debug            #debug mode

        self.add_episode(episode = episode) # for initate the price, we have to add the first episode when we create the object



    def add_episode(self,episode:str):
        if self.debug == '--debug':
           print("Adding episode {0} of movie {1} :".format(episode,self._basetitle))
        if episode in self._nomenclature:
           self._nomenclature[episode] = self._nomenclature[episode]+1 #add one purchase if the episode has already added to the dictionnary
        else:
           self._nomenclature[episode] = 1 #if epidode 2 of avatar hasn't yet added to the dictionnary, we have to initiate it and add the key "2"
        self._computePrice()


    def _computePrice(self):

        '''
        This funection compute the price from the nomenclature, if you have self._nomenclature={"1":2,"2":1,"3",1}
        then the price id equal to (2+1+2)*(1-0.2)
        '''

        number_of_episode = len(self._nomenclature)
        total_price = 0
        match number_of_episode:
            case 1:
                if None in self._nomenclature:
                   total_price = self._usualPrice*self._nomenclature[None]
                else:
                   total_price = self._sagaPrice*self._nomenclature["1"]

            case 2:
                total_price = self._sagaPrice*(self._nomenclature["1"] + self._nomenclature["2"])*(1-self._reduction[0])

            case _:
                for number in self._nomenclature.values():
                    total_price = total_price + self._sagaPrice*number
                total_price = total_price * (1-self._reduction[1])
        self._total_price=total_price



    def getPrice(self):
         return self._total_price
