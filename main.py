"""Deterministic Dataset Sharder"""
import random

def partition_shards(dataset, num_shards=4, seed=42):
    random.seed(seed)
    shuffled = list(dataset)
    random.shuffle(shuffled)
    shards = [shuffled[i::num_shards] for i in range(num_shards)]
    return shards

if __name__ == "__main__":
    print("[RUN] Dataset Sharder...")
    data = list(range(100))
    shards = partition_shards(data, num_shards=4)
    print(f"[OK] Partitioned {len(data)} items into {len(shards)} shards ({len(shards[0])} items/shard).")
