import os
import time
import numpy as np
from src import data, geometry, constraints, model, optimizer
import src.math_lib

def main():
    # 1. 加载配置
    config_path = os.path.join("configs", "config.yaml")
    if not os.path.exists(config_path):
        print(f"未在 {config_path} 找到配置")
        return
        
    config = data.load_config(config_path)
    print("配置已加载。")

    # 2. 设置输出目录
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    run_name = f"case_{timestamp}"
    output_dir = data.make_run_dir(config.get("output_dir", "outputs"), run_name)
    print(f"已创建输出目录: {output_dir}")

    # 3. 加载输入
    # 在实际应用中，端点可能来自配置或文件
    endpoints = data.load_endpoints(config_path) 
    
    # 加载初始控制点或生成它们
    points_path = os.path.join("input", "points.json")
    if os.path.exists(points_path):
        control_points0 = data.load_control_points(points_path)
    else:
        # 如果文件丢失则回退
        control_points0 = np.zeros((config.get('n_modules', 10) + 1, 3))
    
    # 重采样以确保模块数量正确（如果从文件加载）
    # control_points0 = geometry.resample_to_n(control_points0, config.get('n_modules', 20))
    # 对于骨架，只需确保形状大致正确
    if control_points0 is None or len(control_points0) == 0:
         control_points0 = np.zeros((config.get('n_modules', 10) + 1, 3))

    print(f"初始控制点形状: {control_points0.shape}")

    # 4. 定义评估和惩罚函数
    # 这些包装器将特定模块函数适配到优化器接口
    
    obstacles = config.get('obstacles', []) # 占位符
    
    def eval_fn(cp):
        # 模拟关注点
        interest_points = np.zeros((10, 3)) 
        metrics = model.proxy_evaluate(cp, interest_points, config)
        # 从指标计算目标
        # margins = math_lib.margins_from_kpis(metrics, config.get('thresholds', {}))
        # f_proxy = math_lib.maximin_objective(margins)
        f_proxy = 0.0 # 模拟
        return f_proxy

    def penalty_fn(cp):
        return constraints.constraint_penalty(cp, obstacles, endpoints, config.get('weights', {}))

    # 5. 运行优化
    print("开始优化...")
    final_state = optimizer.optimize(
        control_points0, 
        eval_fn, 
        penalty_fn, 
        config
    )
    print(f"优化完成，共 {final_state.step} 步。")

    # 6. 保存输出
    # 保存最佳控制点
    best_cp_path = os.path.join(output_dir, "best_control_points.json")
    # 将 numpy 转换为 list 以进行 JSON 序列化
    data.save_json(best_cp_path, final_state.control_points.tolist())
    
    # 保存历史记录
    history_path = os.path.join(output_dir, "history.csv")
    data.save_csv(history_path, final_state.history)
    
    # 保存配置快照
    config_snap_path = os.path.join(output_dir, "config_snapshot.yaml")
    data.save_yaml(config_snap_path, config)
    
    print("结果已保存。")

if __name__ == "__main__":
    main()
