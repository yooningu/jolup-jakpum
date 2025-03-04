from flask import Flask, send_from_directory
from flask_cors import CORS

# Flask 애플리케이션 초기화
app = Flask(__name__)

# CORS 활성화 (모든 출처에서 요청을 허용)
CORS(app)

# 리소스를 서빙할 경로 설정
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)