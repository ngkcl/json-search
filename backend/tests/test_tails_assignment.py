import json
import orjson

# JSON Benchmarking tests ----------------

# Test json obj
m = {
    "timestamp": 1556283673.1523004,
    "task_uuid": "0ed1a1c3-050c-4fb9-9426-a7e72d0acfc7",
    "task_level": [1, 2, 1],
    "action_status": "started",
    "action_type": "main",
    "key": "value",
    "another_key": 123,
    "and_another": ["a", "b"],
}

def test_default_json_benchmark(benchmark):
    benchmark(json.dumps, m)

def test_orjson_benchmark(benchmark):
    benchmark(orjson.dumps, m)

# ========================================

