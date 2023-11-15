"""
File: my_drawing.py
Name: Ellie Tang
----------------------
This file generates a drawing picture by GObject.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GArc, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Kirby X stanCode

    I made a poster of my favorite character with stanCode.
    """
    window = GWindow(width=600, height=800, title='Kirby X stanCode')

    # rectangles
    rect1 = GRect(150, 150, x=75, y=75)
    rect1.filled = True
    rect1.fill_color = 'mistyrose'
    rect1.color = 'mistyrose'
    window.add(rect1)

    rect2 = GRect(150, 150, x=225, y=75)
    rect2.filled = True
    rect2.fill_color = 'palevioletred'
    rect2.color = 'palevioletred'
    window.add(rect2)

    rect3 = GRect(150, 150, x=375, y=75)
    rect3.filled = True
    rect3.fill_color = 'rosybrown'
    rect3.color = 'rosybrown'
    window.add(rect3)

    rect4 = GRect(150, 150, x=75, y=225)
    rect4.filled = True
    rect4.fill_color = 'rosybrown'
    rect4.color = 'rosybrown'
    window.add(rect4)

    rect5 = GRect(150, 150, x=225, y=225)
    rect5.filled = True
    rect5.fill_color = 'mistyrose'
    rect5.color = 'mistyrose'
    window.add(rect5)

    rect6 = GRect(150, 150, x=375, y=225)
    rect6.filled = True
    rect6.fill_color = 'lightpink'
    rect6.color = 'lightpink'
    window.add(rect6)

    rect7 = GRect(150, 150, x=75, y=375)
    rect7.filled = True
    rect7.fill_color = 'lightpink'
    rect7.color = 'lightpink'
    window.add(rect7)

    rect8 = GRect(150, 150, x=225, y=375)
    rect8.filled = True
    rect8.fill_color = 'palevioletred'
    rect8.color = 'palevioletred'
    window.add(rect8)

    rect9 = GRect(150, 150, x=375, y=375)
    rect9.filled = True
    rect9.fill_color = 'mistyrose'
    rect9.color = 'mistyrose'
    window.add(rect9)

    # texts
    label1 = GLabel('stanCode')
    label1.color = 'black'
    label1.font = 'Helvetica-40-bold'
    window.add(label1, x=345, y=600)

    label2 = GLabel('2023')
    label2.color = 'black'
    label2.font = 'Helvetica-36-bold'
    window.add(label2, x=445, y=640)

    label2 = GLabel('from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GArc, GPolygon')
    label2.color = 'black'
    label2.font = 'Times New Roman-8'
    window.add(label2, x=245, y=655)

    label3 = GLabel('from campy.graphics.gwindow import GWindow')
    label3.color = 'black'
    label3.font = 'Times New Roman-8'
    window.add(label3, x=366, y=665)

    label4 = GLabel('my_drawing.py')
    label4.color = 'black'
    label4.font = 'Times New Roman-8'
    window.add(label4, x=474, y=675)

    # bottom
    line1 = GLine(150, 725, 525, 725)
    line1.color = 'black'
    window.add(line1)

    line2 = GLine(150, 730, 525, 730)
    line2.color = 'black'
    window.add(line2)

    label = GLabel('since 2019')
    label.color = 'black'
    label.font = 'Times New Roman-12'
    window.add(label, x=75, y=735)

    # kirby_1
    k1_feet_l = GArc(30, 45, 110, 270)
    k1_feet_l.filled = True
    k1_feet_l.fill_color = 'firebrick'
    k1_feet_l.color = 'firebrick'
    window.add(k1_feet_l, 260, 290)

    k1_feet_r = GArc(30, 45, 110, 270)
    k1_feet_r.filled = True
    k1_feet_r.fill_color = 'firebrick'
    k1_feet_r.color = 'firebrick'
    window.add(k1_feet_r, 300, 300)

    k1_body = GOval(75, 75, x=265, y=250)
    k1_body.filled = True
    k1_body.fill_color = 'pink'
    k1_body.color = 'pink'
    window.add(k1_body)

    k1_hand_l = GArc(25, 45, 0, 270)
    k1_hand_l.filled = True
    k1_hand_l.fill_color = 'pink'
    k1_hand_l.color = 'pink'
    window.add(k1_hand_l, 260, 245)

    k1_hand_r = GArc(27, 43, 220, 280)
    k1_hand_r.filled = True
    k1_hand_r.fill_color = 'pink'
    k1_hand_r.color = 'pink'
    window.add(k1_hand_r, 325, 273)

    k1_eye_l = GOval(10, 15, x=285, y=265)
    k1_eye_l.filled = True
    k1_eye_l.fill_color = 'black'
    k1_eye_l.color = 'black'
    window.add(k1_eye_l)

    k1_eye_l_1 = GOval(4, 7, x=287, y=266)
    k1_eye_l_1.filled = True
    k1_eye_l_1.fill_color = 'white'
    k1_eye_l_1.color = 'white'
    window.add(k1_eye_l_1)

    k1_eye_l_2 = GOval(3, 3, x=287, y=274)
    k1_eye_l_2.filled = True
    k1_eye_l_2.fill_color = 'blue'
    k1_eye_l_2.color = 'blue'
    window.add(k1_eye_l_2)

    k1_eye_r = GOval(10, 15, x=305, y=265)
    k1_eye_r.filled = True
    k1_eye_r.fill_color = 'black'
    k1_eye_r.color = 'black'
    window.add(k1_eye_r)

    k1_eye_r_1 = GOval(4, 7, x=307, y=266)
    k1_eye_r_1.filled = True
    k1_eye_r_1.fill_color = 'white'
    k1_eye_r_1.color = 'white'
    window.add(k1_eye_r_1)

    k1_eye_r_2 = GOval(3, 3, x=307, y=274)
    k1_eye_r_2.filled = True
    k1_eye_r_2.fill_color = 'blue'
    k1_eye_r_2.color = 'blue'
    window.add(k1_eye_r_2)

    k1_mouth = GOval(5, 8, x=298, y=285)
    k1_mouth.filled = True
    k1_mouth.fill_color = 'maroon'
    k1_mouth.color = 'maroon'
    window.add(k1_mouth)

    k1_blush_l = GOval(8, 5, x=275, y=282)
    k1_blush_l.filled = True
    k1_blush_l.fill_color = 'tomato'
    k1_blush_l.color = 'tomato'
    window.add(k1_blush_l)

    k1_blush_r = GOval(8, 5, x=319, y=282)
    k1_blush_r.filled = True
    k1_blush_r.fill_color = 'tomato'
    k1_blush_r.color = 'tomato'
    window.add(k1_blush_r)

    # kirby_2
    k2_feet_l = GArc(30, 45, 180, 300)
    k2_feet_l.filled = True
    k2_feet_l.fill_color = 'firebrick'
    k2_feet_l.color = 'firebrick'
    window.add(k2_feet_l, 430, 450)

    k2_body = GOval(100, 100, x=365, y=390)
    k2_body.filled = True
    k2_body.fill_color = 'pink'
    k2_body.color = 'pink'
    window.add(k2_body)

    k2_hand_l = GArc(35, 45, 0, 270)
    k2_hand_l.filled = True
    k2_hand_l.fill_color = 'pink'
    k2_hand_l.color = 'pink'
    window.add(k2_hand_l, 364, 392)

    k2_hand_r = GArc(50, 40, 220, 280)
    k2_hand_r.filled = True
    k2_hand_r.fill_color = 'pink'
    k2_hand_r.color = 'pink'
    window.add(k2_hand_r, 428, 390)

    k2_eye_l = GOval(10, 20, x=383, y=415)
    k2_eye_l.filled = True
    k2_eye_l.fill_color = 'black'
    k2_eye_l.color = 'black'
    window.add(k2_eye_l)

    k2_eye_l_1 = GOval(4, 7, x=384, y=417)
    k2_eye_l_1.filled = True
    k2_eye_l_1.fill_color = 'white'
    k2_eye_l_1.color = 'white'
    window.add(k2_eye_l_1)

    k2_eye_l_2 = GOval(3, 3, x=385, y=425)
    k2_eye_l_2.filled = True
    k2_eye_l_2.fill_color = 'blue'
    k2_eye_l_2.color = 'blue'
    window.add(k2_eye_l_2)

    k2_eye_r = GOval(10, 20, x=407, y=415)
    k2_eye_r.filled = True
    k2_eye_r.fill_color = 'black'
    k2_eye_r.color = 'black'
    window.add(k2_eye_r)

    k2_eye_r_1 = GOval(4, 7, x=408, y=417)
    k2_eye_r_1.filled = True
    k2_eye_r_1.fill_color = 'white'
    k2_eye_r_1.color = 'white'
    window.add(k2_eye_r_1)

    k2_eye_r_2 = GOval(3, 3, x=409, y=425)
    k2_eye_r_2.filled = True
    k2_eye_r_2.fill_color = 'blue'
    k2_eye_r_2.color = 'blue'
    window.add(k2_eye_r_2)

    k2_mouth_1 = GLabel(')   (', x=390, y=450)
    k2_mouth_1.color = 'black'
    window.add(k2_mouth_1)

    k2_mouth_2 = GLine(392, 442, 408, 442)
    k2_mouth_2.color = 'black'
    window.add(k2_mouth_2)

    k2_blush_l = GOval(15, 9, x=370, y=435)
    k2_blush_l.filled = True
    k2_blush_l.fill_color = 'tomato'
    k2_blush_l.color = 'tomato'
    window.add(k2_blush_l)

    k2_blush_r = GOval(15, 9, x=415, y=435)
    k2_blush_r.filled = True
    k2_blush_r.fill_color = 'tomato'
    k2_blush_r.color = 'tomato'
    window.add(k2_blush_r)

    # kirby_3
    k3_feet_l = GArc(30, 45, 30, 300)
    k3_feet_l.filled = True
    k3_feet_l.fill_color = 'firebrick'
    k3_feet_l.color = 'firebrick'
    window.add(k3_feet_l, 144, 143)

    k3_feet_r = GArc(30, 45, 150, 270)
    k3_feet_r.filled = True
    k3_feet_r.fill_color = 'firebrick'
    k3_feet_r.color = 'firebrick'
    window.add(k3_feet_r, 207, 157)

    k3_body = GOval(90, 90, x=150, y=100)
    k3_body.filled = True
    k3_body.fill_color = 'pink'
    k3_body.color = 'pink'
    window.add(k3_body)

    k3_hand_l = GArc(40, 35, 350, 350)
    k3_hand_l.filled = True
    k3_hand_l.fill_color = 'pink'
    k3_hand_l.color = 'pink'
    window.add(k3_hand_l, 135, 115)

    k3_hand_r = GArc(40, 35, 220, 280)
    k3_hand_r.filled = True
    k3_hand_r.fill_color = 'pink'
    k3_hand_r.color = 'pink'
    window.add(k3_hand_r, 218, 105)

    k3_eye_l = GOval(10, 20, x=187, y=120)
    k3_eye_l.filled = True
    k3_eye_l.fill_color = 'black'
    k3_eye_l.color = 'black'
    window.add(k3_eye_l)

    k3_eye_l_1 = GOval(4, 7, x=189, y=122)
    k3_eye_l_1.filled = True
    k3_eye_l_1.fill_color = 'white'
    k3_eye_l_1.color = 'white'
    window.add(k3_eye_l_1)

    k3_eye_l_2 = GOval(3, 3, x=190, y=131)
    k3_eye_l_2.filled = True
    k3_eye_l_2.fill_color = 'blue'
    k3_eye_l_2.color = 'blue'
    window.add(k3_eye_l_2)
    #
    k3_eye_r = GOval(10, 20, x=210, y=120)
    k3_eye_r.filled = True
    k3_eye_r.fill_color = 'black'
    k3_eye_r.color = 'black'
    window.add(k3_eye_r)
    #
    k3_eye_r_1 = GOval(4, 7, x=212, y=122)
    k3_eye_r_1.filled = True
    k3_eye_r_1.fill_color = 'white'
    k3_eye_r_1.color = 'white'
    window.add(k3_eye_r_1)

    k3_eye_r_2 = GOval(3, 3, x=213, y=131)
    k3_eye_r_2.filled = True
    k3_eye_r_2.fill_color = 'blue'
    k3_eye_r_2.color = 'blue'
    window.add(k3_eye_r_2)

    k3_mouth_1 = GOval(40, 43, x=183, y=140)
    k3_mouth_1.filled = True
    k3_mouth_1.fill_color = 'darkred'
    k3_mouth_1.color = 'darkred'
    window.add(k3_mouth_1)

    k3_mouth_2 = GOval(30, 36, x=183, y=144)
    k3_mouth_2.filled = True
    k3_mouth_2.fill_color = 'indianred'
    k3_mouth_2.color = 'darkred'
    window.add(k3_mouth_2)

    k3_blush_l = GOval(15, 9, x=171, y=140)
    k3_blush_l.filled = True
    k3_blush_l.fill_color = 'tomato'
    k3_blush_l.color = 'tomato'
    window.add(k3_blush_l)

    k3_blush_r = GOval(15, 9, x=222, y=140)
    k3_blush_r.filled = True
    k3_blush_r.fill_color = 'tomato'
    k3_blush_r.color = 'tomato'
    window.add(k3_blush_r)

    # waddle
    waddle_feet_l = GArc(40, 25, 120, 300)
    waddle_feet_l.filled = True
    waddle_feet_l.fill_color = 'orange'
    waddle_feet_l.color = 'orange'
    window.add(waddle_feet_l, 90, 315)

    waddle_feet_r = GArc(40, 25, 170, 280)
    waddle_feet_r.filled = True
    waddle_feet_r.fill_color = 'orange'
    waddle_feet_r.color = 'orange'
    window.add(waddle_feet_r, 130, 315)

    waddle_hand_l = GArc(45, 35, 70, 220)
    waddle_hand_l.filled = True
    waddle_hand_l.fill_color = 'darkorange'
    waddle_hand_l.color = 'darkorange'
    window.add(waddle_hand_l, 86, 283)

    waddle_hand_r = GArc(45, 35, 160, 330)
    waddle_hand_r.filled = True
    waddle_hand_r.fill_color = 'darkorange'
    waddle_hand_r.color = 'darkorange'
    window.add(waddle_hand_r, 130, 283)

    waddle_body_1 = GOval(60, 60, x=100, y=260)
    waddle_body_1.filled = True
    waddle_body_1.fill_color = 'darkorange'
    waddle_body_1.color = 'darkorange'
    window.add(waddle_body_1)

    waddle_body_2 = GOval(80, 60, x=90, y=275)
    waddle_body_2.filled = True
    waddle_body_2.fill_color = 'darkorange'
    waddle_body_2.color = 'darkorange'
    window.add(waddle_body_2)

    waddle_body_3 = GOval(50, 60, x=105, y=265)
    waddle_body_3.filled = True
    waddle_body_3.fill_color = 'linen'
    waddle_body_3.color = 'linen'
    window.add(waddle_body_3)

    waddle_body_4 = GOval(65, 40, x=98, y=287)
    waddle_body_4.filled = True
    waddle_body_4.fill_color = 'linen'
    waddle_body_4.color = 'linen'
    window.add(waddle_body_4)

    waddle_eye_l = GOval(8, 15, x=117, y=278)
    waddle_eye_l.filled = True
    waddle_eye_l.fill_color = 'black'
    waddle_eye_l.color = 'black'
    window.add(waddle_eye_l)

    waddle_eye_l_1 = GOval(3, 5, x=119, y=279)
    waddle_eye_l_1.filled = True
    waddle_eye_l_1.fill_color = 'white'
    waddle_eye_l_1.color = 'white'
    window.add(waddle_eye_l_1)

    waddle_eye_r = GOval(8, 15, x=134, y=278)
    waddle_eye_r.filled = True
    waddle_eye_r.fill_color = 'black'
    waddle_eye_r.color = 'black'
    window.add(waddle_eye_r)

    waddle_eye_r_1 = GOval(3, 5, x=136, y=279)
    waddle_eye_r_1.filled = True
    waddle_eye_r_1.fill_color = 'white'
    waddle_eye_r_1.color = 'white'
    window.add(waddle_eye_r_1)

    waddle_blush_l = GOval(15, 9, x=103, y=295)
    waddle_blush_l.filled = True
    waddle_blush_l.fill_color = 'darkorange'
    waddle_blush_l.color = 'darkorange'
    window.add(waddle_blush_l)

    waddle_blush_r = GOval(15, 9, x=140, y=295)
    waddle_blush_r.filled = True
    waddle_blush_r.fill_color = 'darkorange'
    waddle_blush_r.color = 'darkorange'
    window.add(waddle_blush_r)

    # cloud
    cloud_a_1 = GOval(45, 30, x=80, y=430)
    cloud_a_1.filled = True
    cloud_a_1.fill_color = 'white'
    cloud_a_1.color = 'white'
    window.add(cloud_a_1)

    cloud_a_2 = GOval(105, 45, x=67, y=440)
    cloud_a_2.filled = True
    cloud_a_2.fill_color = 'white'
    cloud_a_2.color = 'white'
    window.add(cloud_a_2)

    cloud_a_3 = GOval(40, 30, x=75, y=460)
    cloud_a_3.filled = True
    cloud_a_3.fill_color = 'white'
    cloud_a_3.color = 'white'
    window.add(cloud_a_3)

    cloud_a_4 = GOval(50, 30, x=100, y=465)
    cloud_a_4.filled = True
    cloud_a_4.fill_color = 'white'
    cloud_a_4.color = 'white'
    window.add(cloud_a_4)

    cloud_a_5 = GOval(45, 30, x=110, y=430)
    cloud_a_5.filled = True
    cloud_a_5.fill_color = 'white'
    cloud_a_5.color = 'white'
    window.add(cloud_a_5)

    cloud_b_1 = GOval(200, 50, x=275, y=490)
    cloud_b_1.filled = True
    cloud_b_1.fill_color = 'white'
    cloud_b_1.color = 'white'
    window.add(cloud_b_1)

    cloud_b_2 = GOval(80, 30, x=290, y=480)
    cloud_b_2.filled = True
    cloud_b_2.fill_color = 'white'
    cloud_b_2.color = 'white'
    window.add(cloud_b_2)

    cloud_b_3 = GOval(100, 35, x=350, y=480)
    cloud_b_3.filled = True
    cloud_b_3.fill_color = 'white'
    cloud_b_3.color = 'white'
    window.add(cloud_b_3)

    cloud_c_1 = GOval(160, 50, x=400, y=300)
    cloud_c_1.filled = True
    cloud_c_1.fill_color = 'white'
    cloud_c_1.color = 'white'
    window.add(cloud_c_1)

    cloud_c_2 = GOval(60, 30, x=420, y=290)
    cloud_c_2.filled = True
    cloud_c_2.fill_color = 'white'
    cloud_c_2.color = 'white'
    window.add(cloud_c_2)

    cloud_c_3 = GOval(70, 30, x=470, y=290)
    cloud_c_3.filled = True
    cloud_c_3.fill_color = 'white'
    cloud_c_3.color = 'white'
    window.add(cloud_c_3)

    cloud_c_4 = GOval(60, 25, x=417, y=332)
    cloud_c_4.filled = True
    cloud_c_4.fill_color = 'white'
    cloud_c_4.color = 'white'
    window.add(cloud_c_4)

    cloud_c_5 = GOval(60, 30, x=460, y=330)
    cloud_c_5.filled = True
    cloud_c_5.fill_color = 'white'
    cloud_c_5.color = 'white'
    window.add(cloud_c_5)

    # smoke
    smoke_1 = GArc(200, 40, 240, 150)
    smoke_1.color = 'white'
    window.add(smoke_1, x=235, y=125)

    smoke_2 = GArc(160, 40, 330, 150)
    smoke_2.color = 'white'
    window.add(smoke_2, x=235, y=170)

    smoke_3 = GArc(120, 40, 240, 150)
    smoke_3.color = 'white'
    window.add(smoke_3, x=245, y=110)

    # pieces
    pieces_1 = GPolygon()
    pieces_1.add_vertex((450, 100))
    pieces_1.add_vertex((440, 120))
    pieces_1.add_vertex((458, 125))
    pieces_1.add_vertex((465, 110))
    pieces_1.filled = True
    pieces_1.fill_color = 'lavenderblush'
    pieces_1.color = 'lavenderblush'
    window.add(pieces_1)

    pieces_2 = GOval(10, 10, x=400, y=120)
    pieces_2.filled = True
    pieces_2.fill_color = 'lavenderblush'
    pieces_2.color = 'lavenderblush'
    window.add(pieces_2)

    pieces_3 = GOval(7, 7, x=420, y=130)
    pieces_3.filled = True
    pieces_3.fill_color = 'lavenderblush'
    pieces_3.color = 'lavenderblush'
    window.add(pieces_3)

    pieces_4 = GPolygon()
    pieces_4.add_vertex((500, 160))
    pieces_4.add_vertex((480, 165))
    pieces_4.add_vertex((510, 170))
    pieces_4.add_vertex((450, 140))
    pieces_4.filled = True
    pieces_4.fill_color = 'lavenderblush'
    pieces_4.color = 'lavenderblush'
    window.add(pieces_4)

    pieces_5 = GPolygon()
    pieces_5.add_vertex((400, 160))
    pieces_5.add_vertex((380, 165))
    pieces_5.add_vertex((420, 170))
    pieces_5.add_vertex((410, 180))
    pieces_5.filled = True
    pieces_5.fill_color = 'lavenderblush'
    pieces_5.color = 'lavenderblush'
    window.add(pieces_5)

    pieces_6 = GOval(5, 5, x=450, y=180)
    pieces_6.filled = True
    pieces_6.fill_color = 'lavenderblush'
    pieces_6.color = 'lavenderblush'
    window.add(pieces_6)

    pieces_7 = GRect(6, 6, x=430, y=155)
    pieces_7.filled = True
    pieces_7.fill_color = 'lavenderblush'
    pieces_7.color = 'lavenderblush'
    window.add(pieces_7)

    pieces_8 = GOval(8, 8, x=450, y=160)
    pieces_8.filled = True
    pieces_8.fill_color = 'lavenderblush'
    pieces_8.color = 'lavenderblush'
    window.add(pieces_8)

    pieces_9 = GArc(100, 100, 180, 90)
    pieces_9.filled = True
    pieces_9.fill_color = 'lavenderblush'
    pieces_9.color = 'lavenderblush'
    window.add(pieces_9, x=500, y=50)

    pieces_10 = GRect(12, 12, x=480, y=120)
    pieces_10.filled = True
    pieces_10.fill_color = 'lavenderblush'
    pieces_10.color = 'lavenderblush'
    window.add(pieces_10)

    # decor
    decor_1 = GArc(70, 70, 90, 90)
    decor_1.color = 'darkgray'
    window.add(decor_1, x=245, y=235)

    decor_2 = GArc(90, 90, 90, 90)
    decor_2.color = 'darkgray'
    window.add(decor_2, x=233, y=227)

    decor_3 = GLabel('+')
    decor_3.color = 'white'
    decor_3.font = 'Verdana-18-bold'
    window.add(decor_3, x=160, y=270)

    decor_4 = GLabel('+')
    decor_4.color = 'white'
    decor_4.font = 'Verdana-18-bold'
    window.add(decor_4, x=180, y=250)

    decor_5 = GLabel('*')
    decor_5.color = 'darkgray'
    decor_5.font = 'Verdana-20-bold'
    window.add(decor_5, x=230, y=278)

    decor_5 = GLabel('*')
    decor_5.color = 'white'
    decor_5.font = 'Verdana-36-bold'
    window.add(decor_5, x=230, y=440)

    decor_6 = GLabel('*')
    decor_6.color = 'white'
    decor_6.font = 'Verdana-32-bold'
    window.add(decor_6, x=210, y=470)

    # circles
    cir = GOval(21, 54, x=317, y=409)
    cir.filled = True
    cir.fill_color = 'mistyrose'
    cir.color = 'palevioletred'
    window.add(cir)

    cir_1 = GOval(30, 65, x=300, y=400)
    cir_1.filled = True
    cir_1.fill_color = 'mistyrose'
    cir_1.color = 'palevioletred'
    window.add(cir_1)

    cir_2 = GOval(35, 75, x=285, y=390)
    cir_2.filled = True
    cir_2.fill_color = 'mistyrose'
    cir_2.color = 'palevioletred'
    window.add(cir_2)

    cir_3 = GOval(40, 85, x=270, y=380)
    cir_3.filled = True
    cir_3.fill_color = 'mistyrose'
    cir_3.color = 'palevioletred'
    window.add(cir_3)


if __name__ == '__main__':
    main()
