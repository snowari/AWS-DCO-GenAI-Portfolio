import os
import glob
import re

def analyze_logs():
    # 스크립트가 위치한 폴더 기준으로 server*.log 파일 탐색
    log_dir = os.path.dirname(os.path.abspath(__file__))
    log_files = glob.glob(os.path.join(log_dir, "server*.log"))
    
    if not log_files:
        print(f"오류: {log_dir} 디렉토리에서 server*.log 파일을 찾을 수 없습니다.")
        return

    # 결과를 저장할 딕셔너리
    results = {}

    for file_path in sorted(log_files):
        file_name = os.path.basename(file_path)
        server_name = os.path.splitext(file_name)[0]
        
        crc_count = 0
        link_down_count = 0
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line_upper = line.upper()
                    # ERROR 등급의 로그만 카운트 대상으로 지정
                    if "ERROR" in line_upper:
                        if "CRC ERROR" in line_upper:
                            crc_count += 1
                        if "LINK DOWN" in line_upper:
                            link_down_count += 1
        except Exception as e:
            print(f"파일 {file_name}을 읽는 중 오류 발생: {e}")
            continue
            
        results[server_name] = {
            "crc_error": crc_count,
            "link_down": link_down_count
        }

    # 결과 테이블 출력
    print("=" * 50)
    print(f"{'서버명 (Server)':<15} | {'CRC Error 횟수':<12} | {'Link Down 횟수':<12}")
    print("-" * 50)
    for server, counts in sorted(results.items()):
        print(f"{server:<15} | {counts['crc_error']:<12} | {counts['link_down']:<12}")
    print("=" * 50)

if __name__ == "__main__":
    analyze_logs()
