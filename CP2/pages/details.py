from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

class DetailsPage(QMainWindow):
    def __init__(self, main_window, root_dir):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        
        # load file ui
        ui_path = self.root_dir + "/GUI/..."
        uic.loadUi(ui_path, self)
        
        # TODO: bat su kien chuyen close ve home 
        
        # hien thi giao dien
        self.show()
        
    # TODO: ham close -> home