from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QRect
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from qtguidesign import Ui_MainWindow
from PyQt5.uic import loadUi

class GuiStyle(ApplicationContext ,Ui_MainWindow):

    def __init__(self):
        # loadUi("qtguidesign.ui", self)  #  loadin from qtguidesign.ui
        self.setupUi(self)   # loading from qtguidesign.py
        # setting params
        self.icon_path = self.get_resource("images")
        # stop button style
        self.stopchain_button.setIcon(QtGui.QIcon(self.icon_path + "/stop_icon.png"))
        self.stopchain_button.setIconSize(QtCore.QSize(32, 32))
        # menubar
        self.actionQuit.setIcon(QtGui.QIcon(self.icon_path + '/exit_icon.png'))
        # mcl tab
        self.mcl_tab.setTabIcon(0, QtGui.QIcon(self.icon_path + '/chain_icon.png'))
        self.mcl_tab.setTabIcon(1, QtGui.QIcon(self.icon_path + '/wallet_icon.png'))
        self.mcl_tab.setTabIcon(2, QtGui.QIcon(self.icon_path + '/credit.png'))
        self.mcl_tab.setTabIcon(3, QtGui.QIcon(self.icon_path + '/loop_icon.png'))
        self.mcl_tab.setTabIcon(4, QtGui.QIcon(self.icon_path + '/persons.png'))
        # Side panel
        self.getinfo_refresh_button.setIcon(QtGui.QIcon(self.icon_path + '/refresh_icon.png'))
        self.getinfo_refresh_button.setIconSize(QtCore.QSize(32, 32))
        self.chainstatus_button.setStyleSheet("QPushButton {image: url("+self.icon_path+"/circle-inactive.png); border: 0; width: 30px; height: 30px;}")
        self.chainsync_button.setStyleSheet("QPushButton {image: url("+self.icon_path+"/circle-inactive.png); border: 0; width: 30px; height: 30px;}")
        self.staking_button.setVisible(False)
        self.staking_button = ToggleSwitch(self.miningstatus_frame)
        self.staking_button.setObjectName("staking_button")
        self.gridLayout_17.addWidget(self.staking_button, 1, 1, 1, 1)
        self.mining_button.setVisible(False)
        self.mining_button = ToggleSwitch(self.miningstatus_frame)
        self.mining_button.setObjectName("mining_button")
        self.gridLayout_17.addWidget(self.mining_button, 3, 1, 1, 1)
        # Wallet page button icons
        self.lock_button.setIcon(QtGui.QIcon(self.icon_path + "/coin_lock_icon.png"))
        self.lock_button.setIconSize(QtCore.QSize(32, 32))
        self.unlock_button.setIcon(QtGui.QIcon(self.icon_path + "/coin_unlock_icon.png"))
        self.unlock_button.setIconSize(QtCore.QSize(32, 32))
        self.addressamount_refresh_button.setIcon(QtGui.QIcon(self.icon_path + '/refresh_icon.png'))
        self.addressamount_refresh_button.setIconSize(QtCore.QSize(24, 24))
        # Coin Send-Receive page
        self.coinsend_button.setIcon(QtGui.QIcon(self.icon_path + '/send_coin_icon.png'))
        self.coinsend_button.setIconSize(QtCore.QSize(24, 24))
        # Credit loops page
        self.looprequest_search_button.setIcon(QtGui.QIcon(self.icon_path + '/search_icon.png'))
        self.looprequest_search_button.setIconSize(QtCore.QSize(24, 24))

        self.loopsearch_button.setIcon(QtGui.QIcon(self.icon_path + '/search_icon.png'))
        self.loopsearch_button.setIconSize(QtCore.QSize(24, 24))

        self.loopqueries_pubkey_search_button.setIcon(QtGui.QIcon(self.icon_path + '/search_icon.png'))
        self.loopqueries_pubkey_search_button.setIconSize(QtCore.QSize(24, 24))

        self.activeloops_search_button.setIcon(QtGui.QIcon(self.icon_path + '/search_icon.png'))
        self.activeloops_search_button.setIconSize(QtCore.QSize(24, 24))
        self.transferableloops_search_button.setIcon(QtGui.QIcon(self.icon_path + '/search_icon.png'))
        self.transferableloops_search_button.setIconSize(QtCore.QSize(24, 24))

class ToggleSwitch(QtWidgets.QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setCheckable(True)
        self.setMinimumWidth(66)
        self.setMinimumHeight(22)

    def paintEvent(self, event):
        label = "ON" if self.isChecked() else "OFF"
        bg_color = Qt.green if self.isChecked() else Qt.red

        radius = 10
        width = 32
        center = self.rect().center()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(center)
        painter.setBrush(QtGui.QColor(0,0,0))

        pen = QtGui.QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawRoundedRect(QRect(-width, -radius, 2*width, 2*radius), radius, radius)
        painter.setBrush(QtGui.QBrush(bg_color))
        sw_rect = QRect(-radius, -radius, width + radius, 2*radius)
        if not self.isChecked():
            sw_rect.moveLeft(-width)
        painter.drawRoundedRect(sw_rect, radius, radius)
        painter.drawText(sw_rect, Qt.AlignCenter, label)