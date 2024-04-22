def process_text(input_text):
    # 入力テキストを行に分割する
    lines = input_text.strip().split('\n')
    
    # 出力を格納するためのリスト
    output = []
    
    # 現在の行番号を保持する変数
    current_line_num = ""
    
    # 各行を処理
    for line in lines:
        # "行目:"が含まれているかどうかをチェック
        if '行目:' in line:
            # 新しい行番号を更新
            current_line_num = line.split(':')[0]
        else:
            # 現在の行番号と行の内容を組み合わせて出力リストに追加
            output.append(f"{current_line_num}:{line}")
    
    return output



input_file = "test.txt"

# ファイルを開く
with open(input_file, 'r', encoding='utf-8') as file:
    # ファイルの内容を読み込む
    content = file.read()


# 処理関数を呼び出し
output_lines = process_text(content)

# 出力を表示
for line in output_lines:    
    print(line)
