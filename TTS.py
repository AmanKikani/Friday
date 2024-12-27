import torch
import torchaudio
import ChatTTS
import os
import sys
import getopt
import threading

torch._dynamo.config.cache_size_limit = 64
torch._dynamo.config.suppress_errors = True
torch.set_float32_matmul_precision('high')

chat = ChatTTS.Chat()
chat.load(compile=True) # Set to True for better performance
def main(texts,num):
    print(texts)
    wavs = chat.infer(texts)
    for i in range(len(wavs)):
        try:
            torchaudio.save(f"speech{num}.mp3", torch.from_numpy(wavs[i]).unsqueeze(0), 24000)
        except:
            torchaudio.save(f"speech{num}.mp3", torch.from_numpy(wavs[i]), 24000)

if __name__ == "__main__":
    texts = "This is a first sentence. This is a second sentence. This is the third sentence. This is the fourth sentence. This is the fifth sentence."
    texts = texts.split(".")
    x = 0
    arr = []
    '''
    t1 = threading.Thread(target=main, args=(texts[0],))
    t2 = threading.Thread(target=main, args=(texts[1],))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    '''
    print(texts)
    # x = 0
    # t0 = threading.Thread(target=main, args=(texts[0],))
    # t1 = threading.Thread(target=main, args=(texts[1],))
    # '''    while x < len(texts):
    #     exec(f't{x} = threading.Thread(target=main, args=(texts[{x}],))')
    #     x+=1'''
    #
    # x = 0
    # while x < len(texts):
    #     exec(f't{x}.start()')
    #     x += 1
    # x = 0
    # while x < len(texts):
    #     exec(f't{x}.join()')
    #     x += 1

    threads = []
    x = 0
    for i in range(len(texts)):
        t = threading.Thread(target=main, args=(texts[i],x))
        threads.append(t)
        t.start()
        x += 1
    x = 0
    print("Done")