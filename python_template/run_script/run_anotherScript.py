'''run_anotherScript.py
    外部スクリプトを定義された引数で逐次実行する。
    実行対象のスクリプトと引数は設定ファイルに設定する。
'''

import subprocess
from datetime import datetime
from pathlib import Path

def connect_elements(args: list)-> str:
    connected_str = ""
    for elem in args:
        connected_str += f"{elem}"
    
    return(connected_str)

def check_valid_date(year: str, month: str, date: str)-> bool:
    ymd = f"{year}{month:02}{date:02}"

    try:
        datetime.strptime(ymd, "%Y%m%d")
    except ValueError:
        return(False)

    return(True)

def make_datetime_str()-> str:
    dt = datetime.now()
    datetime_str = f"{dt.year}{dt.month:02}{dt.day:02}{dt.hour:02}" + \
                   f"{dt.minute:02}{dt.second:02}"

    return(datetime_str)

def run_script(args_list):
    for args in args_list:
        proc = subprocess.Popen(args)
        proc.wait()

    return()

if __name__ == "__main__":
    import sys, logging, argparse, json
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
    if args.debug == True:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    log_filename = Path(sys.argv[0]).stem + "_" + make_datetime_str() + \
                        ".log"
    logging.basicConfig(level=log_level,
                        filename=log_filename,
                        format="%(asctime)s %(levelname)s: %(message)s")

    logging.info(f"START {sys.argv[0]}")

    # 設定ファイル検査
    conf_file = Path(args.conf)
    if conf_file.is_file() != True:
        print(f"{args.conf} isn't a file")
        logging.info(f"{args.conf} isn't a file")
        sys.exit()

    # 設定ファイル読込
    logging.info(f"loading the configuration file: {conf_file}")
    with open(conf_file, "r") as conf_fp:
        try:
            conf = json.load(conf_fp)
        except json.decoder.JSONDecodeError:
            print(f"{args.conf} contains invalid json format")
            logging.info(f"{args.conf} contains invalid json format")
            sys.exit()

    logging.debug(f"contents of the conf_file: \n{conf}")

    #   処理タイプ取得
    process_type = conf['process_type']

    #   スクリプト名取得
    tool_name = conf['tool_name']
    tool = Path(tool_name)
    if tool.is_file() != True:
        logging.info(f"[{tool}] isn't a file")
        sys.exit()
    logging.info(f"tool: {tool}")

    # サブプロセスで使用するpython
    py = sys.executable

    # 設定ファイルから引数取得 
    #   引数リストを生成する
    received_args = set()
    args_list = []
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

            logging.info("loaded a set of arguments ... "
                         f"tso_id: {tso_id}, year: {year}, "
                         f"month_start: {month_start}, "
                         f"month_end: {month_end}, "
                         f"date_start: {date_start}, date_end: {date_end}, "
                         f"voltage: {voltage}")

            # 引数リスト作成
            for month in range(month_start, month_end+1):
                for date in range(date_start, date_end+1):
                    if check_valid_date(year, month, date) != True:
                        logging.info(f"failed to convert: {year}"
                                     f"{month}{date}")
                        break
                    year_month = f"{year}{month:02}"
                    logging.info(f"{tso_id} {year_month} {date} {voltage}")

                    args = [py, tool, f'--ym={year_month}']
                    if process_type != 'sort_30min_data':
                        # 30分値仕分け以外の場合は下記を追加
                        args.append(f'--tso_id={tso_id}')
                        args.append(f'--date={date}')
                        args.append(f'--voltage={voltage}')

                    # コマンドの重複チェック
                    connected_elem = connect_elements(args)
                    if (connected_elem in received_args) == True:
                        logging.info(f"duplicated command was found. "
                                     "skipped")
                        break
                    else:
                        received_args.add(connected_elem)

                    args_list.append(args)


    # 引数リストを使って外部スクリプトを実行する
    logging.info("start run_script")
    #run_script(args_list)
    for args in args_list:
        logging.info(f"running with args: {args}")
        proc = subprocess.Popen(args)
        proc.wait()
        logging.info(f"finished running with args: {args}")

    logging.info("end run_script")

    sys.exit()
