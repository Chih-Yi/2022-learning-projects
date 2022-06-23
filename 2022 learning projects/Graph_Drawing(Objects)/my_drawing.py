"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


def main():
    """
    TODO:
    Title: Jerry Mouse (easy version)
    I am Jerry, and my teacher is Jerry. I also belong mouth in the Chinese yearly representation.
    Thus I intended in draw Jerry mouse.
    However, it's too hard.....
    """
    # head and ear
    window = GWindow(800,800)
    ear1 = GOval(200, 300)
    ear1.filled = True
    ear1.fill_color = 'orange'
    ear1.color = 'orange'
    inner_ear1 = GOval(180, 280)
    inner_ear1.filled = True
    inner_ear1.fill_color = 'pink'
    inner_ear1.color = 'pink'

    ear2 = GOval(200, 300)
    ear2.filled = True
    ear2.fill_color = 'orange'
    ear2.color = 'orange'
    inner_ear2 = GOval(180, 280)
    inner_ear2.filled = True
    inner_ear2.fill_color = 'pink'
    inner_ear2.color = 'pink'

    head = GOval(600, 600)
    head.filled = True
    head.fill_color = 'orange'
    head.color = 'orange'

    window.add(ear1, window.width/2 - head.width/2 - ear1.width/2, 20)
    window.add(ear2, window.width/2 + head.width/2 - ear1.width/2, 20)
    window.add(inner_ear1, ear1.x + (ear1.width-inner_ear1.width), ear1.y + (ear1.height-inner_ear1.height))
    window.add(inner_ear2, ear2.x, ear2.y + (ear2.height - inner_ear2.height))
    window.add(head, window.width / 2 - head.width / 2, 100)

    # face
    eye1 = GOval(150, 200)
    eye1.filled = True
    eye1.fill_color = 'white'
    eye1.color =  'white'
    inner_eye1 = GOval(75, 100)
    inner_eye1.filled = True
    inner_eye1.fill_color = 'black'
    inner_eye1.color = 'black'

    eye2 = GOval(150, 200)
    eye2.filled = True
    eye2.fill_color = 'white'
    eye2.color =  'white'
    inner_eye2 = GOval(75, 100)
    inner_eye2.filled = True
    inner_eye2.fill_color = 'black'
    inner_eye2.color = 'black'

    window.add(eye1, head.x + head.width/3 - eye1.width/2, head.y + head.height/4)
    window.add(eye2, head.x + head.width*2 / 3 - eye1.width / 2, head.y + head.height / 4)
    window.add(inner_eye1, eye1.x + (eye1.width - inner_eye1.width), eye1.y + (eye1.height/3))
    window.add(inner_eye2, eye2.x, eye2.y + (eye2.height/3))

    # nose and mouth
    nose = GOval(350, 150)
    nose.filled = True
    nose.fill_color = 'brown'
    nose.color = 'brown'
    window.add(nose, eye1.x, eye2.y + (eye2.height*2 / 3))
    nose_tip = GPolygon()
    nose_tip.add_vertex(((nose.x+nose.width/2), (nose.y+nose.height/3 + 75)))
    nose_tip.add_vertex((nose.x + nose.width / 2 - 50, nose.y + nose.height / 3))
    nose_tip.add_vertex((nose.x + nose.width / 2 + 50, nose.y + nose.height / 3))
    nose_tip.filled = True
    nose_tip.fill_color = 'black'
    nose_tip.color = 'black'
    window.add(nose_tip)

    mouth = GArc(350, 200, 0, -180)
    mouth.filled = True
    mouth.fill_color = 'red'
    mouth.color = 'red'
    window.add(mouth, nose.x, nose.y + nose.height)












if __name__ == '__main__':
    main()
