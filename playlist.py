from flask import Flask, request, render_template

playlist = Flask(__name__)

@playlist.route('/')
def my_index():
    return render_template('index.html')

@playlist.route('/form', methods=['GET', 'POST'])
def func_form():
    if request.method == "POST":
       playlist = request.form["playlist"]
       processed_text = playlist.upper()
       with open('playlist.data', 'a') as fileObject:
           fileObject.write(str(f'{processed_text}\n'))
           fileObject.close()
    return render_template('form.html')

@playlist.route('/read', methods=['GET'])
def func_read():
    fileObject = open('playlist.data', 'r')
    fileContent = fileObject.read()
    lines = fileObject.readlines()
    fileObject.close()
    return render_template('read.html', fileContent=fileContent)

if __name__ == '__main__':
    playlist.run(debug=True)