import wx
import sys
import argparse
from src.menu import MyFrame
from src.tools import Text_to_List,OrderPrice


parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug', action='store_true',
    help="debug mode")

parser.add_argument('-g', '--graphics-mode', action='store_true',
    help="mode graphique")

parser.add_argument('--p',nargs=1,default=[],help="fichier text de commande")


parser.add_argument('-a','--add-movies', action='store_true',help='add manually movies')


args = parser.parse_args()
arguments = [args.debug , args.graphics_mode,args.p != [],args.add_movies]


if __name__ =="__main__":

    match arguments[1:]:
        case [True,False,False] :
             if arguments[0] == True:
                 debug='--debug'
                 app = wx.App()
                 frm = MyFrame(debug)
                 frm.Show()
                 app.MainLoop()
             else:
                 app = wx.App()
                 frm = MyFrame()
                 frm.Show()
                 app.MainLoop()


        case [False,True,False]:
             if arguments[0] == True:
                debug ="--debug"
                orderList = Text_to_List(path =args.p[0] ,debug=debug )
                print("Prix total :",OrderPrice(orderList=orderList,debug=debug))
             else:
                orderList = Text_to_List(path =args.p[0])
                print("Prix total :",OrderPrice(orderList=orderList))

        case [False,True,True]:
             debug ="--debug"
             if arguments[0] == True:
                movie = ''
                movie = input('Enter the movie:')
                orderList = Text_to_List(path =args.p[0],debug=debug)
                while movie != 'exit':
                      orderList.append(movie.strip())
                      movie = input('Enter the movie,if you have finish tap \'exit\':')

                print(orderList)
                print("Prix total :",OrderPrice(orderList=orderList,debug=debug))
             else:
                movie = ''
                movie = input('Enter the movie:')
                orderList = Text_to_List(path =args.p[0])
                while movie != 'exit':
                      orderList.append(movie.strip())
                      movie = input('Enter the movie,if you have finish tap \'exit\':')
                print("Prix total :",OrderPrice(orderList=orderList))

        case [False,False,True]:
             debug ="--debug"
             movie = ''
             movie = input('Enter the movie:')
             orderList = []
             while movie != 'exit':
                   orderList.append(movie.strip())
                   movie = input('Enter the movie,if you have finish tap \'exit\':')

             if arguments[0] == True:
                print(orderList)
                print("Prix total :",OrderPrice(orderList=orderList,debug=debug))

             else:
                print("Prix total :",OrderPrice(orderList=orderList))

        case [True,True,True]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
        case [True,False,True]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
        case [True,True,False]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
