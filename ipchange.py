import requests

url = 'https://addressesapi.090227.xyz/CloudFlareYes'
response = requests.get(url)

# 确保请求成功
if response.status_code == 200:
    # 将文件内容存储到变量中
    file_content = response.content.decode('utf-8')  # 解码为字符串处理

    # 尝试读取本地文件并比较内容
    try:
        with open('yeqing.txt', 'r', encoding='utf-8') as file:
            local_content = file.read()
    except FileNotFoundError:
        local_content = None  # 如果文件不存在，设置本地内容为None

    # 如果本地文件内容与拉取内容不同或本地文件不存在，则进行修改和保存
    if local_content != file_content:
        # 对每行检查是否包含'#'，如果有，在'#'前加上":2053"
        modified_lines = []
        for line in file_content.splitlines(True):
            index = line.find('#')
            if index != -1:
                line = line[:index] + ':8443' + line[index:]
            modified_lines.append(line)
        modified_content = ''.join(modified_lines).encode('utf-8')  # 重新编码为二进制
        
        # 将修改后的内容保存到文件中
        with open('yeqing.txt', 'wb') as file:
            file.write(modified_content)
    else:
        print('No changes detected, ending execution.')
else:
    print('Failed to retrieve the file')
