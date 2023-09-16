import json
import os


def extract_raw_text_from_json(json_file_path):
    # JSON 파일 읽기
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # raw_text 값 추출
    raw_texts = [item['raw_text'] for item in data.get('page_data')]

    return raw_texts


def process_all_json_files_in_directory(input_directory, output_directory):
    # 모든 JSON 파일 경로 가져오기
    json_files = [f for f in os.listdir(input_directory) if f.endswith('.json')]

    for json_file in json_files:
        json_file_path = os.path.join(input_directory, json_file)
        raw_texts = extract_raw_text_from_json(json_file_path)

        # JSON 파일과 동일한 이름의 텍스트 파일 생성 및 저장
        base_filename = os.path.splitext(json_file)[0]
        output_text_file_path = os.path.join(output_directory, base_filename + '.txt')

        with open(output_text_file_path, 'w', encoding='utf-8') as text_file:
            for raw_text in raw_texts:
                text_file.write(raw_text + '\n')


input_directory = 'json_files'  # JSON 파일 경로
output_directory = 'text_files'  # 텍스트 파일 경로

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

process_all_json_files_in_directory(input_directory, output_directory)
