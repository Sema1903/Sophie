<h1>Sophie</h1>

<h2>Decription</h2>
Issuies Sophie is the simple LLM based on transformers' model learning and on the dataset in the 'text.txt'. The target of project is creating the virtual friend and Sophie'll be learned on dialogs in real chats to be more plausible.

<h2>Abilities</h2>
Sophie can answer for your questions and due to easy configuration you can learn she as you want. In default she is learned on the real dialogs in my chats.

<h2>How to install</h2>
To download Sophie you should download 2 files: Sophie.py with the main code and text.txt with based dataset. 
If you havn't installed python, you should instell it. All frameworks are in default. 
If you want to change dataset for your tasks, you need to change text.txt. WARNING! your new dataset must look like: 
    user: ...
    bot: ...
And after all settings you need to run Sophie.py. You can do it if you go to the your directory and put <strong>python Sophie.py</strong> or <strong>python3 Sophie.py</strong> in the terminal
This program is whery hard to run, so if you have the weak GPU it'll learn very long time. If it's a problem, you should make your dataset lower or change number of epochs in the main script. To do it, you should change the number in the name <strong>epochs</strong> on lower content in the Sophie.py
WARNING! You shouldn't change number of epochs lower then 1000, cause she need to learn harder. 
After running, she'll write you the number of learning epochs and loss. If the number of epochs is 1000 (in default) or in your number and loss are upper then 1: you should make the number of epochs upper in Sophie.py and learn she again or make the dataset lower.
How more epochs she learned then cleverer she became.
If you see th e message <strong>Вы:</strong> it means that everything is OK!

<h2>Development</h2>
It is the simple LLM based on transformers' model. Language is the Python and frameworks are NumPy for math and PyTorch for ML and realisation transformers' model. 
She read <strong>text.txt</strong>, after then she tokenies words and on transformers model makes the descigion of the next word in the your text.

I know nothing in AI, so I guess, that Sophie'll have lots of problems, but I'll glad to hear your advises, and I'm sure that none want to work with it. 

Thank you for your attention
