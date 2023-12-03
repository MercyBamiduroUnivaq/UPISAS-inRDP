import pprint, time
from UPISAS.exemplar import Exemplar
import logging
pp = pprint.PrettyPrinter(indent=4)
logging.getLogger().setLevel(logging.INFO)

# TODO add actual exemplar name
class YourExemplar(Exemplar):
    """
    A class which encapsulates a self-adaptive exemplar run in a docker container.
    """
    def __init__(self, auto_start: "Whether to immediately start the container after creation" =False, container_name = "suave"):
        my_docker_kwargs = {
            "name":  container_name,   # TODO add your container name
            "image": "suave:dev", # TODO add your exemplar's image name
            "ports" : {6901:6901, 4902:4902, 8000:8000}}              # TODO add any other necessary ports

        super().__init__("http://localhost:8000", my_docker_kwargs, auto_start)
    
    def start_run(self):
        pass
        # TODO start a simulation run within the exemplar's container (see swim.py)
