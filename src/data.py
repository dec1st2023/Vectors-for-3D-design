import json
import csv
import yaml
import os
import numpy as np
from typing import Dict, Tuple, List, Any

def load_config(path: str) -> Dict[str, Any]:
    """
    从 YAML 文件加载配置。

    参数:
        path (str): YAML 配置文件路径。

    返回:
        Dict[str, Any]: 配置字典。
    """
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_endpoints(path: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    从配置文件（或特定端点文件）加载起点和终点。
    
    参数:
        path (str): 包含端点定义的文件路径。

    返回:
        Tuple[np.ndarray, np.ndarray]: (start_point, end_point) 形状为 (3,) 的 numpy 数组。
    """
    # 模拟返回，用于可运行的骨架
    return np.array([0.0, 0.0, 0.0]), np.array([10.0, 10.0, 10.0])

def load_control_points(path: str) -> np.ndarray:
    """
    从 JSON 文件加载控制点。

    参数:
        path (str): JSON 文件路径 (例如 input/points.json)。

    返回:
        np.ndarray: 形状为 (N, 3) 的控制点数组。
    """
    # 模拟返回
    return np.zeros((10, 3))

def load_interest_points(path: str) -> np.ndarray:
    """
    从文件加载关注点（目标场点）。

    参数:
        path (str): 文件路径。

    返回:
        np.ndarray: 形状为 (M, 3) 的关注点数组。
    """
    return np.zeros((5, 3))

def make_run_dir(base_dir: str, run_name: str) -> str:
    """
    为当前运行创建目录。

    参数:
        base_dir (str): 基础输出目录 (例如 "outputs")。
        run_name (str): 运行名称 (例如 时间戳)。

    返回:
        str: 创建的目录路径。
    """
    path = os.path.join(base_dir, run_name)
    os.makedirs(path, exist_ok=True)
    return path

def save_json(path: str, obj: Any) -> None:
    """
    将对象保存为 JSON 文件。

    参数:
        path (str): 输出文件路径。
        obj (Any): 要保存的对象。
    """
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)

def save_csv(path: str, rows: List[Dict[str, Any]]) -> None:
    """
    将字典列表保存为 CSV 文件。

    参数:
        path (str): 输出文件路径。
        rows (List[Dict[str, Any]]): 要保存的数据。
    """
    if not rows:
        return
    keys = rows[0].keys()
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)

def save_yaml(path: str, obj: Any) -> None:
    """
    将对象保存为 YAML 文件。

    参数:
        path (str): 输出文件路径。
        obj (Any): 要保存的对象。
    """
    with open(path, 'w') as f:
        yaml.dump(obj, f)
