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

    t1_path,d1_path = '../20191025/data/a1.txt', '../20191025/data/b1.txt'
    t1,d1 = getDrawLine(t1_path,d1_path)

    t2_path,d2_path = '../20191025/data/a2.txt', '../20191025/data/b2.txt'
    t2,d2 = getDrawLine(t2_path,d2_path)

    plt.plot(t1,range(0,len(d1)),color="k",label='follow1',linestyle="-")
    plt.plot(t2,range(0,len(d2)),color='k',label='follow2',linestyle=":")

    plt.xlabel("Trigger times")
    plt.ylabel("Trigger intervals")
    plt.legend()
    plt.show()


    # t1_path,d1_path = '../20191025/data/aa1.txt', '../20191025/data/b1.txt'
    # t1,d1 = getDrawLine(t1_path,d1_path)
    #
    # t2_path,d2_path = '../20191025/data/a2.txt', '../20191025/data/b2.txt'
    # t2,d2 = getDrawLine(t2_path,d2_path)
    #
    # plt.plot(t1,range(0,len(d1)),color="#8dd3c7",label='follow1')
    # plt.plot(t2,range(0,len(d2)),color='#8dd3c5',label='follow2')
    #
    # plt.ylabel("Trigger times")
    # plt.xlabel("Trigger intervals")
    # plt.legend()
    # plt.show()




