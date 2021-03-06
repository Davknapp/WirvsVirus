# WirvsVirus
We aim to develop a simulation for the virus, challenge 0307

There are already multiple simulation approaches that illustrate and explain the spread of the coronavirus. These approaches are to be expanded to include the possibility of simulating the effects of one's own actions on the course of the pandemic. Users can simulate their real or fictitious behaviour and get a reaction how this effects others.

We have moved to https://github.com/youvsvirus/youvsvirus-game, you can find the current progress there.
  
## Versions and dependencies:

- Python version: 3.8
- pygame>=1.9.6
- numpy>=1.18.2

Recommended: Create a virtual environment (e.g. using conda) and install all requirements using ´pip install -r requirements.txt´

## How to run the simulation

In the main directory just execute the main.py file with python:

```
python3 main.py
```

or

```
python main.py
```

And then use the arrow keys to escape the virus.

You can additionally provide a social distancing factor between 0 and 1 as an argument.

```
python3 main.py 0.8
```

simulates 80% social distancing.

## Repo structure and coding style

- Every class gets its own file in the classes folder or a subfolder of the classes folder
- Additional ressources (images, audio, ...) should be put in the res folder
- Please see the file [Coding guidelines](https://github.com/Davknapp/WirvsVirus/blob/master/CODINGGUIDELINES.md)

## Smiley pictures

Pictures taken from <a href="https://pixabay.com/de/users/OpenClipart-Vectors-30363/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=146094">OpenClipart-Vectors</a> auf <a href="https://pixabay.com/de/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=146094">Pixabay</a> und Image by <a href="https://pixabay.com/users/Clker-Free-Vector-Images-3736/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=306283">Clker-Free-Vector-Images</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=306283">Pixabay</a> and http://pngimg.com/download/36231 and http://pngimg.com/download/36229 and http://pngimg.com/download/36097
