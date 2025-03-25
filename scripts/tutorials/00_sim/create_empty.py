"""This script demonstrates how to create a simple stage in Isaac Sim.

.. code-block:: bash

    # Usage
    ./isaaclab.sh -p scripts/tutorials/00_sim/create_empty.py

"""

"""Launch Isaac Sim Simulator first."""

import argparse

from isaaclab.app import AppLauncher

# create argparser
parser = argparse.ArgumentParser(description="Tutorial on creating an empty stage.")
# append Applaunch cli args
AppLauncher.add_app_launcher_args(parser)
# parse args
args_cli = parser.parse_args()
# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Rest everything follows."""

from isaaclab.sim import SimulationCfg, SimulationContext


def main():
    """Main function."""

    # initialize simulation context
    sim_cfg = SimulationCfg(dt=0.01)
    sim = SimulationContext(sim_cfg)
    # set main camera
    sim.set_camera_view((2.5, 2.5, 2.5), (0.0, 0.0, 0.0))

    # play simulator
    sim.reset()
    print("[INFO]: Setup complete...")

    # simulate physics
    while simulation_app.is_running():
        sim.step()


if __name__ == "__main__":
    # run main function
    main()
    # close sim app
    simulation_app.close()
