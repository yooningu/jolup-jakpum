const express = require('express');
const app = express();
const fs = require('fs');
const https = require('https');

const options = {
  key: fs.readFileSync('server.key'),
  cert: fs.readFileSync('server.cert')
};

// 정적 파일 제공 설정
app.use(express.static('html'));  // 'html' 폴더를 정적 파일로 설정

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/html/index.html');  // 'index.html' 파일을 반환
});

https.createServer(options, app).listen(3000, () => {
  console.log('Server running on https://localhost:3000');
});
