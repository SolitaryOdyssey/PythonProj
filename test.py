class test:
    count = 0
    def RefCount(self):
        test.count += 1
        return test.count
