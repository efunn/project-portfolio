---
title: 'Instabrain: real-time fMRI'
subtitle: A system to decode brain states in real time
id: p3
icon: instabrain
---
**Project Link: [github.com/lewispeacocklab/instabrain](https://github.com/lewispeacocklab/instabrain)**

![instabrain banner](@images/mri-banner.jpg)

fMRI records blood flow in the brain as a proxy for neural activity. Being able to record, decode, and display feedback from this signal in real time may allow people to control their own brain activity. When I started this project, several real-time fMRI pipelines existed but either didn't expose enough of the pipeline to allow customization (paid products) or had poorly designed architectures (research code). I am always hesitant to build my own system if a solution already exists, but here I saved myself many headaches by starting from scratch. The final set of scripts runs largely asynchronously and can be run from the same or different computers (helpful depending on the IT/networking policies of your MRI facility).

- pipeline includes **head motion correction, time-series processing, and pattern decoding** in real time
- **client-server architecture** separates fMRI processing from experiment display scripts
- **asynchronous data processing** avoids issues with unpredictable data arrival and processing times
