import wx
from .tools import Text_to_List, SliceBaseTitle, OrderPrice
from .movie import Saga


########################################################################
class MyFileDropTarget(wx.FileDropTarget):
    '''
    This class listen event Drag and drop, read the Path and gives to the panel ResultPanel the list of movies ordered.
    OnDropFiles(self, x, y, path) take x and y, position of the mouse, and path, the path file
    '''

    #----------------------------------------------------------------------
    def __init__(self, window,parentFrame,debug:str=''):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.parentFrame =parentFrame
        self.debug =debug

    def OnDropFiles(self, x, y, path):
        #self.window.AppendText("%d file(s) dropped at (%d,%d):\n" % (len(path), x, y))
        #self.window.AppendText("%s\n" % path[0])
        self.orderList = Text_to_List(path = path[0],debug=self.debug)
        for movie in self.orderList:
            self.window.AppendText("%s\n" % movie)
            self.parentFrame.result_panel.addMovie(movie)
        #self.parentFrame.result_panel.setOrderList(self.orderList)
########################################################################

########################################################################
class MyFrame(wx.Frame):
    '''
    Frame where all panel will be displayed
    '''

    #----------------------------------------------------------------------
    def __init__(self,debug:str=''):
        wx.Frame.__init__(self, None, title="Disquaire",size=(800,300))
        self.debug =debug

        self.mainPanel = wx.Panel(self)

        '''Input main panel, it contains dragdrop_panel and enter_panel '''
        self.input_panel = wx.Panel(self.mainPanel)

        '''Drag and Drop Panel'''
        self.dragdrop_panel = wx.Panel(self.input_panel)

        '''Manually input data panel'''
        self.enter_panel = ManualInuputPanel(self.input_panel,'red',self)

        label_input = wx.StaticText(self.input_panel, -1, "Add movie Manually, one at a time please:")

        '''Creation of vertical sizer to organise each element vertically, elements are: dragdrop_panel , enter_panel and label_input'''
        input_sizer = wx.BoxSizer(wx.VERTICAL)
        input_sizer.Add(self.dragdrop_panel, 7,wx.EXPAND| wx.ALL, 5)
        input_sizer.Add(label_input, 1,wx.EXPAND| wx.ALL, 5)
        input_sizer.Add(self.enter_panel, 2,wx.EXPAND|wx.ALL, 5)
        self.input_panel.SetSizer(input_sizer)

        '''Result Panel creation, this panel will contain button for calculation, reset and display price'''
        self.result_panel = ResultPanel(self.mainPanel,'red',self,debug=self.debug )

        '''Position of each panel, we put them horizontally'''
        sizerPanel = wx.BoxSizer(wx.HORIZONTAL)
        sizerPanel.Add(self.input_panel,1, wx.EXPAND|wx.ALL, 5)
        sizerPanel.Add(self.result_panel,1, wx.EXPAND|wx.ALL, 5)

        '''Associate the main panel to the sizerPanel, it means that mainPanel contains input_panel and result_panel'''
        self.mainPanel.SetSizer(sizerPanel)

        label_drop = wx.StaticText(self.dragdrop_panel, -1, "Drop some files here:")
        self.text_drop = wx.TextCtrl(self.dragdrop_panel, -1, "",style= wx.TE_READONLY |wx.TE_MULTILINE|wx.HSCROLL)

        dt = MyFileDropTarget(self.text_drop ,self,debug=self.debug)
        self.text_drop.SetDropTarget(dt)

        '''Position of each element in drag and drop panel, we put them vertically'''
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label_drop, 0, wx.ALL, 5)
        sizer.Add(self.text_drop, 1, wx.EXPAND|wx.ALL, 5)
        self.dragdrop_panel.SetSizer(sizer)
########################################################################



########################################################################
class ResultPanel(wx.Panel):


    #----------------------------------------------------------------------
    def __init__(self, parent, color,parentFrame:wx.Frame,debug:str='',orderList:str=list()):
        '''
        This Panel is made for computing results, reset to compute again
        orderList = ["avatar 1","avatar 2", "Back to the Future 1"]
        parentFrame is the main frame, it allows us to access text_drop object and clear it
        '''

        wx.Panel.__init__(self, parent)
        self.orderList=orderList
        self.parentFrame=parentFrame
        self.debug = debug
        self.SetBackgroundColour(color)

        self.price ="0"

        '''when you click on the Compute price button, _OnButtonClickPrice enable'''
        self.button_price = wx.Button(self, wx.ID_ANY, 'Compute price', (10, 10))
        self.button_price.Bind(wx.EVT_BUTTON, self._OnButtonClickPrice)

        '''when you click on the reset button, _OnButtonClickReset enable'''
        self.button_reset = wx.Button(self, wx.ID_ANY, 'reset', (10, 10))
        self.button_reset.Bind(wx.EVT_BUTTON, self._OnButtonClickReset)

        self.lbl = wx.StaticText(self, label="Result:")

        self.response = wx.TextCtrl ( self, value = self.price,style = wx.TE_READONLY | wx.TE_CENTER )

        '''organise elements in the result panel'''
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.button_price, 0, wx.ALL|wx.CENTER, 10)
        sizer.Add(self.button_reset, 0, wx.ALL|wx.CENTER, 10)
        sizer.Add(self.lbl, 0, wx.ALL|wx.EXPAND|wx.CENTER, 10)
        sizer.Add(self.response, 0, wx.ALL|wx.EXPAND|wx.CENTER, 10)

        self.SetSizer(sizer)

    def _OnButtonClickPrice(self, event):
        self.response.Clear()
        self.response.write(str(OrderPrice(self.orderList,self.debug)))


    def _OnButtonClickReset(self, event):
        self.parentFrame.text_drop.Clear()
        self.response.Clear()
        self.orderList=list()
        self.response.write(self.price)

    def setOrderList(self,orderList):
        self.orderList=orderList
    def addMovie(self,movie):
        self.orderList.append(movie)

########################################################################


########################################################################
class ManualInuputPanel(wx.Panel):

    '''
    This Panel is made for manual input
    parentFrame is the main frame, it allows us to access text_drop object and add text and addMovie in orderList from ResultPanel
    '''
    #----------------------------------------------------------------------
    def __init__(self, parent, color,parentFrame):
        wx.Panel.__init__(self, parent)
        self.parentFrame=parentFrame
        self.SetBackgroundColour(color)



        self.value =""

        '''when you click on the Add movie button, _OnButtonClick enable'''
        self.button = wx.Button(self, wx.ID_ANY, 'Add movie', (10, 10))
        self.button.Bind(wx.EVT_BUTTON, self._OnButtonClick)


        self.input_movie= wx.TextCtrl ( self, value = self.value,style = wx.TE_LEFT )
        self.input_movie.SetHint('Enter movie title')



        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.input_movie, 2, wx.ALL|wx.EXPAND|wx.CENTER, 10)
        sizer.Add(self.button, 0, wx.ALL|wx.CENTER, 10)

        self.SetSizer(sizer)

    def _OnButtonClick(self, event):
        self.movie = self.input_movie.GetLineText(0)
        if self.movie.strip() != '':
           self.parentFrame.result_panel.addMovie(self.movie)
        self.parentFrame.text_drop.AppendText("%s\n" % self.movie)
        self.input_movie.Clear()

    def setOrderList(self,orderList):
        self.orderList=orderList

########################################################################

if __name__ == "__main__":
    app = wx.App()
    frm = MyFrame()
    frm.Show()
    app.MainLoop()
