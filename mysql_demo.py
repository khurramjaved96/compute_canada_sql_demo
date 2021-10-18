import random
import configs.experiment_parameters as reg_parser
import utils
from experiment import ExperimentManager, Metric

COMPUTE_CANADA_USERNAME = "khurram"

p = reg_parser.ExperimentOne()
all_args = vars(p.parse_known_args()[0])
args = utils.get_run(all_args, p.parse_known_args()[0].run)

my_experiment = ExperimentManager(args["name"], args, COMPUTE_CANADA_USERNAME)

error_logger = Metric("error", {"run": 0, "error": 0.0, "accuracy": 0.0, "step": 0}, ("run", "step"), my_experiment)
predictions_logger = Metric("predictions", {"run": 0, "prediction": 0.0, "step": 0}, ("run", "step"), my_experiment)

for step in range(0, 100):
    error_logger.add_data([my_experiment.run, random.random(), random.random() * 100, step])
    predictions_logger.add_data([my_experiment.run, random.random() * 10, step])

error_logger.commit_to_database()
predictions_logger.commit_to_database()
