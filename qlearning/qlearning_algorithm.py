import gym
import numpy as np
import random


def qlearning(emax, tmax, gamma ,beta, epsilon, n_states, n_actions):
    env = gym.make('Taxi-v3', render_mode="ansi").env
    Q_table = np.zeros((n_states, n_actions), dtype=float)
    e = 0
    steps = []
    while e < emax:
        t = 0
        env.reset()
        state = env.s
        while t < tmax:
            if random.uniform(0, 1) < epsilon:
                action = random.randint(0, 5) # explore 
            else:
                action = np.argmax(Q_table[state]) # exploit 

            next_state, reward, done = env.step(action)[:3]
            Q_table[state][action] = (1 - beta) * Q_table[state][action] + beta * (reward + gamma * max(Q_table[next_state]))
            t += 1
            if done:
                steps.append(t + 1)
                break
            state = next_state
        e +=1
    return Q_table, steps
        
def check_agent(Q_table, tmax):
    env = gym.make('Taxi-v3', render_mode="human").env
    done = False
    env.reset()
    state = env.s
    for i in range(tmax):
        action = np.argmax(Q_table[state])
        next_state, reward, done= env.step(action)[:3]        
        if done:
            break
        state = next_state
    print(env.render())




def main():
    Q_table = qlearning(10000, 100, 0.99, 0.5, 0.1, 500, 6)[0]
    check_agent(Q_table, 1000)

    

main()