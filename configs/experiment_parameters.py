import argparse


class ExperimentOne(argparse.ArgumentParser):
    def __init__(self):
        super().__init__()

        self.add_argument('--epoch', nargs='+', type=int, help='Number of learning steps', default=500)
        self.add_argument('--step-size', nargs='+', type=float, help='Step-size parameter',
                          default=[1e-5])
        self.add_argument('--b2', nargs='+', type=float, help='Value of b2 parameter of Adam',
                          default=[0.99])
        self.add_argument('--b1', nargs='+', type=float, help='Value of b1 parameter of Adam',
                          default=[0.99])
        self.add_argument('--name', help='Name of experiment', default="sweep_test")
        self.add_argument('--seed', nargs='+', type=int, default=[0], help='Value of the seed')
        self.add_argument('--run', type=int,
                          help='Run number to index the right experiment. This parameter must be specified', default=0)
