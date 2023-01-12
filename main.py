# Perform initialization as early as possible,
# before importing other modules,
# to minimize the risk of memory failures when instantiating framebuffer.
from color_setup import ssd  # Create a display instance.
from gui.core.nanogui import refresh
refresh(ssd, True)  # Initialise and clear display.
import cmath
import utime
from gui.core.colors import *
from gui.core.writer import CWriter
from gui.widgets.dial import Dial, Pointer
from gui.widgets.label import Label
import gui.fonts.arial10 as arial10


def aclock():
    uv = lambda phi: cmath.rect(1, phi)  # Return a unit vector of phase phi
    pi = cmath.pi
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday')
    months = ('Jan', 'Feb', 'March', 'April', 'May', 'June', 'July',
              'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
    # Instantiate CWriter
    CWriter.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
    wri = CWriter(ssd, arial10, GREEN, BLACK)  # Report on fast mode. Or use verbose=False
    wri.set_clip(True, True, False)

    # Instantiate displayable objects
    dial = Dial(wri, 20, 10, height=200, ticks=12, bdcolor=None, label=150, pip=False)  # Border in fg color
    lbltim = Label(wri, 5, 85, 35)
    hrs = Pointer(dial)
    mins = Pointer(dial)
    secs = Pointer(dial)

    hstart = 0 + 0.7j  # Pointer lengths and position at top
    mstart = 0 + 0.92j
    sstart = 0 + 0.92j
    while True:
        t = utime.localtime()
        hrs.value(hstart * uv(-t[3] * pi / 6 - t[4] * pi / 360), YELLOW)
        mins.value(mstart * uv(-t[4] * pi / 30), YELLOW)
        secs.value(sstart * uv(-t[5] * pi / 30), RED)
        lbltim.value('{:02d}.{:02d}.{:02d}'.format(t[3], t[4], t[5]))
        dial.text('{} {} {} {}'.format(days[t[6]], t[2], months[t[1] - 1], t[0]))
        refresh(ssd)
        utime.sleep(1)


aclock()
