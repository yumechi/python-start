import json
import argparse


def get_args():
    # https://docs.python.org/ja/3/library/argparse.html
    # argparseというもので簡単に取り出せます

    parser = argparse.ArgumentParser(description='メッセージを自動生成する')
    parser.add_argument('-d', '--data', type=str, required=True, help='json data')
    parser.add_argument('-t', '--template', type=str, required=True, help='template data')
    # count とかも足してみます

    return parser.parse_args()

def create_message(args):
    template = args.template
    data = args.data

    # ここをやっていきましょう
    message = "デフォルトメッセージ"

    return message

if __name__ == "__main__":
    args = get_args()
    print(create_message(args))
