import streamlit as st
from PIL import Image
import tempfile
import urllib.parse
import os

st.title("More 500KB")

st.write("元画像の圧縮比率とサイズを変えて500KB以上の画像ファイルを生成します。画質は向上しません。")
st.write("アップロードデータは画像処理のために使用し、保存していません。")

image_file = st.file_uploader("画像をアップロードしてください", type=['png', 'jpeg', 'jpg'])
if image_file is not None:
    file_details = {"FileName": image_file.name, "FileType": image_file.type}
    img = Image.open(image_file).convert('RGB')
    with tempfile.NamedTemporaryFile(delete=True, suffix=".jpg") as tmp:
        for i in range(10):
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
        st.image(img, caption="PNG画像 長押しで保存", output_format='png')
