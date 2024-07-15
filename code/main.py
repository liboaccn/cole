# from datasets import *
import argparse
import json
import os
from tqdm import tqdm
import sys
sys.path.append('utils/')

import llm
import config

if __name__ == '__main__':
    root_path = os.path.dirname(os.path.abspath(__file__))+'/../'

    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset','-d',
        type=str,
        default="COLE", 
        choices=config.datasets
    )
    parser.add_argument('--model', '-m',
        type=str,
        default="gpt-3.5", 
        choices=config.models
    )
    parser.add_argument('--temperature', '-t',
        type=str,
        default="0.9",
        choices=["0.3","0.6","0.9","0.5","0.7","0.8","0.4","1.2","1.5","1.0",
    ])
    parser.add_argument('--continues','-c',
        type=str,
        default="1", 
        choices=["1","0"]
    )
    args = parser.parse_args()
    dataset = args.dataset
    model_name = args.model
    temperature = args.temperature
    
    model = llm.init(model_name, temperature=float(temperature)).set_method('cole')
    
    dataset_path = root_path + 'datasets/test/'
    ref_path     = root_path + 'output/ref/'
    # test_dataset  = dataset_path + 'test/'+dataset+'.jsonl'
    sample_dataset  = ref_path + 'best_sample/'+dataset+'_res.jsonl'
    ref_dataset  = ref_path + 'best_law/'+dataset+'_res.jsonl'

    
    output_path = root_path + 'output/cole/'+model_name+'/'+temperature+'/'
    output_file = output_path + dataset +'.jsonl'


    ready_ids = []
    if 0 == int(args.continues):
        try:
            os.remove(output_file)
            print('Remove file: ' + output_file)
        except:
            print('File not exist: ' + output_file)
    else:
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                data = f.readlines()
                for item_str in data:
                    item = json.loads(item_str)
                    ready_ids.append(item['idx'])
        except:
            pass
    # print(ready_ids)

    
    # #读取sample
    ref_data = {}
    with open(ref_dataset, 'r', encoding='utf-8') as f:
        data = f.readlines()
        # print(data[0])
        for item_str in data:
            item = json.loads(item_str)
            ref_data[item['idx']] = item['best_ids']

    with open(sample_dataset, 'r', encoding='utf-8') as f:
        data = f.readlines()
        total = len(data)
    pbar = tqdm(total=int(total), desc='Progress', unit='item')
    #读取test
    with open(sample_dataset, 'r', encoding='utf-8') as f:
        data = f.readlines()
        # idx = 0
        for item_str in data:
            pbar.update(1)
            item = json.loads(item_str)
            # print(item['question'])
            idx = str(item['idx'])
            # break
            if idx in ready_ids:
                print('Skip: ' + str(idx))
                # idx += 1
                continue
            refs_data = {
                'sample': item['best_sample'],
                'ref': ref_data[idx]
            }
            # print(refs_data)
            response = llm.generate(model, dataset, refs_data, item['item'])
            # print(str(idx)+"_res:",response)
            if response == False:
                continue
            # print("res******", response)
            res_data = {
                'idx': str(idx),
                'response': response,
                'model': model_name,
                'dataset': dataset,
                'refs_data': refs_data,
                'item': item['item']
            }
            
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(res_data, ensure_ascii=False)+'\n')
            # idx += 1
            # break
    pbar.close()