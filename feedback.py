import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='feedback',size = (1000, 1000))
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.TOP | wx.EXPAND, 350)        
        my_btn = wx.Button(panel, label='send feedback',size = (500,40))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.TOP | wx.CENTER, 10)        
        panel.SetSizer(my_sizer)        
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()