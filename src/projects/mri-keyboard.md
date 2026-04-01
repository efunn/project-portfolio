---
title: MRI-compatible keyboard
subtitle: an interface to record finger forces during fmri
id: p4
icon: keyboard
---

**Project Link: [github.com/lewispeacocklab/rewire-keyboard](https://github.com/lewispeacocklab/rewire-keyboard)**

![keyboard banner](@images/keyboard-banner.jpg)

Yes, you can put (some) electronics inside an MRI scanner. This device was used to measure the force output of each finger during imaging of the motor cortex. The real-time measurements were integrated into a game that was played during fMRI scanning. The force sensor I used had both differential power and output signals, which, when transmitted over twisted pairs, cancelled out almost all of the electrical noise introduced by the MRI scanner during operation.

- **force keyboard module** with minimal electronics sits on the patient's lap
- force signals for each finger are transmitted over twisted wire pairs into the scanner control room and amplified on the **controller module**
- device appears as a **standard USB joystick** for easy integration into any experiment
