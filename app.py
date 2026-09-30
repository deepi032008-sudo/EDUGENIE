import google.generativeai as genai
from flask import Flask, request, jsonify

# INGA PUDHU API KEY-A PODU - AIza... nu varanum
genai.configure(api_key="enter your api key")

model = genai.GenerativeModel('gemini-3.5-flash')

app = Flask(__name__)

@app.route('/')
def home():
    return """<html><head><script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script></head>
<body style="background:#121212;color:white;font-family:Arial"><div style="max-width:600px;margin:auto">
<h2>EduGenie</h2><div id="chat" style="height:70vh;overflow:auto;background:#1a1a1a;padding:10px"></div>
<input id="q" style="width:70%;padding:10px"><button onclick="send()" style="padding:10px">Send</button>
<script>
async function send(){
 let q=document.getElementById('q').value; if(!q)return;
 let c=document.getElementById('chat'); c.innerHTML+=`<div>You: ${q}</div>`; document.getElementById('q').value='';
 let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:q})});
 let d=await r.json(); c.innerHTML+=`<div style="background:#222;padding:10px;margin:10px 0;border-radius:8px">${marked.parse(d.answer)}</div>`;
}
</script></div></body></html>"""

@app.route('/ask', methods=['POST'])
def ask():
    q = request.json['question']
    response = model.generate_content(q)
    return jsonify({'answer': response.text})

if __name__ == '__main__':
    app.run(debug=True)