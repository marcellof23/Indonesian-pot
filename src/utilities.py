import os, re
import PySimpleGUI as sg

path = "/proc/self/cgroup"

def is_docker():
  if not os.path.isfile(path): return False
  with open(path) as f:
    for line in f:
      if re.match("\d+:[\w=]+:/docker(-[ce]e)?/\w+", line):
        return True
    return False

def setPlaceholder(widget, placeholderText):
  if getattr(widget, "WxTextCtrl", None): # SimpleGUIWx
      textCtrl = widget.WxTextCtrl # type: wx.TextCtrl
      textCtrl.SetHint(placeholderText)
      return
  if getattr(widget, "QT_QLineEdit", None): # SimpleGUIQt
      lineEdit = widget.QT_QLineEdit # type: QWidgets.QLineEdit
      lineEdit.setPlaceholderText(placeholderText)
      return
  if getattr(widget, "Widget", None) and hasattr(widget.Widget, "attributes"): # SimpleGUIWeb
      textInput = widget.Widget # type: remi.gui.TextInput
      textInput.attributes["placeholder"] = placeholderText
      return
  if getattr(widget, "TKEntry", None):
      entry = widget.TKEntry
      def resetCursor(event=None):
          if entry.get() == placeholderText:
              entry.after_idle(entry.icursor, 0)
      def startInput(event=None):
          if entry.get() == placeholderText:
              entry.delete(0, "end")
              entry.config(fg="black")
          else:
              entry.after_idle(showPlaceholder)
      def showPlaceholder(event=None):
          if entry.get() == placeholderText or not entry.get():
              entry.delete(0, "end")
              entry.insert(0, placeholderText)
              entry.config(fg="gray50")
              entry.after_idle(entry.icursor, 0)
      entry.bind("<FocusIn>", resetCursor)
      entry.bind("<FocusOut>", showPlaceholder)
      entry.bind("<Button-1>", resetCursor)
      entry.bind("<Key>", startInput)
      showPlaceholder()
      def get_value():
          text = entry.get()
          return text if text != placeholderText else ""
      widget.Get = get_value
      return