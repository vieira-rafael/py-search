# qbr.py# Chris Barker# CMU S13 15-112 Term Project

from app import Appimport Tkinterimport screenGrabberfrom cube import Cube
class Cubr(App):
 def init(self): self.resized = False self.inCam = False        ctrlPaneHeight = 60        ctrlPaneColor = '#222222'
 # Canvas for holding buttons self.controlPane = Tkinter.Canvas(self.root, width = self.width,  height = ctrlPaneHeight, background=ctrlPaneColor)
 # Event handlers for window resizing self.controlPane.bind('<Configure>', self.controlResize) self.canvas.bind('<Configure>', self.resize)
 # Superclass deals with packing canvas self.controlPane.pack(expand=1, fill=Tkinter.BOTH) self.newCube()
 def newCube(self): # replaces self.cube with a new Cube() object if hasattr(self, 'cube'): self.cube.cleanup() del self.cube self.cube = Cube(self.canvas, self.controlPane, self)
 def received(self, cube): # callback handler for the screenGrabber module # sets self.cube's configuration based on the Streamer cube self.inCam = False self.cube.helpState = self.cube.INGAME if self.cube.debug: print cube.events try: self.cube.setConfig(cube) except: # Something went wrong setting the configuration self.cube.state.setSolved()
 def fromCamera(self): # Create "Starting webcam..." popup while we wait for webcam to turn on self.canvas.create_rectangle(self.width/2 - 200, self.height/2 - 50, self.width/2 + 200, self.height/2 + 50, fill='#123456', outline='#abcdef', width=5) self.canvas.create_text(self.width/2, self.height/2, fill='#ffffff', font='Arial 36 bold', text='Starting webcam...')
 self.canvas.update() self.newCube() self.inCam = True
 # Hand over control to the screenGrabber        screenGrabber.cubeFromCam(app=self, callback=self.received)  def timerFired(self): # cube.timer wrapper -- only calls if we are not in screenGrabber if not self.inCam: self.cube.timer()
 def debug(self): # toggle whether debug is on or off. this feature is disabled in release builds. self.cube.debug = not self.cube.debug self.cube.redraw()
 def resize(self, event): # Event binding for canvas resizing self.width = event.width self.height = event.height self.resized = True self.cube.width = self.width self.cube.height = self.height self.cube.camera.width = self.width self.cube.camera.height = self.height
 def mousePressed(self, event): # Wrapper for cube.click self.cube.click(event)
 def controlResize(self, event): # Event binding for controlPane resizing # Adjust size, and compensate for border        borderX, borderY = -7, -6 self.controlPane.config(width=event.width+borderX, height=event.height+borderY) self.cube.configureControls(self.controlPane)
 def keyPressed(self, event): # key event handler
 # Adjust viewmode. only available in debug. if self.cube.debug: if event.keysym == 'o': self.cube.camera.fisheye(+1.2) self.cube.redraw() elif event.keysym == 'p': self.cube.camera.fisheye(+0.8) self.cube.redraw()
        amt = self.cube.amt # Delta value for rotation sensitivity if event.keysym == 'Left': self.cube.direction = (amt, self.cube.direction[1]) elif event.keysym == 'Right': self.cube.direction = (-amt, self.cube.direction[1]) elif event.keysym == 'Up': self.cube.direction = (self.cube.direction[0], amt) elif event.keysym == 'Down': self.cube.direction = (self.cube.direction[0], -amt) # command for clockwise rotation of a face elif event.keysym in 'rdlufb': self.cube.rotate(event.keysym.upper()) # command for counterclockwise rotation of a face elif event.keysym in 'RDLUFB': self.cube.rotate(event.keysym + "'") else:  if self.cube.debug: print event.keysym
 def keyReleased(self, event): if event.keysym in ['Left', 'Right', 'Down', 'Up']: # stopping rotation self.cube.direction = (0, 0)
if __name__ == '__main__':    game = Cubr(name="Cubr")