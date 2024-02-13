import json

def txt_to_json(input_file, output_file):
    words = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            # print(f"Processing line: {line.strip()}")  # 添加调试输出
            parts = line.strip().split('：')
            if len(parts) == 2:
                translation, word = parts[0].strip(), parts[1].strip()
                words.append({
                    "word": word,
                    "translations": [{
                        "translation": translation,
                        "type": ""
                    }]
                })

    json_data = {"words": words}

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_txt_file = "input.txt"  # 替换为您的文件路径
    output_json_file = "output.json"

    txt_to_json(input_txt_file, output_json_file)
    print(f"Conversion completed. Output saved to {output_json_file}")
