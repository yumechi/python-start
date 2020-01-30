import json
import argparse


def get_args():
    # https://docs.python.org/ja/3/library/argparse.html
    # argparseというもので簡単に取り出せます

    parser = argparse.ArgumentParser(description='メッセージを自動生成する')
    parser.add_argument('-d', '--data', type=str, required=True, help='json data')
    parser.add_argument('-t', '--template', type=str, required=True, help='template data')
    # count とかも足してみます
    parser.add_argument('-c', '--count', type=int, help='template data', default=1)
 
    return parser.parse_args()

def create_message(args):
    template = args.template
    data = args.data

    # ここをやっていきましょう

    message = "デフォルトメッセージ"

    with open(template, "r") as f:
        template_data = f.read()

    with open(data, "r") as f:
        json_data = json.load(f)

    template_data =  template_data.format(**json_data)

    return template_data

if __name__ == "__main__":
    args = get_args()
    count = args.count
    for i in range(count):
        print(create_message(args))
