import streamlit as st
from PIL import Image
import tempfile
import urllib.parse
import os


def expand_image(file_path):
    img = Image.open(file_path).convert('RGB')
    for i in range(50):
        img = img.resize(
            (int(img.size[0]*1.2), int(img.size[1]*1.2)))
        # 100 disables portions of the JPEG compression algorithm
        img.save(file_path, quality=100)
        file_size = os.path.getsize(file_path)/1024  # KB
        if file_size > 500:
            break
    return img, file_size


st.title(":frame_with_picture: Over 500KB")
st.write("元画像の圧縮比率とサイズを変えて500KB以上の画像ファイルに変換します。画質は向上しません。アップロードデータは保存していません。")

image_file = st.file_uploader("画像をアップロードしてください", type=[
                              'png', 'jpeg', 'jpg'], accept_multiple_files=False)
if image_file is not None:
    file_details = {"FileName": image_file.name, "FileType": image_file.type}
    img = Image.open(image_file).convert('RGB')
    with tempfile.NamedTemporaryFile(delete=True, suffix=".jpg") as tmp:
        img.save(tmp.name, quality=100)
        img, file_size = expand_image(tmp.name)
        if file_size > 500:
            st.header("変換完了！ :grin:")
            st.download_button(
                label="JPEG形式 : クリックでダウンロード " + str(int(file_size)) + "KB",
                data=open(tmp.name, 'rb').read(),
                file_name=urllib.parse.quote(
                    os.path.splitext(image_file.name)[0] + "_500k.jpg"),
                mime="image/jpeg"
            )
            st.write("PNG形式 : 画像長押しで保存")
            st.image(img, output_format='png')
        else:
            st.header("変換失敗... :cry:")
            st.write("元画像サイズが小さすぎます。")
