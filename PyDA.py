import wx
#from espeak import espeak
import wikipedia
import wolframalpha
import pyttsx3
engine = pyttsx3.init()
# from espeak import espeak
# import wolframalpha

app_id = "PGQKHV-RHLPLGYULG"
client = wolframalpha.Client(app_id)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(430, 130),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 15)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        engine.say("Welcome to Virtual Assistant")
        engine.runAndWait()
    def OnEnter(self, event):

        var = self.txt.GetValue()
        var = var.lower()

        try:
        	res = client.query(var)
        	answer = next(res.results).text
        	print (answer)
            #espeak.synth("The answer is " + str(answer))
       	except:
       		try:
       			# var = var.split(' ')
       			# var = ' '.join(var[2:])
       			print (wikipedia.summary(var))
       		except:
       			print ("I don't know")
        
        engine.say("The Searched Results is " + answer)
        engine.runAndWait()

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
