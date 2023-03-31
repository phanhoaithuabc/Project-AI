import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument("-filepath", help="Path to submission file. Default: Softmax_Regression.ipynb",
                    default="Softmax_Regression.ipynb")
args = parser.parse_args()

URL = "http://34.87.169.149/judge/5/upload_file/"

if __name__ == "__main__":
    fin = open(args.filepath, 'rb')
    files = {'file': fin}
    try:
        data_obj = {'name': input('username: ')}
        r = requests.post(URL, files=files, data=data_obj)
        text = json.loads(r.text)
        print("\nYOUR SCORES:")
        print("\t"+"\n\t".join(text["message"].split("\n")))
        print("Total score: ", text["score"])
    finally:
        fin.close()