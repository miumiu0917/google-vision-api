# -*- coding: utf-8 -*-
import urllib.request
import json


def main():
  url = "https://vision.googleapis.com/v1/images:annotate"
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
              "type":"LABEL_DETECTION",
              "maxResults":1
            }
          ]
        }
      ]
    }
    json_data = json.dumps(param).encode("utf-8")
    request = url.request.Reauest(url, data=json, method=method, headers=headers)
    with urllib.request.urlopen(reques) as response:
      response_body = response.read().decode('utf-8')
      print(response_body)

if __name__ == '__main__':
  main()