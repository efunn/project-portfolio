---
title: Mini Robot Bike
subtitle: A toy that balances and gets itself back up
id: p8
icon: aow
---

**Project Link: <a href="https://github.com/efunn/aow-bike-sim" target="_blank">github.com/efunn/aow-bike-sim</a>**

![mini robot bike banner](@images/aow-banner.jpg)

This project is a sim-to-real showcase using an uncommon balancing method: the bike's rear omni wheel drives not only forward and backward, but also side to side. The neural-network control policy, trained entirely in a physics simulation, handles both balance and ground movement. Driving the bike takes just two external inputs (a heading direction and a velocity vector). If the bike gets knocked over, panels on the sides of the bike deploy to get it back on its wheels.

- **A recurrent neural-network control policy** is trained in less than an hour on modern GPU hardware
- **Curriculum-based reinforcement learning** teaches the bike in steps, progressing from simple balancing to complex maneuvers
- **Physics-based simulation** includes detailed modelling of the drivetrain, servos, and omni wheel rollers in a MuJoCo enviroment
- **An optimized linkage mechanism** gets the bike back up from falls using a single actuator to lift it from either side
