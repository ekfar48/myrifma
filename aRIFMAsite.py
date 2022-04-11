from flask import Flask, request, send_file
import os
app = Flask(__name__)

with open("//mypath//russian.txt","r", encoding='cp1251') as file:
    all_words = file.read().split('\n')
    file.close()

def rhyme(mass,word,chain=False):
    word = word[::-1]
    lenght = len(word)
    returned = []
    while lenght > 1:
        for i in mass:
            i = i[::-1].lower()
            if i == word:
                continue
            try:
                if i.startswith(word[:lenght]):
                    returned.append(i[::-1])                
            except IndexError:
                pass
        lenght -= 1
    if len(returned) >= 1:
        return returned
    #return "??DONT??FIND??"
    return "??MASSIVE??NULL??"

@app.route('/',methods=['post','get'])
def home_view():
    rhyme_word = 'привет'
    if request.method == 'POST':
        rhyme_word = request.form.get('username')
    return f"""
<html>
    <head>
        <meta charset="UTF-8">
        <title>Поиск рифм</title>
    </head>
    <body>
        <center><p>Введите в текстовое поле рифму</p></center>
    
    <center><form action="" method="post">
        <p>
	    <label for="username">Рифма</label>
	    <input type="text" name="username">
	</p>
	<p>
	    <input type="submit">
	</p>
    </center></form>
    <p>{rhyme(all_words,rhyme_word,True)}</p>
    </body>
</html>
"""

@app.route(f'/d/<string:file_ekfara>')
def download(file_ekfara):
    return send_file(f'//yy//'+file_ekfara)
    

if __name__ == "__main__":
        app.run()
