from enum import Enum

class TextStyle(Enum):
    Center = 0
    CenterTop = 1
    CenterBottom = 2
    CenterLeft = 3
    CenterRight = 4
    LeftTop = 5
    LeftBottom = 6
    RightTop = 7
    RightBottom = 8
    No = 9

class InputMode(Enum):
    NumberInputMode = 0
    TextInputMode = 1
    ControlInputMode = 2

class EnterMode(Enum):
    Submit = 0
    Text = 1