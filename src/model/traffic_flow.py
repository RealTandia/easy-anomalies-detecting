import csv
import numpy as np
from src.utils.draw import *


class Distance:
    def __init__(self, number, start_node, end_node, distance) -> None:
        self.number = number
        self.start_node = start_node
        self.end_node = end_node
        self.distance = distance 


class DetectorRecord:
    def __init__(self, detector_number, flow, occupancy, speed) -> None:
        self.detector_number = detector_number
        self.flow = flow
        self.occupancy = occupancy
        self.speed = speed


class DetectorRecords:
    records: list
    def __init__(self, time_count) -> None:
        self.time_count = time_count
        self.records = list()

    def append_record(self, record: DetectorRecord):
        self.records.append(record)


class TrafficFlowDataset:
    distance_data: list
    traffic_flow_data: list
    def __init__(self) -> None:
        self.distance_data = list()
        self.traffic_flow_data = list()
        self.time_interval = 0

    def load_dataset(self, csv_file_path, npz_file_path, time_interval, times):
        self.load_distance_data(csv_file_path)
        self.load_traffic_flow_data(npz_file_path, time_interval, times)

    def load_distance_data(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            road_count = 0
            for row in csv_reader:
                distance = Distance(road_count, row[0], row[1], row[2])
                self.distance_data.append(distance)
                road_count += 1
        print("distance data loaded")

    def load_traffic_flow_data(self, npz_file_path, time_interval, times):
        npzfile = np.load(npz_file_path)
        
        detector_datas = npzfile['data']
        
        time_count = 0
        for detector_data in detector_datas[0:times]:
            records = DetectorRecords(time_count)
            detector_count = 0
            for record_data in detector_data:
                detector_record = DetectorRecord(detector_count, record_data[0], record_data[1], record_data[2])
                records.append_record(detector_record)
                detector_count += 1
            self.traffic_flow_data.append(records)
            time_count += 1
        self.time_interval = time_interval
 
        print("traffic flow data loaded")


class TrafficFlow:
    traffic_flow_dataset: TrafficFlowDataset
    def __init__(self) -> None:
        self.traffic_flow_dataset = TrafficFlowDataset()

    def load_dataset(self, csv_file_path, npz_file_path, time_interval, times):
        self.traffic_flow_dataset.load_dataset(csv_file_path, npz_file_path, time_interval, times)

    # 动态邻域检测
    def dn_detecting(self, eps1, eps2, eps3, alpha):
        print('动态邻域检测尚未开发完全，请使用简易检测')

    # 简易检测
    def easy_detecting(self, k: float, road_num: int):
        detecting_result = list()
        for road in self.traffic_flow_dataset.distance_data:
            road_records = {
                "road": road.number,
                "road_records": []
            }
            road_start = road.start_node
            road_end = road.end_node
            for detectors_record in self.traffic_flow_dataset.traffic_flow_data:
                record_1 = detectors_record.records[int(road_start)]
                congestion = k * (record_1.flow * record_1.occupancy / record_1.speed)
                record_2 = detectors_record.records[int(road_end)]
                congestion += (1-k) * (record_2.flow * record_2.occupancy / record_2.speed)
                congestion_record = {
                    "time": detectors_record.time_count,
                    "congestion": congestion
                }
                road_records["road_records"].append(congestion_record)
            detecting_result.append(road_records)
        draw_line_chart(detecting_result[0:road_num])
        save_as_csv(detecting_result[0:road_num])

