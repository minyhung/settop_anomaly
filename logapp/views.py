# logapp/views.py
import logging
import time
import numpy as np
import pandas as pd
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.conf import settings
from threading import Thread
from .models import LogEntry

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# 데이터 로드 (절대 경로 사용)
df1 = pd.read_csv(r'C:\Users\USER\settop_0527.csv', index_col=0)

# 전역 변수로 로그 데이터 저장
log_data = []

# 로그 생성 함수
def log_random_samples_by_group(df, group_column, columns, interval=5, stop_event=None):
    global log_data
    while not (stop_event and stop_event.is_set()):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entries = []
        for group_name, group_df in df.groupby(group_column):
            random_samples = {column: np.random.choice(group_df[column].dropna().values) for column in columns}
            log_entries.append(f"Current_time: {current_time}, Group: {group_name}, Randomly sampled values: {random_samples}")
        
        for entry in log_entries:
            logger.info(entry)
            log_data.append(entry)  # 로그 데이터를 전역 변수에 저장
        
        time.sleep(interval)

def start_logging_thread():
    stop_event = getattr(settings, 'LOGGING_STOP_EVENT', None)
    if stop_event and stop_event.is_set():
        stop_event.clear()
    thread = Thread(target=log_random_samples_by_group, args=(df1, 'cell_number', ['upper_power2', 'upper_snr', 'lower_power', 'lower_snr'], 5, stop_event))
    thread.daemon = True
    thread.start()

def stop_logging_thread():
    stop_event = getattr(settings, 'LOGGING_STOP_EVENT', None)
    if stop_event:
        stop_event.set()

def index(request):
    start_logging_thread()
    return render(request, 'logapp/index.html')

@require_GET
# def get_log_data(request):
#     global log_data
#     # response_data = {'logs': log_data[-100:]}  # 마지막 10개의 로그 데이터만 반환
#     response_data = {'logs': log_data[]}
#     return JsonResponse(response_data)

def get_log_data(request):
    global log_data
    response_data = {'logs': log_data}  # 전체 로그 데이터 반환
    return JsonResponse(response_data)
