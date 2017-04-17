from flask_wtf import Form
from flask_wtf.file import FileField


class UploadForm(Form):
    example = FileField()