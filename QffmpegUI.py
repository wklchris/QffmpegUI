from subprocess import Popen, PIPE, STDOUT, check_output
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from Ui_QffmpegUI import Ui_winMain

# High DPI support
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# class StrFlow(QtCore.QObject):
#     textFlowSignal = QtCore.pyqtSignal(str)
#     def write(self, text):
#         self.textFlowSignal.emit(str(text))

class GForm(QMainWindow, Ui_winMain):
    def __init__(self):
        super(GForm, self).__init__()
        self.setupUi(self)
        # Set the file browser button
        self.btnFileBrowser.clicked.connect(self.file_browser)
        self.btnClearList.clicked.connect(self.clear_filelist)
        self.btnMoveUpFile.clicked.connect(self.move_up_file)
        self.btnDeleteFile.clicked.connect(self.delete_file)
        # Capture the command line output
        self.btnAdvanceRun.clicked.connect(self.run_advance_cmd)
    
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

    # --- Advance Tab ---
    def run_advance_cmd(self):
        advanceCmd = self.tbxAdvanceCmd.toPlainText()
        try:
            pipe = Popen(advanceCmd, encoding='utf-8', stdout=PIPE, stderr=PIPE)
            stdout, stderr = pipe.communicate()
            streamText = f"{stderr}\n---\nError" if stderr else f"{stdout}\n---\nPass"
            self.txeAdvanceOutput.setPlainText(streamText)
        except Exception as e:
            self.txeAdvanceOutput.setPlainText(f"{e}\n---\nException thrown")
        ## Move the view to the bottom
        self.txeAdvanceOutput.moveCursor(QTextCursor.End)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = GForm()
    w.show()
    sys.exit(app.exec_())
