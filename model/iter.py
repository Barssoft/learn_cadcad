from radcad import Model
from model.system_parameters import parameters
from model.state_variables import initial_state
from model.state_update_blocks import partial_state_update_blocks

model_generator = iter(
    Model(
        initial_state=initial_state,
        state_update_blocks=partial_state_update_blocks,
        params=parameters,
    )(raise_exceptions=False, deepcopy=False, drop_substeps=True)
)

timesteps = 1000

for t in range(timesteps):
    model = next(model_generator)
    model(raise_exceptions=False, deepcopy=False, drop_substeps=True)
    state = model.state
    a = state["timestep"]

    if state["timestep"] % 100 == 0:
        print(f"Timestep {t}: {a}")
