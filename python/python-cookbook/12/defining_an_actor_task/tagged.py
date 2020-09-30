from actor import Actor


class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self,"do_"+tag)(*payload)


    # methods correponding to different message tags
    def do_A(self, x):
        print("Running A", x)

    def do_B(self, x, y):
        print("Running B", x, y)

if __name__ == '__main__':
    a = TaggedActor()
    a.start()
    a.send(('A', 1)) # invokes do_A(1)
    a.send(('B', 2, 3)) # invokes do_B(2,3)
    a.close()
    a.join()

