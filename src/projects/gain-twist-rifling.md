---
title: Gain Twist Rifling Machine
subtitle: a G-code generator for variable twist rifling
id: p5
icon: rifling
---

**Project Link: [github.com/efunn/gaintwist-rifling](https://github.com/efunn/gaintwist-rifling)**

![rifling banner](@images/rifling-banner.jpg)

This project started many years ago with one of the first Python scripts I ever wrote. My dad was building a machine to cut rifle barrels and wanted to automate the generation of G-code (the commands to move the machine). The original script was written in Python 2.7 and ran on an airgapped Windows XP computer that operated the CNC machine. I have since modernized the code and added new rifling profile options.

- generates **G-code for a 2-axis CNC machine** to cut rifling with an accelerating twist
- **combines linear and rotational movement** to operate a virtual third axis which advances the rifling cutter depth
- uses YAML configurations to select parameters such as **twist rates, rifling profiles, and cutter depth advancements**
