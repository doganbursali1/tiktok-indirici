from flask import Flask, request, send_file
import yt_dlp
import os
import time

app = Flask(__name__)

@app.route('/indir')
def indir():
    video_url = request.args.get('url')
    if not video_url:
        return "Lütfen bir URL gönderin", 400

    # Dosya ismini benzersiz yapıyoruz
    dosya_adi = f"video_{int(time.time())}.mp4"

    ydl_opts = {
        'outtmpl': dosya_adi,
        'format': 'bestvideo+bestaudio/best', # En iyi kalite
        'noplaylist': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            
        return send_file(dosya_adi, as_attachment=True)
        
    except Exception as e:
        return f"Hata: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
