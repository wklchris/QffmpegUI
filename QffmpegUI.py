from subprocess import Popen, PIPE
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidgetItem
from Ui_QffmpegUI import Ui_winMain

# High DPI support
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class GForm(QMainWindow, Ui_winMain):
    def __init__(self):
        super(GForm, self).__init__()
        self.setupUi(self)
        # Init variables
        self.qFileList, self.qOutFileList = [], []
        self.qAudioOptions = None
        self.qContainerType = "MP3"
        # Set the file browser button
        self.btnFileBrowser.clicked.connect(self.file_browser)
        self.btnClearList.clicked.connect(self.clear_filelist)
        self.btnMoveUpFile.clicked.connect(self.move_up_file)
        self.btnDeleteFile.clicked.connect(self.delete_file)
        # Set the audio panel buttons
        self.ckbxNoAudio.stateChanged.connect(self.no_audio)
        self.rbtnBitRateManual.toggled.connect(self.manual_audio_bitrate)
        self.btnAudioRun.clicked.connect(self.run_audio_tab)
        # Capture the command line output
        self.tbxAdvanceCmd.setPlainText(QtCore.QCoreApplication.translate(
            "winMain", "ffmpeg -version"))
        self.btnAdvanceRun.clicked.connect(self.run_advance_cmd)
        self.run_advance_cmd()  # Initial check for ffmpeg
        ## Enable clickable web links
        self.tbrAbout.setOpenExternalLinks(True)

        # Always start at the first tab
        self.tabWidget.setCurrentIndex(0)

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
        self.qFileList = fnames  # Store the file list
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
        del(self.qFileList[currentRow])
        self.lstFileList.takeItem(currentRow)

        n = self.update_filenum()
        if n > 0:
            self.lstFileList.setCurrentRow(max(currentRow-1, 0))

    def clear_filelist(self):
        self.lstFileList.clear()

    # --- Advance Tab ---
    def run_advance_cmd(self):
        advanceCmd = self.tbxAdvanceCmd.toPlainText()
        self.txeAdvanceOutput.setPlainText(self.cmd_output(advanceCmd))
        ## Move the view to the bottom
        self.txeAdvanceOutput.moveCursor(QTextCursor.End)
    
    def cmd_output(self, cmdline):
        try:
            pipe = Popen(cmdline, encoding='utf-8', stdout=PIPE, stderr=PIPE)
            stdout, stderr = pipe.communicate()
            streamText = f"{stderr}\n---\nError" if stderr else f"{stdout}\n---\nPass"
        except Exception as e:
            streamText = f"{e}\n---\nException thrown"
        return streamText
    
    def join_cmd(self, infname):
        cmd_list = [
            "ffmpeg -y",  # Always overwrite
            "-hide_banner",  # Hide info banner
            f'-i "{infname}"',
            self.qAudioOptions,
            f'"{self.generate_output_fname(infname)}"'
        ]
        cmd_each_loop = ' '.join([x for x in cmd_list if x])
        return cmd_each_loop

    def update_final_cmd(self):
        # Jump to the Advance tab only when there's one file
        if len(self.qFileList) == 1:
            infname = self.qFileList[0]
            self.qWorkFlowCmd = self.join_cmd(infname)
            self.tbxAdvanceCmd.setPlainText(self.qWorkFlowCmd)
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(
                QtWidgets.QWidget, "tabAdvance"))
        # else:
        #     for infname in self.qFileList:


    # --- Audio Tab ---
    def no_audio(self):
        if self.ckbxNoAudio.isChecked():
            self.gbxAudioConfig.setEnabled(False)
        else:
            self.gbxAudioConfig.setEnabled(True)

    def manual_audio_bitrate(self):
        if self.rbtnBitRateManual.isChecked():
            self.spbxAudioBitRate.setEnabled(True)
        else:
            self.spbxAudioBitRate.setEnabled(False)
    
    def generate_audio_options(self):
        if self.ckbxNoAudio.isChecked():
            self.qAudioOptions = "-an"
        else:
            ops = {k: None for k in ["-c:a", "-b:a"]}
            ## If an audio codec is selected
            if 'Auto' not in self.cbbxAudioCodec.currentText():
                ops["-c:a"] = self.cbbxAudioCodec.currentText()
            ## If the audio bitrate is specified (in Kbps)
            if self.spbxAudioBitRate.isEnabled():
                ops["-b:a"] = "{}k".format(self.spbxAudioBitRate.value())
            audioOpsLst = [f"{k} {v}" for k, v in ops.items() if v]
            self.qAudioOptions = ' '.join(audioOpsLst)

    def run_audio_tab(self):
        self.generate_audio_options()
        self.update_final_cmd()
    
    # --- Work Flow tab ---
    def generate_output_fname(self, infullpath):
        fname = infullpath.split('/')[-1]
        fdir = infullpath[:-(len(fname)+1)]
        fext = fname.split('.')[-1]
        fshortname = fname[:-(len(fext)+1)]
        foutext = self.qContainerType.lower()
        
        outfullpath = f'{fdir}/{fshortname}.{foutext}'
        return outfullpath

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = GForm()
    w.show()
    sys.exit(app.exec_())
