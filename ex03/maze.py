import tkinter as tk
import maze_maker as mm


def key_down(event):# key_down関数の定義
    global key
    key = event.keysym
   # print(f"{key}キーが押されました .") 

def key_up(event):
    global key
    key = ""


    
def main_proc():
    global cx, cy,mx,my
    UP,DOWN,LEFT,RIGHT =range(4)
    KEY_DIC = {"w":UP,"a":LEFT,"s":DOWN,"d":RIGHT}
    delta = {#キー：押されているキーkey/値：移動幅リスト[x,y]
    "w"   :[0,-1],
                           "s" :[0,+1],
        "d":[+1,0],
        "a":[-1,0],
    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0: #もし移動先が床なら
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass

    #if maze_bg[][] == 0: #もし移動先が床なら
    #if key == "Up" : my -= 1
    #if key == "Down" : my += 1
    #if key == "Left" : my -= 1
    #if key == "Right" : my += 1
    cx,cy = mx*100+50,my*100+50
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)
    
if __name__ == "__main__":
    root =tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width =1500,height=900,bg ="black")
    canvas.pack()
    maze_bg = mm.make_maze(15,9) #1:壁/0:床を表す二次元リスト
    mm.show_maze(canvas,maze_bg) #
   # print(maze_bg)


    tori = tk.PhotoImage(file="fig/7.png")
    mx,my = 1,1
    cx,cy = mx*100+50,my*100+50
    canvas.create_image(cx,cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()
    root.mainloop()
        