from src.model.traffic_flow import TrafficFlow

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Process command line arguments")
    parser.add_argument("--distance-dataset", type=str, default="./data/PEMS04/distance.csv", help="distance dataset file path")
    parser.add_argument("--traffic-flow-dataset", type=str, default="./data/PEMS04/pems04.npz", help="traffic flow dataset file path")
    parser.add_argument("--time-interval", type=int, default=300, help="Time interval (default: 300)")
    parser.add_argument("--times", type=int, default=288, help="Number of times (default: 288)")
    parser.add_argument("--roads", type=int, default=4, help="Number of roads (default: 4)")
    parser.add_argument("--model", type=str, choices=["easy_detecting", "dn_detecting"], default="easy_detecting", help="model type")
    parser.add_argument("-k", type=int, default=0.5, help="Parameter k (required when model type is easy_detecting)")
    return parser.parse_args()

def main():
    args = parse_args()
    print("distance dataset file path:", args.distance_dataset)
    print("traffic flow dataset file path:", args.traffic_flow_dataset)
    print("Time interval:", args.time_interval)
    print("Number of times:", args.times)
    print("Number of roads:", args.roads)
    print("model:", args.model)
    if args.distance_dataset is None or args.traffic_flow_dataset is None:
        print("dataset file is required")
        exit(1)
    if args.model == "easy_detecting" and args.k is None:
        print("Parameter -k is required when detection model is easy_detecting")
        exit(1)

    trafficflow = TrafficFlow()
    trafficflow.load_dataset(csv_file_path=args.distance_dataset,
                             npz_file_path=args.traffic_flow_dataset,
                             time_interval=args.time_interval,
                             times=args.times)
    if args.model == "easy_detecting":
        trafficflow.easy_detecting(args.k, args.roads)
    elif args.model == "dn_detecting":
        trafficflow.dn_detecting(0, 0, 0, 0)

if __name__ == "__main__":
    main()

# trafficflow = TrafficFlow()
# trafficflow.load_dataset(csv_file_path='./data/PEMS04/distance.csv',
#                          npz_file_path='./data/PEMS04/pems04.npz',
#                          time_interval=300,
#                          times=288)
# print('hello world')
# trafficflow.easy_detecting(0.5, 4)
