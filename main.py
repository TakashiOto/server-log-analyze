import json
with open("sample.log","r",encoding="utf-8") as log_file:
    lines=log_file.readlines()

info_count=0
warning_count=0
error_count=0
error_messages={}

for line in lines:
    parts=line.strip().split(maxsplit=3)
    level=parts[2]
    if level == "INFO":
        info_count += 1
    elif level == "WARNING":
        warning_count += 1
    elif level == "ERROR":
        error_count += 1
        message=parts[3]
        if message in error_messages:
            error_messages[message]+=1
        else:
            error_messages[message]=1    
mce=""
hc=0
for message in error_messages:
    count=error_messages[message]
    if count>hc:
        hc=count
        mce=message

print(f"最も多い原因は{mce}で,回数は{hc}でした")

summary = {
    "total": len(lines),
    "info": info_count,
    "warning": warning_count,
    "error": error_count,
    "most_common_error": mce,
    "most_common_error_count": hc
}

with open("summary.json","w",encoding="utf8") as output_file:
    json.dump(summary,output_file,ensure_ascii=False,indent=2)
    