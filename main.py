# -*- coding: utf-8 -*-
import urllib.request
import json
import argparse
import base64


def api_key():
  with open('./resource/.env', 'r') as f:
    return f.read()


def main(photo_file):
  url = "https://vision.googleapis.com/v1/images:annotate?key=" + api_key()
  method = "POST"
  headers = {"Content-Type": "application/json"}
  with open(photo_file, 'rb') as image:
    image_content = base64.b64encode(image.read())
    param = {
      "requests":[
        {
          "image":{
            "content": image_content.decode('utf-8')
          },
          "features":[
            {
              "type":"TEXT_DETECTION",
              "maxResults":1
            }
          ]
        }
      ]
    }
    json_data = json.dumps(param).encode("utf-8")
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
      response_body = response.read().decode('utf-8')
      print(response_body)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--image_file', help='The image you\'d like to detect.')
  args = parser.parse_args()
  main(args.image_file)