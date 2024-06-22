'''run_anotherScript.py
    外部スクリプトを定義された引数で逐次実行する。
    実行対象のスクリプトと引数は設定ファイルに設定する。
'''

import sys, logging, argparse, json, subprocess
from datetime import datetime
from pathlib import Path

# 引数処理
#   設定ファイル取得
parser = argparse.ArgumentParser(
            prog=f'{sys.argv[0]}',
            description=f'stub script for {sys.argv[0]}'
        )
parser.add_argument('-d', '--debug', action='store_true')
parser.add_argument('-c', '--conf', required=True, \
                    help='configuration file')
args = parser.parse_args()

# ログ初期処理
#   ログファイル名生成（時分秒付き）
if args.debug == True:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO

print(log_level)

logging.basicConfig(level=log_level,
                    format="%(asctime)s %(levelname)s: %(message)s")

logging.info(f"START {sys.argv[0]}")

# 設定ファイル検査
conf_file = Path(args.conf)
if conf_file.is_file() != True:
    logging.info(f"{args.conf} isn't a file")
    sys.exit()

# 設定ファイル読込
logging.info(f"loading the configuration file: {conf_file}")
with open(conf_file, "r") as conf_fp:
    conf = json.load(conf_fp)

logging.debug(f"contents of the conf_file: \n{conf}")

#   スクリプト名取得
tool_name = conf['tool_name']
tool = Path(tool_name)
if tool.is_file() != True:
    logging.info(f"{tool} isn't a file")
    sys.exit()
logging.info(f"tool: {tool}")

# サブプロセスで使用するpython
py = sys.executable

# 設定ファイルから引数取得 
for tso_set in conf['tso_sets']:
    tso_id = tso_set['tso_id']
    voltage = tso_set['voltage']
    for term in tso_set['terms']:
        # スクリプト用の引数取得
        year = term['year']
        month_start = int(term['month']['start'])
        month_end = int(term['month']['end'])
        date_start = int(term['date']['start'])
        date_end = int(term['date']['end'])

        logging.info(f"tso_id: {tso_id}, year: {year}, "
                     f"month_start: {month_start}, month_end: {month_end}, "
                     f"date_start: {date_start}, date_end: {date_end}, "
                     f"voltage: {voltage}")

        # TODO: スクリプト実行
        for month in range(month_start, month_end+1):
            for date in range(date_start, date_end+1):
                ymd = f"{year}{month:02}{date:02}"
                try:
                    datetime.strptime(ymd, "%Y%m%d")
                except ValueError:
                    logging.info(f"failed to convert: {ymd}")
                    break
                year_month = f"{year}{month:02}"
                logging.info(f"{tso_id} {year_month} {date} {voltage}")
                proc = subprocess.Popen([py, tool, \
                                        f'--tso_id={tso_id}', \
                                        f'--year_month={year_month}', \
                                        f'--date={date}', \
                                        f'--voltage={voltage}'])
                proc.wait()

sys.exit()
