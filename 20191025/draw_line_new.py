import codecs
import matplotlib.pyplot as plt


def getDrawLine(input_time_path,input_stream_path):

    with codecs.open(input_time_path) as td:
        time_data = td.readlines()

    with codecs.open(input_stream_path) as md:
        stream_data = md.readlines()

    t1 = [float(time.strip()) for time in time_data]
    m1 = [float(stream.strip()) for stream in stream_data]

    tm_data = zip(t1, m1)
    filter_tm_data = [item for item in tm_data if item[1] > 0]
    filter_tm_data = list(zip(*filter_tm_data))

    filter_time = list(filter_tm_data[0])
    filter_data = list(filter_tm_data[1])

    return filter_time,filter_data

if __name__ == '__main__':


    # t1_path,d1_path = '../20191025/data_new/agent11_time.txt', '../20191025/data_new/agent11_data.txt'
    # t1,d1 = getDrawLine(t1_path,d1_path)
    #
    # t2_path,d2_path = '../20191025/data_new/agent22_time.txt', '../20191025/data_new/agent22_data.txt'
    # t2,d2 = getDrawLine(t2_path,d2_path)

    t1_path,d1_path = '../20191025/data_new/agent1_time.txt', '../20191025/data_new/agent1_data.txt'
    t1,d1 = getDrawLine(t1_path,d1_path)

    t2_path,d2_path = '../20191025/data_new/agent2_time.txt', '../20191025/data_new/agent2_data.txt'
    t2,d2 = getDrawLine(t2_path,d2_path)

    figsize = 50, 39
    figure, ax = plt.subplots(figsize=figsize)
    plt.scatter(t1,range(0,len(d1)),color="r",label='follower1',linestyle="-")
    plt.scatter(t2,range(0,len(d2)),color='b',label='follower2',linestyle=":")

    fontsize = 180
    font = {'family': 'Times New Roman', 'weight': 'normal', 'size': fontsize, 'style':"normal"}
    plt.xlabel("Time(s)", font)
    plt.ylabel("Trigger times",font)
    plt.legend(prop=font, loc=4)


    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]

    plt.xticks(range(0,33,10), fontsize=fontsize)
    plt.yticks(range(0,200,40),fontsize=fontsize)


    plt.savefig('../20191025/pic/p5.eps')
    #plt.show()





