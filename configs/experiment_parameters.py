import argparse


class ExperimentOne(argparse.ArgumentParser):
    def __init__(self):
        """
        #
        Returns:
            object:
        """
        super().__init__()

        self.add_argument('--epoch', nargs='+', type=int, help='epoch number', default=500)
        self.add_argument('--step-size', nargs='+', type=float, help='task-level inner update learning rate',
                 default=[1e-5])
        self.add_argument('--b2', nargs='+', type=float, help='task-level inner update learning rate',
                 default=[0.99])
        self.add_argument('--b1', nargs='+', type=float, help='task-level inner update learning rate',
                 default=[0.99])
        self.add_argument('--mask', nargs='+', type=float, help='task-level inner update learning rate',
                 default=[0.5])
        self.add_argument('--name', help='Name of experiment', default="oml_regression")
        self.add_argument('--seed',  nargs='+', type=int, default=[0], help='Name of experiment')
        self.add_argument('--run', type=int, help='meta batch size, namely task num', default=0)

