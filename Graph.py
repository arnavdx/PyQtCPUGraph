import pyqtgraph as pg
import numpy as np
import subprocess

app=pg.mkQApp()
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
pen = pg.mkPen(color='r', width=1)
wid=pg.PlotWidget()
pg.setConfigOptions(antialias=True)
x=np.linspace(0,0,100)
wid.setLimits(xMin=0, xMax=100, yMin=0, yMax=100)
wid.setYRange(0, 100, padding=0)
wid.setXRange(0,100,padding=0)
wid.showGrid(x=True,y=True,alpha=0.1)
wid.hideAxis('bottom')
wid.setWindowTitle("CPU Usage")
wid.setTitle("CPU Usage(%)")
wid.plot(x,pen=pen)
wid.show()

timer = pg.QtCore.QTimer()
def update():
    global x
    x[:-1]=x[1:]
    command = "wmic cpu get loadpercentage"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    x[-1]=int(result.stdout.split()[1])
    wid.plot(x, clear=True,pen=pen, fillLevel=0, brush=(255,102,102,200))

timer.timeout.connect(update)
timer.setInterval(1000)
timer.start()
app.exec()