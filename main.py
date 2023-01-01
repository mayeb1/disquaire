import wx
import sys
import argparse
from src.menu import MyFrame
from src.tools import Text_to_List,OrderPrice


parser = argparse.ArgumentParser()

parser.add_argument('-d', '--debug', action='store_true',help="debug mode")

parser.add_argument('-g', '--graphics-mode', action='store_true',help="graphics interface")

parser.add_argument('--p',nargs=1,default=[],help="movies order text file")

parser.add_argument('-a','--add-movies', action='store_true',help='add manually movies')

parser.add_argument('-m','--mode', action='store_true',help='promotion mode for all the saga, not only \'back to the future\'')

args = parser.parse_args()
arguments = [args.debug , args.graphics_mode,args.p != [],  args.add_movies,  args.mode]


'''
python3.10 main.py -d -a -m --> arguments = [True,False,False,True,True]
'''

if __name__ =="__main__":

    '''
    case disjunction of user choice
    '''

    match arguments[1:]:
        case [True,False,False,False] :
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
        case [True,False,False,True] :
             if arguments[0] == True:
                 debug='--debug'
                 app = wx.App()
                 frm = MyFrame(debug,mode= arguments[-1])
                 frm.Show()
                 app.MainLoop()
             else:
                 app = wx.App()
                 frm = MyFrame(mode= arguments[-1])
                 frm.Show()
                 app.MainLoop()


        case [False,True,False,False]:
             if arguments[0] == True:
                debug ="--debug"
                orderList = Text_to_List(path =args.p[0] ,debug=debug )
                print("Total Price :",OrderPrice(orderList=orderList,debug=debug))
             else:
                orderList = Text_to_List(path =args.p[0])
                print("Total Price :",OrderPrice(orderList=orderList))

        case [False,True,False,True]:
             if arguments[0] == True:
                debug ="--debug"
                orderList = Text_to_List(path =args.p[0] ,debug=debug )
                print("Prix total :",OrderPrice(orderList=orderList,debug=debug,mode = arguments[-1]))
             else:
                orderList = Text_to_List(path =args.p[0])
                print("Total Price :",OrderPrice(orderList=orderList,mode = arguments[-1]))


        case [False,True,True,False]:
             debug ="--debug"
             if arguments[0] == True:
                movie = ''
                movie = input('Enter the movie:')
                orderList = Text_to_List(path =args.p[0],debug=debug)
                while movie != 'exit':
                      orderList.append(movie.strip())
                      movie = input('Enter the movie,if you have finish tap \'exit\':')

                print(orderList)
                print("Total Price :",OrderPrice(orderList=orderList,debug=debug))
             else:
                movie = ''
                movie = input('Enter the movie:')
                orderList = Text_to_List(path =args.p[0])
                while movie != 'exit':
                      orderList.append(movie.strip())
                      movie = input('Enter the movie,if you have finish tap \'exit\':')
                print("Total Price :",OrderPrice(orderList=orderList))


        case [False,True,True,True]:
             debug ="--debug"
             if arguments[0] == True:
                movie = ''
                movie = input('Enter the movie:')
                orderList = Text_to_List(path =args.p[0],debug=debug)
                while movie != 'exit':
                      orderList.append(movie.strip())
                      movie = input('Enter the movie,if you have finish tap \'exit\':')

                print(orderList)
                print("Total Price :",OrderPrice(orderList=orderList,debug=debug,mode = arguments[-1]))
             else:
                movie = ''
                movie = input('Enter the movie:')
                orderList = Text_to_List(path =args.p[0])
                while movie != 'exit':
                      orderList.append(movie.strip())
                      movie = input('Enter the movie,if you have finish tap \'exit\':')
                print("Total Price :",OrderPrice(orderList=orderList,mode = arguments[-1]))


        case [False,False,True,False]:
             debug ="--debug"
             movie = ''
             movie = input('Enter the movie:')
             orderList = []
             while movie != 'exit':
                   orderList.append(movie.strip())
                   movie = input('Enter the movie,if you have finish tap \'exit\':')

             if arguments[0] == True:
                print(orderList)
                print("Total Price :",OrderPrice(orderList=orderList,debug=debug))

             else:
                print("Total Price :",OrderPrice(orderList=orderList))

        case [False,False,True,True]:
             debug ="--debug"
             movie = ''
             movie = input('Enter the movie:')
             orderList = []
             while movie != 'exit':
                       orderList.append(movie.strip())
                       movie = input('Enter the movie,if you have finish tap \'exit\':')

             if arguments[0] == True:
                    print(orderList)
                    print("Total Price :",OrderPrice(orderList=orderList,debug=debug,mode = arguments[-1]))

             else:
                    print("Total Price :",OrderPrice(orderList=orderList,mode = arguments[-1]))

        case [True,True,True,False]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
        case [True,False,True,False]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
        case [True,True,False,False]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
        case [True,True,True,True]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
        case [True,False,True,True]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
        case [True,True,False,True]:
             print("###########################Cannot use graphics software with -p or -a, refer to README to use arguments correctly########################")
