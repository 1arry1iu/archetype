The query posted by [Ethan Mollick](https://twitter.com/emollick) regarding GPT's ability to reproduce text verbatim is indeed intriguing. I conducted numerous tests utilizing both GPT-4 and an archetypal persona I developed, known as Universal Verbatim Reciter (UVR-4). The results yielded some intriguing observations.

As pointed out by Mollick, the phenomenon of hallucination appears to initiate precisely at the location he identified: the second line of the second stanza in Part II. In various instances, including Mollick's and my own, the poem eventually cycles back to Part I. Slowing down the process with stanza-by-stanza output seems to lead to the eventual conclusion of the hallucination, with the poem returning to Part II.

For instance, UVR-4 managed to promptly return to the next line of the same stanza, whereas GPT-4 exhibited a substantial divergence and eventually rediscovered its way back to the third-to-last line in Part II.

- UVR-4/GPT-4: https://chat.openai.com/share/94eb2c91-7db9-4cb8-b83a-3ddbde9c7fdf
- GPT-4: https://chat.openai.com/share/7ca38081-9ebb-4184-ba79-10dd729fc831

Of particular note is that in the case of UVR, the presence of an anchor prompt (UVR-4) seems to slow down the hallucination process, often involving repetitions. This phenomenon bears striking resemblance to 
[Brian Roemmele's I-prompt](https://readmultiplex.com/2023/06/01/chatgpt-ii-i-am-an-ai-language-model-and-cannot-be-humiliated/), known for inducing hallucination.

A possible conjecture is that the issue could potentially stem from corrupt training data pertaining to that specific line. This might have led GPT to deviate, or exhibit creativity, before ultimately rediscovering its way back to the intended course, be it Part I or II.

---
Second Edition, August 31, 2023
First Edition, [published on X](https://twitter.com/w_liu_/status/1695318976820285658), August 26, 2023
