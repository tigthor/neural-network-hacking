# Hacking Neural Networks: A Short Introduction

<span style="color:red">**Disclaimer: This article and all the associated exercises are for educational purposes only.**</span>

This repository provides a comprehensive introduction to various offensive techniques using neural networks. The methods covered include bug hunting, shellcode obfuscation, information extraction, malware injection, backdooring, and more.

Each method is accompanied by an exercise, allowing you to practice and understand the concepts hands-on. You can find the detailed article here in '[Article.pdf](Article.pdf)' or on arXiv ([arXiv:1911.07658](https://arxiv.org/pdf/1911.07658.pdf)).

---

## Setup

### Python and pip

Download and install Python3 and its package installer pip using a package manager or directly from the [official website](https://www.python.org/downloads/).

### Editor

An editor is required to work with the code, preferably one that supports Python syntax highlighting. Some recommended editors are:

- [Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial)
- Vim/Emacs

### Packages

To run the exercises, you will need to install several Python packages:

- **Keras**: Follow the [official installation guide](https://keras.io/#installation). TensorFlow is recommended as the backend, preferably the GPU-enabled version if available.
- **NumPy**, **SciPy**, and **scikit-image**: Install these helper packages for numerical operations and image processing. Follow the [SciPy installation instructions](https://www.scipy.org/install.html) and [scikit-image installation guide](https://scikit-image.org/docs/stable/install.html).
- **PyCuda**: Required for GPU-based attack exercises. If you don't have an NVIDIA GPU, you can skip this. Follow the [PyCuda installation guide](https://wiki.tiker.net/PyCuda/Installation).
- **NLTK**: Necessary for natural language processing tasks. Follow the [NLTK installation instructions](https://www.nltk.org/install.html).

---

## The exercises

This repository includes a variety of exercises, each focusing on a different aspect of neural network attacks:

- **0 - Last Layer Attack**: Understand and manipulate the last layer of a neural network.
- **1 - Backdooring**: Inject backdoors into neural network models.
- **2 - Extracting Information**: Extract sensitive information from neural networks.
- **3 - Brute Forcing**: Develop brute-force strategies for image-based security.
- **4 - Neural Overflow**: Explore neural network overflow vulnerabilities.
- **5 - Malware Injection**: Inject malware into neural networks.
- **6 - Neural Obfuscation**: Obfuscate neural network operations.
- **7 - Bug Hunting**: Use neural networks to find vulnerabilities in code.
- **8 - GPU Attack**: Attack GPU-based authorization systems.

For detailed instructions, please read the `README.md` file in each exercise directory.

---

## Further Reading / Watching

For more information on security and machine learning, check out the following resources:

- Isao Takaesu's course on [Security and Machine Learning](https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/Security_and_MachineLearning)
- Will Pearce and Nick Landers' [Talk at Derbycon 2019](https://www.youtube.com/watch?v=CsvkYoxtexQ) on Offensive Machine Learning techniques.
- The [Deep Learning Book](http://www.deeplearningbook.org/) by Ian Goodfellow, Yoshua Bengio, and Aaron Courville.
- The [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) book by Aurélien Géron.

---

## Contributing

Contributions are welcome! If you find errors or missing references, feel free to make a PR or contact me.

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

Please ensure that your contributions align with the repository's purpose and follow the established coding standards
---

## What else?

The neural networks found in the exercises are based on the examples provided by [keras](https://keras.io/).

If you find that there are errors or missing references, feel free to make a PR or contact me.
