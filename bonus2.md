# Scientific Programming: A Crash Course

## Bonus Class 2 – Behavioral Experiments

In this bonus class we're going to focus on coding experiments, which you will likely want to do at some point during your PhD if you are in Cognitive Neuroscience. Since we are now building experiments, we won't want to use Jupyter notebooks; as you can imagine, it doesn't make much sense to run an experiment inside a notebook. So, this raises a question: What should we use to write and run our Python code?

In theory, you could use the plain text editor that comes bundled with your operating system (Notepad on Windows, TextEdit on Mac); however, these are actually not very good choices for programming, since they are not designed for editing code. They do not, for example, automatically color-code the syntax to make the code more readable; nor do they indent the code automatically or provide keyboard shortcuts for common coding manipulations.

One option is to use [Spyder](https://www.spyder-ide.org), which is included in the Anaconda distribution. Spyder is what's known as an IDE (an integrated development environment). It includes lots of extra tools that are useful for programming in Python – for example, a file manager, debugger, integrated plot viewer, and so on. Check out the website to get the general idea, or take a look at the app itself.

One limitation of Spyder is that it's Python specific. If you code in lots of different languages, you may prefer to adopt a single, general text editing application that you can use for lots of different things. Indeed, you may already have a preferred editor if you've done a bit of coding before. The advantage of this general approach is that you only have to learn one tool, but the disadvantage is that that tool is less well designed for each specific language. Here are some popular editors that you can investigate:

- [Atom](https://atom.io)

- [Brackets](https://brackets.io)

- [Sublime Text](https://www.sublimetext.com)

- [VSCode](https://code.visualstudio.com)

Personally, I find that using a single tool for all the coding I do (Bash, CSS, HTML, JavaScript, LaTeX, Markdown, Matlab, PHP, Python, and R) makes me more productive. But even if you don't adopt a text editor today, I would highly recommend that you investigate this in the future and find something that works well for your needs.

For the purpose of building experiments, another option is to use the "Coder" tool that is provided as part of PsychoPy (see below). This will be sufficient for coding up a lab experiment, but if you want to create a web-based experiment in JavaScript (see below), you will need a more general purpose text editor that is not specific to Python.


## Lab Experiments with PsychoPy

There are lots of different tools to build experiments, but the most widely used package in the Python ecosystem is PsychoPy. If you've run any experiments before, you may have used Eprime or Psychtoolbox, which work in a similar way to PsychoPy. There are three main ways to use PsychoPy:

1. The PsychoPy "Builder": This allows you to create experiments using a point-and-click visual interface. This can be useful for quickly making something that works, but, in general, it gives you less control and can be more cumbersome to use. You may decide to use the Builder interface in the future, but for the purpose of this course – which is about learning to code – I want you to create your experiments manually without using the Builder.

2. The PsychoPy "Coder": This is essentially just a text editor (like the apps I recommended above), but the Coder is a little more specific to Python and PsychoPy in particular. In the Coder interface, you type the code for your experiment and then hit the green run button to run it. For today, I would recommend this option.

3. You can also install PsychoPy as a regular package using `pip` and then run your experiment script from the terminal. Personally, this is what I do because I find the PsychoPy GUI interface to be slow and clunky. However, it can be a bit fiddly to get PsychoPy to install correctly on some systems.

### Option 2 – Easy, recommended

This option should be relatively painless and straightforward. Go to the PsychoPy website and download the "Standalone PsychoPy": https://www.psychopy.org/download.html The app is quite big and might take some time to download and install. This is because the standalone version of PsychoPy basically bundles everything you need into one giant package – it even incorporates its own internal version of Python.

Once you've installed it, you can open the PsychoPy app and you'll see three windows: The Builder, the Coder and the Runner. Go ahead and close the Builder – you won't need this today. In the Coder interface, you can then open the `experiment.py` code and start playing around with the experiment (see activities below).

### Option 3 – Complicated

If you would like a more minimalist installation, you can install PsychoPy using `pip`:

```python
pip install psychopy
```

although it may be sensible to make a separate virtual environment first if you are comfortable with doing that:

```bash
python3 -m venv psychopy_venv
source psychopy_venv/bin/activate
pip install psychopy
```

Personally, I had a few issues getting this working because there were some other dependencies I needed to install first. So, if you go down this road and bump into issues, it's probably best to opt for Option 2 above. For more info, check PsychoPy page which also explains more options for setting things up with Anaconda: https://www.psychopy.org/download.html

Finally, note that if you choose this option, you won't have access to the Builder or Coder interfaces – just the core PsychoPy package. Therefore you will need to use your own text editor to read/write/run the code.


## Activities

Make sure you've downloaded the two Python files for this class (`bonus2/lab_experiment.py` and `bonus2/results.py`) and then work through the following activities, which are roughly in order of difficulty. Get my attention if you need any help.

### Experiment activities

1. Run `experiment.py` to check that everything works correctly.

2. Increase the number of repetitions to four or five and try the experiment again. Use `results.py` to look at your results. Try the experiment several times to see how consistent your results are.

3. Change the background color to black and the foreground color (text and dots) to white. You might need to look around online to find out how to change colors.

4. Make the experiment script more organized by using functions. For example, you could create a function that takes `n_dots` as input and draws that number of dots on the screen.

5. Try modifying the code to collect reaction time data? Do you respond faster when there are fewer dots?

6. A potential issue with the code at the moment is that dots can overlap. At the moment, we simply generate random positions on the screen without checking where the other dots are located. Write a function to generate *n* dot positions that are non-overlapping, taking into account the `DOT_RADIUS`.

7. Make an option that controls how densely clustered the dots are? Is the task easier if the dots are more densely clustered?

### Analysis activities

1. Try creating your own Jupyter Notebook to document your analyses, and then try the following:

2. How would you extend the analysis to multiple subjects? Can you plot an accuracy curve averaging over participants? Would it perhaps make sense to create a violin plot?

3. Another useful way to look at numerosity estimation data is to plot the correct answer on the *x*-axis against the subject's response on the *y*-axis. This will allow you to see if people tend to over- or underestimate numerosities. Try to write some plotting code to make such a plot.


## Online Experiments with jsPsych

Online experiments are gradually becoming much more popular in psychology and the social sciences. However, there are quite a few skills you need to learn if you want to run experiments this way. To keep things familiar, we will continue with the same numerosity estimation experiment that we played with above. This means you can still use any Python analysis code that you already wrote – the only thing that's changing is that the experiment will now be run in the browser.


## JavaScript

Unfortunately, web experiments can not be written in Python. This is because the only programming language that web browsers understand is [JavaScript](https://www.javascript.com). The JavaScript language is strictly limited in what it can do because there would be security issues if websites could just run any random program on your computer. For example, JavaScript cannot read or write files to your computer. However, like Python, JavaScript is a high-level programming language with a syntax that is quite English-like. Many of the core constructs will seem familiar, even if the precise syntax is a little different. Learning JavaScript is well outside the scope of this course, but here are a few comparisons between Python and JavaScript to give you the general idea:

**Variable creation in Python:**

```python
magic_number = 3.14159
```

**Variable creation in JavaScript:**

```javascript
var magic_number = 3.14159;
```

**If-statement in Python:**

```python
if magic_number < 4:
	print('Magic number is less than 4')
```

**If-statement in JavaScript:**

```javascript
if (magic_number < 4) {
	console.log('Magic number is less than 4');
}
```

**For-loop in Python:**

```python
for thing in list_of_things:
	print(thing)
```

**For-loop in JavaScript:**

```javascript
for (thing of list_of_things) {
	console.log(thing);
}
```

**Function in Python:**

```python
def my_func(argument1, argument2):
	return argument1 + argument2
```

**Function in JavaScript:**

```javascript
function my_func(argument1, argument2) {
	return argument1 + argument2;
}
```

One of the nice things about working with JavaScript is that you don't need very much software to get started. All you need is a web browser (to run the experiment) and a code editor (to edit the code). If you don't already have a favorite text editor, I would recommend that you download one now (have a look at the ones I listed at the top of this page – they are mostly equivalent in functionality). The general usage pattern is that you use the text editor to write and edit the code, and you use the web browser to run the code.

## jsPsych

jsPsych is a JavaScript library for online experiments and is roughly equivalent to PsychoPy. It provides a lot the core infrastructure you need for experiments, like creating stimuli, randomizing trials, and capturing participant responses. You can read more about it here: https://www.jspsych.org jsPsych is not the only library for building online experiments, but it is increasingly becoming the standard package that people use for this purpose.

Note that you don't actually need to download jsPsych. Instead, the jsPsych library is linked in your script file and downloaded automatically by each participant when they open the experiment.

If you would like to explore jsPsych further, a good place to start is the tutorial on the jsPsych website: https://www.jspsych.org/7.1/tutorials/rt-task/ I'd also highly recommend this course from my former PhD advisor, Kenny Smith: https://kennysmithed.github.io/oels2021/ It's a little bit more focused on language experiments, but there's still lots of general advice that will apply whatever type of experiment you want to run.


## Activities

Make sure you've downloaded the three files for this class (`bonus2/web_experiment.html`, `bonus2/results.py`, and `bonus2/transform.py`) and then work through the following activities, which are roughly in order of difficulty.

### Experiment activities

1. Open `experiment.html` in a web browser to check that everything works correctly.

2. Once you get the data at the end, copy it into a new file, save it as `.json`. Use the `transform.py` script to convert the raw JSON data to CSV for analysis.

3. Use `results.py` to look at your results. Increase `N_REPS` and try the experiment several times to collect a larger dataset.

4. Change the background color to black and the foreground color (text and dots) to white. You might need to look around online to find out how to change colors (hint: you will probably want to add a new `<style>` tag in the HTML where you can specify formatting parameters).

5. I didn't add any comments to the code to explain how it works. Read through the code and add you own comments to explain how different parts of the code work.

6. The code has the same issue as the PsychoPy version: dots can potentially overlap. Write a function to generate *n* dot positions that are non-overlapping (i.e. by taking into account the `DOT_RADIUS`). You might find it easier to write a Python version first and then try to translate it to JavaScript.

7. Make an option that controls how densely clustered the dots are? Is the task easier if the dots are more densely clustered? Again, you might find it easier to write a Python version first. This is quite hard – first you need to decide what it even means for dots to be densely or sparsely clustered.

### Analysis activities

1. If you didn't already, create a new notebook to record your analyses.

2. Collect data from both the PsychoPy version of the experiment and the jsPsych version, and then compare the results. Are there any differences? For example, maybe reaction times are recorded differently in each version.

3. If you didn't already do this in the last class, try plotting the correct number of dots (*x*-axis) against the number of dots estimated by participants (*y*-axis). Are you able to replicate the effect where people underestimate larger numbers?

4. Instead of having a separate CSV file for each participant, it might make more sense to merge everything together into a single CSV file with an extra `subject_id` column. Can you figure out a way to do this? Perhaps it would be best to write a preprocessing script that merges all the data together into one big file.

5. Try to make a plot that captures across-participant variation by using a box plot or violin plot. If you feel more confident in R, try using R to read in the data and make the plots.


## Totally Optional Extra Work

Try to create a new experiment from scratch using either PsychoPy or jsPsych. You can pick an experiment that you've run before or something you would like to run in the future. If you don't have any ideas, try coding up a classic experiment, like [the Stroop task](https://en.wikipedia.org/wiki/Stroop_effect). Even if you can't implement all parts of the experiment, try to get some parts working (e.g. the instructions screen, the training procedure, the test trials, the data handling, the analysis script, etc...). You will probably need to do lots of Googling to find out how things are done.
