#https://github.com/tqdm/tqdm
from tqdm import tqdm
from time import sleep

for _ in tqdm(range(10000)):
    sleep(0.1)