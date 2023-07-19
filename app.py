from flask import Flask, request, render_template
from ml_model import classify_img
import os

app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400

        file = request.files['file']

        if file.filename == '':
            return 'No file selected', 400

        # Save the file to the uploads folder
        file.save(os.path.join('static/uploads', file.filename))

        # Call the classify_image function on the uploaded file
        result = classify_img(os.path.join('static/uploads', file.filename))
        
        # Display the result
        return render_template('result.html', filename=file.filename, result=result)

    #  enctype="multipart/form-data" : 사진이나 영상 같은 파일을 올릴 때는 binary 파일로 전달되기 때문에 
    # 파일명 등의 정보도 달아서 보냅니다. text + binary 파일이 섞여있음
    # 
    return '''
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

if __name__=='__main__':
    app.run()