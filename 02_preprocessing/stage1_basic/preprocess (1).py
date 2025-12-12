import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR:", BASE_DIR)

ANNO_DIR = os.path.join(BASE_DIR, "Anno")
EVAL_DIR = os.path.join(BASE_DIR, "Eval")

bbox_path = os.path.join(ANNO_DIR, "list_bbox_consumer2shop.txt")
item_path = os.path.join(ANNO_DIR, "list_item_consumer2shop.txt")
eval_path = os.path.join(EVAL_DIR, "list_eval_partition.txt")

print("Anno 존재:", os.path.exists(ANNO_DIR))
print("Eval 존재:", os.path.exists(EVAL_DIR))
print("bbox 존재:", os.path.exists(bbox_path))
print("item 존재:", os.path.exists(item_path))
print("eval 존재:", os.path.exists(eval_path))

out_csv = os.path.join(BASE_DIR, "out_datas.csv")

##########################
# 1) BBOX 읽기
##########################
cols = ['image_name','clothes_type','source_type','x1','y1','x2','y2']
df = pd.read_csv(bbox_path, sep=r"\s+", skiprows=2, names=cols)

df['image_name'] = df['image_name'].str.replace("comsumer","consumer", regex=False)

df['item_id'] = df['image_name'].str.extract(r"(id_\d+)")
df['type'] = df['source_type'].map({1:'shop', 2:'consumer'})

cons = df[df['type']=='consumer'][[
    'item_id','image_name','x1','y1','x2','y2'
]].rename(columns={
    'image_name':'consumer_path',
    'x1':'cons_x1','y1':'cons_y1','x2':'cons_x2','y2':'cons_y2'
})

shop = df[df['type']=='shop'][[
    'item_id','image_name','x1','y1','x2','y2'
]].rename(columns={
    'image_name':'shop_path',
    'x1':'shop_x1','y1':'shop_y1','x2':'shop_x2','y2':'shop_y2'
})

pairs = cons.merge(shop, on="item_id", how="inner")

##########################
# 2) eval 파일 파싱
##########################
eval_df = pd.read_csv(eval_path, sep=r"\s+", skiprows=2,
                      names=['consumer_path','shop_path','item_id','split'])

eval_df['consumer_path'] = eval_df['consumer_path'].str.replace("comsumer","consumer", regex=False)

##########################
# 3) split merge
##########################
pairs = pairs.merge(eval_df[['consumer_path','split']], on='consumer_path', how='left')
pairs['split'] = pairs['split'].fillna("train")

##########################
# 4) 저장 (bbox 포함)
##########################
pairs.to_csv(out_csv, index=False)

print("총 pair 수:", len(pairs))
print(pairs.head())
