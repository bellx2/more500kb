import streamlit as st
from PIL import Image
import tempfile
import urllib.parse
import os

st.title("More 500KB")

st.write("謎制限で500KB以上の画像ファイルが必要なときに使うツールです。圧縮率を下げて画像を少しずつ拡大することで、500KB以上のJEPG画像を生成します。プレビューは拡張されたサイズのPNG画像を表示します。")
st.write("一時領域で処理するため管理者は画像を見ることはできません。")

image_file = st.file_uploader("画像をアップロード", type=['png', 'jpeg', 'jpg'])
if image_file is not None:
    file_details = {"FileName": image_file.name, "FileType": image_file.type}
    img = Image.open(image_file).convert('RGB')
    with tempfile.NamedTemporaryFile(delete=True, suffix=".jpg") as tmp:
        for i in range(5):
            img = img.resize(
                (int(img.size[0]*(1+i*0.2)), int(img.size[1]*(1+i*0.2))))
            img.save(tmp.name, quality=100)
            file_size = os.path.getsize(tmp.name)/1024
            if file_size > 500:
                break
        st.download_button(
            label="JPEG画像ダウンロード " + str(int(file_size)) + "KB",
            data=open(tmp.name, 'rb').read(),
            file_name=urllib.parse.quote(
                os.path.splitext(image_file.name)[0] + "_500k.jpg"),
            mime="image/jpeg"
        )
        st.image(img, caption="PNG画像", output_format='png')
