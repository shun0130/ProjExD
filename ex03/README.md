# 第3回
## 迷路ゲーム：迷えるこうかとん（ex03/maze.py）
### ゲーム概要
- ex03/maze.pyを実行すると，1500x900のcanvasに迷路が描画され，迷路に沿ってこ
うかとんを移動させるゲーム
- 実行するたびに迷路の構造は変化する
### 操作方法
- wキーでこうかとんを上に移動する
- aキーでこうかとんを左に移動する
- sキーでこうかとんを下に移動する
- dキーでこうかとんを右に移動する
### 追加機能
- スタート地点とゴール地点の追加：スタート地点をランダムに決定し，ゴール地点をスタートから最も遠い場所に設定する機能を追加した．
- wキー、aキー、sキー、dキー で移動できるようにした。
  壁の色を青色に変えた。(maze_makerの方を変えました。)
### ToDo（実装しようと思ったけど時間がなかった）
- [ ] 自動
- スタート地点とゴール地点、現在地点の色を変えたかった。
- 通ったところに色を付けたかったです。