from flask import Flask, render_template_string, request

app = Flask(__name__)

# Простая HTML-страница с чатом
HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Мини TG Chat</title>
  <meta charset="utf-8">
  <style>
    body { background:#1e1e1e; color:white; font-family:sans-serif; padding:20px; }
    h1 { text-align:center; }
    #chat { border:1px solid #444; padding:10px; height:300px; overflow:auto; background:#2b2b2b; }
    input, button { padding:8px; margin-top:10px; width:100%; }
  </style>
</head>
<body>
  <h1>🧭 Mini TG Chat</h1>
  <div id="chat"></div>
  <input type="text" id="msg" placeholder="Введите сообщение..." />
  <button onclick="send()">Отправить</button>

  <script>
    let chat = document.getElementById('chat');

    function send() {
      let text = document.getElementById('msg').value;
      if (text.trim() !== '') {
        let div = document.createElement('div');
        div.textContent = '👤 ' + text;
        chat.appendChild(div);
        document.getElementById('msg').value = '';
        chat.scrollTop = chat.scrollHeight;
      }
    }
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
