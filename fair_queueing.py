class Fair_queue(object):
    def __init__(self, flows):
        self.flows = flows
        self.queue = [[] * len(flows)]
        self.remain = [len(flows[i]) for i in range(len(flows))]
        self.num_flows = 0
        self.slope = 0

        t = 0
        while 1:
            self.find_packet(t)
            t += 1
            pass
        pass

    def find_packet(self, t):
            for i in range(len(flows)):
                while len(flows[i]) != 0:
                    if flows[i][0].t == t:
                        self.queue[i].append(flows[i].pop(0))
                    else:
                        break

    def is_empty(self):
        return 

            
class Packet(object):
    def __init__(self, t, s):
        self.t = t
        self.s = s

if __name__ == "__main__":
    a = [Packet(4, 1), Packet(5, 1), Packet(6, 1), Packet(7, 1), Packet(9, 1)]
    b = [Packet(1, 1), Packet(6, 1), Packet(9, 1), Packet(12, 1), Packet(14, 1)]
    c = [Packet(1, 1), Packet(4, 1), Packet(8, 1), Packet(10, 1), Packet(12, 1)]
    d = [Packet(2, 1), Packet(4, 1), Packet(5, 1), Packet(6, 1), Packet(12, 1)]
    flows = [a, b, c, d]
    a = Fair_queue(flows)
    pass