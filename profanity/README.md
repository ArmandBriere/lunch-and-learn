---
marp: true
color: white
theme: uncover
paginate: true
class: invert
---

<style>
section::after {
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
}
</style>


# Profanity detected 👀

---

http://spot.brierearmand.com/

---

# Spot is mad

---

He's mad because he's a bot and he doesn't like profanity

How does he know?

---

# Google Bert

---

![Bert](./assets/bert-google.webp)

---

Bert is a language model developed by Google:

- NLP model
- Perfect for sentiment analysis to process words and relation between them

---

![Brazil traveler](./assets/brazil-traveler.webp)

---

# Some code

---

## Training

---


```python

class TextClassificationDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(
            text,
            return_tensors="pt",
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
        )
        return {
            "input_ids": encoding["input_ids"].flatten(),
            "attention_mask": encoding["attention_mask"].flatten(),
            "label": torch.tensor(label),
        }
```

---

### Tokenizer?
