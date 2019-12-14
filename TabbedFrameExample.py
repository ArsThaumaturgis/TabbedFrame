#######################################################################
##                                                                   ##
## An example of the use of TabbedFrame                              ##
##                                                                   ##
##                                                                   ##
#######################################################################
##                                                                   ##
## Original version written by                                       ##
## Ian Eborn (Thaumaturge) in 2019                                   ##
##                                                                   ##
#######################################################################
##                                                                   ##
## This code is licensed under the MIT license. See the              ##
## license file (LICENSE.md) for details.                            ##
## Link, if available:                                               ##
##  https://github.com/ArsThaumaturgis/KeyMapper/blob/master/LICENSE ##
##                                                                   ##
#######################################################################

from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DGG, DirectFrame, DirectButton, DirectOptionMenu
from panda3d.core import TextNode, NodePath

from TabbedFrame import TabbedFrame

import random

class TabbedFrameExample(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Construct our TabbedFrame
        self.frame = TabbedFrame(tab_frameSize = (0, 7, 0, 2),
                                 tab_text_align = TextNode.ALeft,
                                 tab_text_pos = (0.2, 0.6))

        # Make our "pages". These are pretty much just DirectGUI elements
        # that TabbedFrame will flip between

        # Our first "page". This will hold some text.
        page1 = DirectFrame()
        text = TextNode("text")
        text.setText("Press \"Space\" to resize the frame!\n\nPress \"shift\" to teleport the frame!\n\nPress \"ctrl\" to scale the frame!\n\nPress \"escape\" to close this example-program.")
        text.setWordwrap(15)
        text.setTextColor(0, 0, 0, 1)
        textNP = NodePath(text)
        textNP.reparentTo(page1)
        textNP.setScale(0.05)
        textNP.setPos(-0.4, 0, 0.4)

        # Our second page. This will hold a range of buttons.
        # (Which don't actually do anything.)
        page2 = DirectFrame(frameSize = (-0.4, 0.4, -2.0, 0.5))
        for i in range(10):
            btn = DirectButton(text = "Button" + str(i),
                               parent = page2,
                               scale = 0.07,
                               pos = (0, 0, -0.2*i))

        # And finally, add the pages to our TabbedFrame, along with labels
        # for their buttons
        self.frame.addPage(page1, "First Tab")
        self.frame.addPage(page2, "Another Tab")

        # A few events: one to change our TabbedFrame's size, and one to quit
        self.accept("space", self.resizeTabbedFrame)
        self.accept("shift", self.moveTabbedFrame)
        self.accept("control", self.scaleTabbedFrame)
        self.accept("escape", self.userExit)

    def moveTabbedFrame(self):
        self.frame.setPos(random.uniform(-1, 1), 0, random.uniform(-1, 1))

    def scaleTabbedFrame(self):
        self.frame.setScale(self.frame.getSx() - 0.1)

    def resizeTabbedFrame(self):
        size = self.frame["frameSize"]
        self.frame["frameSize"] = (size[0] - 0.1, size[1] + 0.1, size[2] - 0.1, size[3] + 0.1)

example = TabbedFrameExample()
example.run()