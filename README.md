# Công cụ phân tích ngữ pháp

## Hướng dẫn cài đặt

- Cài python3 + pip3
- `pip3 install hanlp flask waitress`
- `python3 hanlp-srv.py`

## Gọi công cụ

Thông qua curl:

```sh
curl -X POST http://localhost:5555/mtl/1 -d "商品和服务。\n晓美焰来到北京立方庭参观自然语义科技公司"
```

Thông qua python:

```py
import requests

url = "http://localhost:5555/mtl/1"
data = "商品和服务。\n晓美焰来到北京立方庭参观自然语义科技公司"
headers = {"Content-Type": "text/plain"}

response = requests.post(url, data=data, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
```

`1 2 3` tương ứng với 3 model Electra Small, Electra Base và Ernie Gram. Càng về sau thì độ chính sác càng cao.

## Lưu ý:

- Lần đầu tiên chạy sẽ khá lâu vì phải tải file model xuống.
- Phải chia dòng theo từng câu văn mới đem lại tốc độ cao nhất.
