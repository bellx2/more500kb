
from app import expand_image
import tempfile
import shutil
import pytest


def test_expand_image_png():
    with tempfile.NamedTemporaryFile(delete=True, suffix=".jpg") as tmp:
        shutil.copyfile("./test_image/18x26.png", tmp.name)
        img, file_size = expand_image(tmp.name)
        print(file_size)
        assert file_size > 500

        shutil.copyfile("./test_image/4x6.png", tmp.name)
        img, file_size = expand_image(tmp.name)
        print(file_size)
        assert file_size < 500


def test_expand_image_jpg():
    with tempfile.NamedTemporaryFile(delete=True, suffix=".jpg") as tmp:
        shutil.copyfile("./test_image/18x26.jpg", tmp.name)
        img, file_size = expand_image(tmp.name)
        print(file_size)
        assert file_size > 500

        shutil.copyfile("./test_image/4x6.jpg", tmp.name)
        img, file_size = expand_image(tmp.name)
        print(file_size)
        assert file_size < 500
