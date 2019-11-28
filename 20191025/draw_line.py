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

    # t1_path,d1_path = '../20191025/data/aa1.txt', '../20191025/data/bb1.txt'
    # t1,d1 = getDrawLine(t1_path,d1_path)
    #
    # t2_path,d2_path = '../20191025/data/aa2.txt', '../20191025/data/bb2.txt'
    # t2,d2 = getDrawLine(t2_path,d2_path)
    #

    plt.figure(figsize=(10, 10))
    plt.plot(t1,range(0,len(d1)),color="k",label='follower1',linestyle="-")
    plt.scatter(t1, range(0,len(d1)), marker='o', color='k', s=4)
    plt.plot(t2,range(0,len(d2)),color='k',label='follower2',linestyle=":")
    plt.scatter(t2, range(0,len(d2)), marker='o', color='k', s=4, label='trigger points')

    fontsize = 35
    font = {'family': 'Times New Roman', 'weight': 'normal', 'size': fontsize}
    plt.xlabel("Trigger times", font)
    plt.ylabel("Trigger intervals",font)


    plt.legend(prop=font)
    plt.tick_params(font)
    plt.xticks(range(0,18,4),fontsize=fontsize)
    plt.yticks(range(0,175,40),fontsize=fontsize)

    plt.savefig('../20191025/pic/p1.eps')
    # plt.savefig('../20191025/pic/p2.eps')



    # plt.plot(t1,range(0,len(d1)),color="k",label='follow1',linestyle="-",marker='.')
    # plt.plot(t2,range(0,len(d2)),color='k',label='follow2',linestyle=":",marker='.')
    #
    # plt.ylabel("Trigger points")
    # plt.xlabel("Trigger intervals")
    # plt.legend()
    # plt.savefig('../20191025/pic/p2.eps')




