# -*- coding: UTF-8 -*-

import nuke

# Custom keyboard shortcuts for existing Nuke nodes.

toolbar = nuke.toolbar("Nodes")

m = toolbar.addMenu("Channel", "ToolbarChannel.png")
m.addCommand("Shuffle", "nuke.createNode(\"Shuffle\")", "z", icon="Shuffle.png", shortcutContext=dagContext)

m = toolbar.addMenu("Merge", "ToolbarMerge.png")
m.addCommand("KeyMix", "nuke.createNode(\"Keymix\")", "a", icon="Keymix.png", shortcutContext=dagContext)
m.addCommand("Premult", "nuke.createNode(\"Premult\")", "v", icon="Premult.png", shortcutContext=dagContext)
m.addCommand("Unpremult", "nuke.createNode(\"Unpremult\")", "alt+v", icon="Unpremult.png", shortcutContext=dagContext)