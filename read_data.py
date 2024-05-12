import numpy as np
import os

def save_npz_data_as_csv(file_path):
    try:
        # 从 npz 文件中加载数据
        npzfile = np.load(file_path)
        
        # 创建一个目录来保存 CSV 文件
        output_dir = os.path.splitext(file_path)[0] + "_csv"
        os.makedirs(output_dir, exist_ok=True)
        
        # 遍历并保存每个数组的数据为 CSV 文件
        for array_name in npzfile.files:
            # 获取数组数据
            array_data = npzfile[array_name]
            
            # 如果数组是3D的，将其展平为2D数组
            if len(array_data.shape) == 3:
                # 将3D数组展平为2D数组
                flattened_array = array_data.reshape(-1, array_data.shape[-1])
                csv_file_path = os.path.join(output_dir, array_name + ".csv")
                np.savetxt(csv_file_path, flattened_array, delimiter=",", fmt="%g")
                print("CSV file saved for array", array_name, ":", csv_file_path)
            else:
                # 如果数组是1D或2D的，直接保存为CSV文件
                csv_file_path = os.path.join(output_dir, array_name + ".csv")
                np.savetxt(csv_file_path, array_data, delimiter=",", fmt="%g")
                print("CSV file saved for array", array_name, ":", csv_file_path)
            
        print("CSV files saved successfully.")
        
    except Exception as e:
        print("Error:", e)

# 要读取的 npz 文件路径
npz_file_path = "./data/PEMS04/pems04.npz"

# 调用函数保存数据为 CSV
save_npz_data_as_csv(npz_file_path)
