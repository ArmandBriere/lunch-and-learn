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
def train(
    model: BERTClassifier,
    data_loader: DataLoader,
    optimizer: AdamW,
    scheduler,
    device,
    index,
):
    model.train()

    for batch in tqdm(data_loader):
        optimizer.zero_grad()

        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["label"].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask)

        loss = torch.nn.CrossEntropyLoss()(outputs, labels)
        loss.backward()

        optimizer.step()
        scheduler.step()

    # Save model checkpoint after each batch
    torch.save(model.state_dict(), f"/data/model_checkpoint_{index}.pth")
```

---


```python
model.train()
```

Set the model in `training` mode

---

```python
for batch in tqdm(data_loader):
```

`data_loader` is an object that contains the data to train the model.

---

### But what is my data?

---

| `is_offensive` | `text`       |
| -------------- | ------------ |
| 0              | "I love you" |
| 1              | "f*ck you"   |

---

But I have 180 000 rows of that

...

For training

---

And wednesday night at 1am

I found 160 000 new rows for testing

---

### Few examples

![Few examples](./assets/get_ready.webp)

---


"Thanks for the heads up! I will take a look!"

"Quick Question 
Why do I need to join the discussion if it's resolved lol?"

---

"Leaders of the Christian Reconstruction movement expect a large majority of citizens worldwide eventually to accept Christ as savior. We believe in postmillennialism. Those who do not share our confidence concerning the future success of the gospel, as empowered by the Holy Spirit, believe that an earthly kingdom must be imposed by force from the top down (premillennialism), or else they do not believe in an earthly institutional kingdom at all (amillennialism).' Gary North, Political Polytheism, pp. 586-587."

---

That was a few non-offensive examples, you can imagine the offensive ones...

You don't need me for this part

---

### Okay, data is good, but now what?

---

### You need to tokenize your data

---

> Tokenizing a text is splitting it into words or subwords,

---

```txt
"Don't you love 🤗 Transformers? We sure do."
```

---

```txt
["Don't", "you", "love", "🤗", "Transformers?", "We", "sure", "do."]

["Don", "'", "t", "you", "love", "🤗", "Transformers", "?", "We", "sure", "do", "."]
```

---

Important part

```python
outputs = model(input_ids=input_ids, attention_mask=attention_mask)
```

Those params are used in transformer-based models.

- `input_ids`: Ids of each word in the input
- `attention_mask`: Which parts to pay attention to

---

```python
optimizer.step()
scheduler.step()
```

- `optimizer.step()`: Update the weights of the model
- `scheduler.step()`: Update the learning rate

---

Tada 🎉

The model is training

---

Go grab a coffee ☕️ and...

come back in a few minutes, hours, days, weeks, months, years, centuries, milleniums?

---

![bg 50%](./assets/modal.svg)

---

![](./assets/modal-total-cost.png)

---

### Let's run it in production


---

![bg](./assets/cpu.webp)

---

Results on a 1000 samples of the test dataset:

```bash
Total inference time:  0:01:02.238444 seconds
Total bad predictions:  15
Total good predictions: 985
Accuracy: 0.9847715736040609
```

~19 iterations per second

---

![bg](./assets/gpu.jpg)

---

Test on the full dataset with an H100:

```bash
9151/159571 [01:04<14:20, 174.86it/s]
```

```bash
Total inference time:  0:15:12.663117 seconds
Total bad predictions:  1427
Total good predictions: 158144
Accuracy: 0.9909765783083772
```

~174 iterations per second

---

GPU is 9 times faster than CPU

---

# Thanks for your attention

Once again, Spot is mad

And have fun with your code 🚀


