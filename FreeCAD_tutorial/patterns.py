# Draft Wire example from doc
import FreeCAD as App
import Draft

doc = App.newDocument()
# App.setActiveDocument("Unnamed")
# App.ActiveDocument=App.getDocument("Unnamed")
# Gui.ActiveDocument=Gui.getDocument("Unnamed")

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()

# ===== 2021-09-06 Dimension experiment ===== #
Gui.runCommand('Draft_Dimension',0)
_dim_ = Draft.make_linear_dimension_obj(FreeCAD.ActiveDocument.Wire002, i1=3, i2=1, dim_line=FreeCAD.Vector(1775.810546875, -757.1243286132812, 0.0))
# Gui.Selection.addSelection('Unnamed','Dimension')
Draft.autogroup(_dim_)
FreeCAD.ActiveDocument.recompute()

# Setting parameters in GUI
FreeCADGui.getDocument('Unnamed').getObject('Dimension').ArrowSize = '50 mm'
FreeCADGui.getDocument('Unnamed').getObject('Dimension').ExtLines = '1000 mm'

# Do:
# (1) Apply function in GUI
# (2) Identify objects in the console
# (3) Study objects in the wiki docs
# (4) Prototype patterns
