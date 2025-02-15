import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
from time import sleep

st.title("streamlit超入門")

# st.write("DataFrame")

# df = pd.DataFrame({"1列目": [1, 2, 3, 4], "2列目": [10, 20, 30, 40]})

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=300) # ...動的な表

# st.table(df) # ...静的な表

# マジックコマンド
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# 折れ線グラフ
# st.line_chart(df)
# 面グラフ
# st.area_chart(df)
# 棒グラフ
# st.bar_chart(df)

# マップをプロット
# df = pd.DataFrame(
#     np.random.randn(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# 画像の表示
# st.write('Display Image')

# img = Image.open('my-notion-face-transparent.png')
# st.image(img, caption='Ojizou', use_container_width=True)


## インタラクティブなウィジェット

# チェックボックス
# if st.checkbox('Show Image'):
#     img = Image.open('my-notion-face-transparent.png')
#     st.image(img, caption='Ojizou', use_container_width=True)

# セレクトボックス
# option = st.selectbox("好きな数字を教えて", list(range(1, 11)))
# "あなたの好きな数字は、", option, "です。"

# """
# ---
# """

# text = st.text_input("あなたの趣味を教えて")
# if text:
#     "あなたの趣味は、", text, "なのですね。"

# """
# ---
# """

# # スライダー
# num = st.slider("ラベル", 0, 100, 50)
# num

## レイアウト

# サイドバー
# text = st.sidebar.text_input("あなたの趣味を教えて")
# if text:
#     "あなたの趣味は、", text, "なのですね。"

# num = st.sidebar.slider("ラベル", 0, 100, 50)
# st.sidebar.write(num)

# 複数カラム
# left, right = st.columns(2)
# with left:
#     text = st.text_input("あなたの趣味を教えて")
#     if text:
#         "あなたの趣味は、", text, "なのですね。"
# button = left.button("右カラムに文字を表示")

# with right:
#     num = st.slider("ラベル", 0, 100, 50)
#     num

# if button:
#     right.write("こんにちは！")

# # expandar
# expander = st.expander('問い合わせ１')
# expander.write('問い合わせ１に対する回答')

## プログレスバー
button = st.button('Start')
latest_iteration = st.empty()
bar = st.progress(0)
if button:
    for i in range(100):
        latest_iteration.text(f'Iteration: {i + 1}')
        bar.progress(i + 1)
        sleep(0.1)
    button = False