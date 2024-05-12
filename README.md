# easy-anomalies-detecting
usage: run.py [-h] [--distance-dataset DISTANCE_DATASET] [--traffic-flow-dataset TRAFFIC_FLOW_DATASET] [--time-interval TIME_INTERVAL] [--times TIMES] [--roads ROADS] [--model {easy_detecting,dn_detecting}] [-k K]

Process command line arguments

optional arguments:
  -h, --help            show this help message and exit
  --distance-dataset DISTANCE_DATASET
                        distance dataset file path
  --traffic-flow-dataset TRAFFIC_FLOW_DATASET
                        traffic flow dataset file path
  --time-interval TIME_INTERVAL
                        Time interval (default: 300)
  --times TIMES         Number of times (default: 288)
  --roads ROADS         Number of roads (default: 4)
  --model {easy_detecting,dn_detecting}
                        model type
  -k K                  Parameter k (required when model type is easy_detecting)