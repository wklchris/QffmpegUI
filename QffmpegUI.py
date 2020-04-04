import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from Ui_QffmpegUI import Ui_winMain

# High DPI support
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class GForm(QMainWindow, Ui_winMain):
    def __init__(self):
        super(GForm, self).__init__()
        self.setupUi(self)
        # Set the file browser button
        self.btnFileBrowser.clicked.connect(self.file_browser)
        self.btnClearList.clicked.connect(self.clear_filelist)
        self.btnMoveUpFile.clicked.connect(self.move_up_file)
        self.btnDeleteFile.clicked.connect(self.delete_file)
    
    # --- File Tab ---
    def file_browser(self):
        options = QFileDialog.Options()
        fnames, _ = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileName()", "",
            "All Files (*)", options=options)
        ## Add file names to the list widget
        if fnames:
            for fp in fnames:
                self.lstFileList.addItem(QListWidgetItem(f"{fp}"))
        self.update_filenum()

    def update_filenum(self):
        n = self.lstFileList.count()
        self.lblTotalFiles.setText(QtCore.QCoreApplication.translate(
            "winMain", f"{n} files selected."))
        return n
    
    def move_up_file(self):
        currentRow = self.lstFileList.currentRow()
        currentItem = self.lstFileList.takeItem(currentRow)
        r = max(currentRow-1, 0)
        self.lstFileList.insertItem(r, currentItem)
        self.lstFileList.setCurrentRow(r)

    def delete_file(self):
        currentRow = self.lstFileList.currentRow()
        self.lstFileList.takeItem(currentRow)

        n = self.update_filenum()
        if n > 0:
            self.lstFileList.setCurrentRow(max(currentRow-1, 0))

    def clear_filelist(self):
        self.lstFileList.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GForm()
    w.show()
    sys.exit(app.exec_())
