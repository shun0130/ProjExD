import tkinter as tk #クラスtkが使えるようにインポートしている
import tkinter.messagebox as tkm # クラスtkmが使えるようにインポートしている


def button_click(event):
    btn = event.widget
    num = btn["text"]#クリックされたボタンの文字

    if num == "=":
        eqn = entry.get()
        result = eval(eqn) #eval関数で計算する
        entry.delete(0,tk.END) #もともとあった文字を消す。
        entry.insert(tk.END,result) #計算結果を表示する
    elif num == "C":#Cが押された時
        s = entry.get()
        entry.delete(len(s)-1,tk.END)
    elif num == "AC":
        entry.delete(0,tk.END)#ACが押された時

    else:
         entry.insert(tk.END,num)
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓") #タイトルの名前をつける

    entry = tk.Entry(root,justify = "right",width = 10,font=("Times New Roman",40)) #右側から入力されていく。
    entry.grid(row =0,column =0,columnspan=3,) #横方向に３マス結合

btn = tk.Button(root,
                width = 4,
                height = 2,
                font=("Times New Roman",30)
                        )
r, c = 1, 0 # 　r　:行番号　c　:列番号

for i,num in enumerate([9,8,7,"/",6,5,4,"*",3,2,1,"-",0,"C","AC","="]): #記号を追加して計算出来るようにした。
    btn = tk.Button(root,
                    text=f"{num}",
                    width = 4,
                    height = 2,
                    font=("Times New Roman",30)
                )
    btn.bind("<1>",button_click)
    btn.grid(row=r,column=c)

    c += 1
    if (i+1)%4 ==0: #横何列で表示するかの式
        r += 1
        c = 0


root.mainloop()