import sys, argparse, time

# 引数を取得する
parser = argparse.ArgumentParser(
            prog='stub_script.py',
            description='stub script for run_anotherScript.py'
        )
parser.add_argument('-f', '--file', help='configuration file')
parser.add_argument('--tso_id')
parser.add_argument('--ym', default="202401")
parser.add_argument('--date', default="1")
parser.add_argument('--voltage')
args = parser.parse_args()

time.sleep(1)
print(f"received: {args.tso_id} {args.ym} {args.date}, "
      f"voltage[{args.voltage}]")

sys.exit()
