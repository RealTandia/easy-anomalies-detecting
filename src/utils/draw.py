from pyecharts import options as opts
from pyecharts.charts import Line
import csv


def draw_line_chart(raw_data):
    line_chart = Line()
    x_values = [d["time"] for d in raw_data[0]["road_records"]]
    line_chart.add_xaxis(xaxis_data=x_values)

    count = 0
    for road in raw_data:
        y_values = [d["congestion"] for d in road["road_records"]]

        # 添加数据和标签
        line_chart.add_yaxis(series_name=f"road: {road['road']}", y_axis=y_values)
        print(str(count))
        count += 1

    # 设置标题和标签
    line_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="路段堵塞预测"),
        xaxis_opts=opts.AxisOpts(name="时间"),
        yaxis_opts=opts.AxisOpts(name="堵塞程度"),
        legend_opts=opts.LegendOpts(),
    )

    # 渲染图表
    line_chart.render("result.html")

def save_as_csv(raw_data):
    datas = list()
    datas.append(['road_num', 'time', 'congestion'])
    for road in raw_data:
        for record in road['road_records']:
            data = [road['road'], record['time'], record['congestion']]
            datas.append(data)
    with open('congestion.csv', "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(datas)