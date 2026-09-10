FROM python:3.12-slim

WORKDIR /bench
COPY . /bench

RUN pip install --no-cache-dir -e harness/

# 一条命令评测(挂载预测文件后):
# docker run --rm -v $PWD:/bench physical-ai-fusion \
#   physical-ai-fusion evaluate --predictions preds.jsonl --output results/results.json
ENTRYPOINT ["physical-ai-fusion"]
CMD ["stats"]
