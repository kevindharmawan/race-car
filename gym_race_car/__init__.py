from gym.env.registration import register

register(
    id='race-car-v0',
    entry_point='gym_race_car.envs:RaceCarEnv'
)