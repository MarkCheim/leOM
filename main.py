import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Feliz Aniversario")
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(45, 5))
        my_btn = wx.Button(panel, label="Feliz aniversario", pos=(5, 120))
        my_btn = wx.Button(panel, label="Confirmar", pos=(5, 60))
        text = wx.StaticText(panel, label="Nome :", pos=(5, 6))
        text = wx.StaticText(panel, label="Idade :", pos=(5, 35))
        self.text_ctrl = wx.TextCtrl(panel, pos=(45, 30))
        text = wx.StaticText(panel, label="Bem Vindo!", pos=(5, 100))

        self.Show()



if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

