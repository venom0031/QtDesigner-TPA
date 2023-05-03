from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from peliculas import Ui_MainWindow
import sys

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.listadepeliculas()
        self.ui.anhadir_pelicula.clicked.connect(self.addpelicula)
        self.ui.editar_nombre_pelicula.clicked.connect(self.editarpelicula)
        self.ui.quitar_pelicula.clicked.connect(self.removerpelicula)
        self.ui.editar_nombre_pelicula.clicked.connect(self.salir)

    def listadepeliculas(self):
        self.ui.Lista_de_peliculas.addItems(["Zack and Miri Make a Porno","Youth in Revolt","You Will Meet a Tall Dark Stranger","When in Rome"
                                            ,"What Happens in Vegas","Water For Elephants","WALL-E","Waitress","Waiting For Forever"
                                            "Valentine's Day","Tyler Perry's Why Did I get Married","Twilight: Breaking Dawn","Twilight","The Ugly Truth"
                                            ,"The Twilight Saga: New Moon","The Time Traveler's Wife","The Proposal","The Invention of Lying","The Heartbreak Kid"])
        self.ui.Lista_de_peliculas.setCurrentRow(1)

    def addpelicula(self):
        currentIndex = self.ui.Lista_de_peliculas.currentRow()
        text, ok = QInputDialog.getText(self,"Nueva Pelicula","Nombre De la Pelicula")
        if ok and text is not None:
            self.ui.Lista_de_peliculas.insertItem(currentIndex,text)

    def editarpelicula(self):
        currentIndex = self.ui.Lista_de_peliculas.currentRow()
        item = self.ui.Lista_de_peliculas.item(currentIndex)
        if item is not None:
            text, ok = QInputDialog.getText(self,"Editar Pelicula","Nombre De La Pelicula",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)

    def removerpelicula(self):
        currentIndex = self.ui.Lista_de_peliculas.currentRow()
        item = self.ui.Lista_de_peliculas.item(currentIndex)
        if item is None:
            return

        question = QMessageBox.question(self,"Remover Pelicula",
                                        "¿Seguro de que quieres borrar esta pelicula?" + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.ui.Lista_de_peliculas.takeItem(currentIndex)
            del item

    def salir(self):
        question = QMessageBox.question(self,"Salir",
                                        "¿Seguro que deseas salir?",
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            quit()



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()