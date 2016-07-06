#-------------------------------------------------
#
# Project created by QtCreator 2016-06-14T02:56:43
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = project
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui \
    dialog_filter.ui \
    dialog_openFile.ui \
    dialog_bookM_import.ui \
    dialog_checklist.ui \
    mulselectfile.ui \
    dialog_filelist.ui \
    test.ui \
    dialog_bookm_main.ui \
    dialog_addborrower.ui \
    dialog_borrview_modify.ui \
    dialog_checkfine.ui \
    dialog_checkoverdue.ui

RESOURCES += \
    rs.qrc
