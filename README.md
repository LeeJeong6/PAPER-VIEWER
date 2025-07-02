# PDF Translator Web App

PDF 파일을 업로드하고, PDF 원본과 텍스트를 좌우로 나누어 보여주며, 텍스트에서 드래그한 단어를 DeepL API를 이용해 번역하는 Flask 기반 웹 애플리케이션입니다


## 사용 방법
- https://www.deepl.com 에서 개인 API키를 받습니다(무료)
- app.py의 `DEEPL_API_KEY = 'YOUR_DEEPL_API_KEY'` 에 API키를 복붙합니다
- python app.py로 웹을 열고 pdf를 업로드하면 uploads폴더에 해당 pdf가 올라갑니다
- 텍스트에서 단어 드래그 시 바로 번역 결과 표시
- 오른쪽 상단에 번역된 단어는 계속해서 남습니다. -> 꺼도 계속 남아있음
## 예시
https://github.com/LeeJeong6/PAPER-VIEWER/issues/1#issue-3194750534



```bash
pip install -r requirements.txt
