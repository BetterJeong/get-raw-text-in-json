import json
import os


def extract_raw_text_from_json(json_file_path, output_text_file_path):
    # JSON 파일 읽기
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # raw_text 값 추출
    raw_texts = [item['raw_text'] for item in data.get('page_data')]

    return raw_texts


def process_all_json_files_in_directory(input_directory, output_text_file_path):
    # 디렉터리 내의 모든 JSON 파일 경로 가져오기
    json_files = [f for f in os.listdir(input_directory) if f.endswith('.json')]

    # 각 JSON 파일에서 raw_text 추출 및 텍스트 파일로 저장
    with open(output_text_file_path, 'w', encoding='utf-8') as text_file:
        for json_file in json_files:
            json_file_path = os.path.join(input_directory, json_file)
            raw_texts = extract_raw_text_from_json(json_file_path, output_text_file_path)
            for raw_text in raw_texts:
                text_file.write(raw_text + '\n')


input_directory = '.'
output_text_file_path = 'output.txt'

process_all_json_files_in_directory(input_directory, output_text_file_path)