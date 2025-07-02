import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn import functional as F
import numpy as np
import random
from collections import Counter

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split()
vocab = ['<PAD>', '<UNK>', '<USER>', '<BOT>'] + [word for word, count in Counter(words).most_common(5000) if count >= 3]
vocab_size = len(vocab)
word_to_idx = {w: i for i, w in enumerate(vocab)}
idx_to_word = {i: w for i, w in enumerate(vocab)}

data = []
current_speaker = '<USER>'
for word in words:
    if word.endswith(':'):
        current_speaker = '<BOT>' if 'bot' in word.lower() else '<USER>'
    else:
        data.append(word_to_idx.get(word, word_to_idx['<UNK>']))
        data.append(word_to_idx[current_speaker])

embed_size = 128
num_heads = 4
num_layers = 4
block_size = 64  
batch_size = 32
learning_rate = 0.0003
#epochs = 2000
epochs = 1000

class DialogGPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.pos_embed = nn.Embedding(block_size, embed_size)
        self.transformer = nn.Transformer(
            d_model=embed_size,
            nhead=num_heads,
            num_encoder_layers=num_layers,
            num_decoder_layers=num_layers,
            batch_first=True
        )
        self.fc = nn.Linear(embed_size, vocab_size)

    def forward(self, x):
        B, T = x.shape
        positions = torch.arange(T, device=x.device).unsqueeze(0)
        x = self.embed(x) + self.pos_embed(positions)
        x = self.transformer(x, x) 
        logits = self.fc(x)
        return logits

model = DialogGPT()
optimizer = optim.AdamW(model.parameters(), lr=learning_rate)
criterion = nn.CrossEntropyLoss(ignore_index=word_to_idx['<PAD>'])

def get_batch():
    indices = [random.randint(0, len(data) - block_size - 1) for _ in range(batch_size)]
    x = torch.tensor([[data[i + j] for j in range(block_size)] for i in indices])
    y = torch.tensor([[data[i + j + 1] for j in range(block_size)] for i in indices])
    return x, y

for epoch in range(epochs):
    x, y = get_batch()
    logits = model(x)
    loss = criterion(logits.view(-1, vocab_size), y.view(-1))

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 200 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item():.4f}')


def generate_response(prompt, max_length=50):
    model.eval()
    tokens = [word_to_idx.get(word, word_to_idx['<UNK>']) for word in prompt.split()]
    tokens.append(word_to_idx['<BOT>'])

    for _ in range(max_length):
        x = torch.tensor([tokens[-block_size:]]).long()
        logits = model(x)
        probs = F.softmax(logits[0, -1, :], dim=-1)
        next_token = torch.multinomial(probs, num_samples=1).item()
        tokens.append(next_token)
        if next_token == word_to_idx['<USER>']:
            break

    response = ' '.join([idx_to_word[t] for t in tokens if t not in [
        word_to_idx['<USER>'], word_to_idx['<BOT>'], word_to_idx['<PAD>']
    ]])
    return response


print("Диалоговый бот (для выхода введите 'exit')")
while True:
    user_input = input("Вы: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = generate_response(user_input)
    print("Софи:", response)
