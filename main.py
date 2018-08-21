import ui
import airplay
import objc_util

screen_connected = False

def score_up(sender):
    global score
    score += 1
    v['score'].text = str(score)
    if screen_connected:
        airplay_view['score'].text = str(score)


def score_down(sender):
    global score
    score -= 1
    v['score'].text = str(score)
    if screen_connected:
        airplay_view['score'].text = str(score)


v = ui.load_view()

v.present('sheet')
score = 0

UIScreen = objc_util.ObjCClass('UIScreen')
if len(UIScreen.screens()) > 1:
    screen_connected = True
    second_screen = UIScreen.screens()[1]

    bounds = second_screen.bounds()

    UIWindow = objc_util.ObjCClass('UIWindow')
    second_window = UIWindow.alloc().initWithFrame_(bounds)
    second_window.setScreen(second_screen)
    second_window.setHidden(False)

    airplay_view = airplay.load_view()
    airplay_view_objc = objc_util.ObjCInstance(airplay_view)
    airplay_view_objc.setFrame(second_window.bounds())
    second_window.addSubview(airplay_view_objc)
