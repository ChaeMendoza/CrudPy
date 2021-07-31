from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import conexion

def validarCampos():
    if window.txtNombre.text() == "" or window.txtEmail.text() == "":
        alerta = QMessageBox()
        alerta.setText("Debes llenar todos los campos!")
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        return True

def agregar():
    if validarCampos():
        return False

    nombre = window.txtNombre.text()
    email = window.txtEmail.text()

    objContactos = conexion.contactos()
    contactos = objContactos.crearContacto((nombre, email))
    consultar()

def modificar():
    id = window.txtID.text()
    nombre = window.txtNombre.text()
    email = window.txtEmail.text()

    objContactos = conexion.contactos()
    contactos = objContactos.modificarContacto((nombre, email, id))
    consultar()

def eliminar():
    id = window.txtID.text()
    objConctactos = conexion.contactos()
    contactos = objConctactos.eliminarContacto(id)
    consultar()

def cancelar():
    consultar()

def consultar():
    window.tbContactos.setRowCount(0)
    indiceControl = 0

    objContactos = conexion.contactos()
    contactos = objContactos.leerConctactos()
    for contacto in contactos:
        window.tbContactos.setRowCount(indiceControl + 1)
        window.tbContactos.setItem(indiceControl, 0, QTableWidgetItem(str(contacto[0])))
        window.tbContactos.setItem(indiceControl, 1, QTableWidgetItem(str(contacto[1])))
        window.tbContactos.setItem(indiceControl, 2, QTableWidgetItem(str(contacto[2])))
        indiceControl += 1

    window.txtID.setText("")
    window.txtEmail.setText("")
    window.txtNombre.setText("")

    window.btnAgregar.setEnabled(True)
    window.btnEliminar.setEnabled(False)
    window.btnModificar.setEnabled(False)
    window.btnCancelar.setEnabled(False)

def selecionar():
    id = window.tbContactos.selectedIndexes()[0].data()
    nombre = window.tbContactos.selectedIndexes()[1].data()
    email = window.tbContactos.selectedIndexes()[2].data()

    window.txtID.setText(id)
    window.txtNombre.setText(nombre)
    window.txtEmail.setText(email)

    window.btnAgregar.setEnabled(False)
    window.btnEliminar.setEnabled(True)
    window.btnModificar.setEnabled(True)
    window.btnCancelar.setEnabled(True)

application = QtWidgets.QApplication([])
window = uic.loadUi("ventana.ui")
window.show()
consultar()
window.tbContactos.setHorizontalHeaderLabels(['ID', 'Nombre', 'Correo'])
window.tbContactos.setEditTriggers(QTableWidget.NoEditTriggers)
window.tbContactos.setSelectionBehavior(QTableWidget.SelectRows)

window.tbContactos.cellClicked.connect(selecionar)

window.btnAgregar.clicked.connect(agregar)
window.btnModificar.clicked.connect(modificar)
window.btnEliminar.clicked.connect(eliminar)
window.btnCancelar.clicked.connect(cancelar)

sys.exit(application.exec())