## Spot Instance N.Virginia
# g5.12xlarge
# default SG
# noharm-care role
# 450 GB
# pre-installed ami: 

## Install GPT-NeoX-20B HF
# source activate pytorch
# git clone https://github.com/mallorbc/GPTNeoX20B_HuggingFace.git
# cd GPTNeoX20B_HuggingFace/
# pip install accelerate transformers
# curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | sudo bash
# sudo yum install git-lfs
# git lfs install
# git clone https://huggingface.co/EleutherAI/gpt-neox-20b gptneox
# mv model.safetensors.index.json model.safetensors.index.json_
# python main.py

## Load Notes
# aws s3 sync s3://noharm-gehn/snapshot-23-03/converted-evolucoes/ ./converted/
# gunzip -c run-1680630492516-part-r-00062.gz | head | jq -c '.[]'  > output.jsonl
# gunzip -c run-1680630492516-part-r-00062.gz | head > output.jsonl
# gunzip -c run-1680630492516-part-r-00062.gz | wc -l
# sed -i 's/texto/text/g' output.jsonl
