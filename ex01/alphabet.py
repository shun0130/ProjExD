import random
import datetime

hyouji = 5
taisyou = 10
kesson = 2

def main():
    st = datetime.datetime.now()
    for _ in range(hyouji):
        ans = shutudai()
        f = kaitou(ans)
        if f == 1:
            break
    ed = datetime.datetime.now()
    print(f"{(ed-st).seconds}秒かかりました")


def shutudai():
    alphabets = [chr(c+65) for c in range(26)]
    all_char_lst = random.sample(alphabets, taisyou)
    print(f"対象文字：{all_char_lst}")

    abs_char_lst = random.sample(all_char_lst,kesson)
    print(f"欠損文字：{abs_char_lst}")

    pre_char_lst = [c for c in all_char_lst if c not in abs_char_lst]
    print(f"表示文字：{pre_char_lst}")

    return abs_char_lst

def kaitou(seikai):
    num = int(input("欠損文字は何でしょうか？"))
    if num == kesson:
        print("不正解です")
        return 0
    else:
        print("正解です。それでは具体的に欠損文字を１つずつ入力してください")
        for i in range(kesson):
            c  = input(f"{i+1}つ目の文字を入力してください")
            if c not in seikai:
                print("不正解です。またチャレンジしてください")
                return 0
            seikai.remove(c)
        print("正解です。ゲームを終了します")  
        return 2
        
if __name__ == "__main__":
    main()
