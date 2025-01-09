## 멜론
- 멜론 차트 100위 조회

</br>

## 바이브
- 국내 급상승 100위 조회
- 해외 급상승 100위 조회

</br>

### default
- **install**

  <pre>
  <code>
  python3 -m venv .venv  
  </code>
  </pre>

  <pre>
  <code>
  poetry config virtualenvs.in-project true
  </code>
  </pre>

  <pre>
  <code>
  poetry env use python3
  </code>
  </pre>

  <pre>
  <code>
  poetry install
  </code>
  </pre>

- **.env**

  <pre>
  <code>
  DOWNLOAD_PATH = "my download path"
  </code>
  </pre>

</br>

### run
- **terminal**

  <pre>
  <code>
  cd app
  </code>
  </pre>

  <pre>
  <code>
  python3 crawling_melon_chart.py
  </code>
  </pre>